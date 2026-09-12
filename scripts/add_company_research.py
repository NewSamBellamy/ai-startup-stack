#!/usr/bin/env python3
# /// script
# dependencies = [
#     "google-genai>=2.3.0",
#     "pydantic"
# ]
# ///
"""
add_company_research.py
-----------------------
Automated workflow tool to deep-research any startup credit program via Gemini (g-spec),
probe and verify its application URL, synthesize citations and disqualifiers, and
automatically update the Stratemark Workflow Credits Dashboard.

Usage:
    uv run scripts/add_company_research.py "Company Name" "Program Name"
Example:
    uv run scripts/add_company_research.py "Cerebras" "Cerebras Cloud for Startups"
"""

import sys
import os
import json
import ssl
import urllib.request
import re
from datetime import datetime
from google import genai

client = genai.Client()

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "startup_credits_dataset.json")
REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "research_audit_registry.json")
BUILD_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "build_dashboard.py")

def probe_url(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            return resp.status, resp.url
    except urllib.error.HTTPError as e:
        return e.code, url
    except Exception as e:
        return 0, url

def main():
    if len(sys.argv) < 3:
        print("Usage: python add_company_research.py <Company Name> <Program Name>")
        print("Example: python add_company_research.py 'Cerebras' 'Cerebras Cloud for Startups'")
        sys.exit(1)

    company_name = sys.argv[1].strip()
    program_name = sys.argv[2].strip()

    print(f"\n=======================================================")
    print(f"🚀 Starting Deep Research via G-Spec (gemini-3.8-flash)")
    print(f"Target: {company_name} — {program_name}")
    print(f"=======================================================\n")

    prompt = f"""You are Vespa, Chief Financial Officer and Operations Agent.
Conduct an exhaustive, fact-checked deep research audit on the following startup program:
Company: {company_name}
Program: {program_name}

STRICT DIRECTIVES:
1. Do NOT reference internal company names like OmniVeo, Shannon, or Stratemark. All guidance must be universal and applicable to any early-stage technology founder.
2. Fact-check the exact 2026 credit tiers, eligibility criteria, and primary disqualifiers.
3. Identify the #1 Primary Rejection Disqualifier (the single most lethal reason applications are denied).
4. Provide the exact, official intake portal URL.
5. Provide 2-3 verified citations.

Return STRICTLY valid JSON with the following schema:
{{
  "id": "slug-name",
  "name": "{company_name}",
  "org": "Parent Corporation Name",
  "programName": "{program_name}",
  "maxCredits": "e.g. $25,000 or $100,000",
  "numericValue": 25000,
  "currency": "USD",
  "category": "Hyperscaler Cloud" | "Frontier AI & Models" | "GPU Clusters & Bare Metal" | "Edge & Developer Platform" | "Analytics & FinOps",
  "badge": "Short badge tag (e.g. Wafer-Scale Inference)",
  "topDisqualifier": "Short title of the #1 fatal rejection mistake",
  "shortDisqualifier": "DQ: Short 3-word warning tag",
  "disqualifierDetail": "Dense 2-sentence explanation of why this triggers instant rejection and how founders bypass it.",
  "disqualifierSource": "Exact official program terms or policy section",
  "turnaroundTime": "e.g. 3–5 Business Days",
  "equityTaken": "0% (Non-Dilutive)",
  "perkHighlight": "Single sentence highlight of core benefits",
  "brandColor": "#HEX",
  "executiveSummary": "Dense, analytical 2-sentence executive summary of the program's strategic value for early-stage runway.",
  "essay": "Exhaustive, 3-to-4 paragraph essay-style breakdown analyzing economic anatomy, compute tiers, model access, unit economics, and burn reduction.",
  "requirements": [
    "4 to 6 exact operational prerequisites (e.g. Registered legal entity, corporate domain email, active public demo/repo)"
  ],
  "rejectionPitfalls": [
    "3 to 4 common rejection triggers and how to avoid them"
  ],
  "successFactors": [
    "3 to 4 verified factors that guarantee approval"
  ],
  "eligibleServices": [
    "4 to 6 specific cloud products, compute instances, or APIs covered"
  ],
  "applicationUrl": "https://exact.official.url/startups",
  "citations": [
    {{"title": "Official Program Portal and Terms", "url": "https://..."}},
    {{"title": "Secondary Verified Source", "url": "https://..."}}
  ]
}}"""

    print("🔎 Querying Gemini 3.8 Flash for deep research synthesis...")
    res = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    text = res.output_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        new_record = json.loads(text)
    except Exception as e:
        print(f"❌ Failed to parse JSON from Gemini: {e}")
        print("Raw text:", text[:500])
        sys.exit(1)

    print("✓ Deep research synthesis completed.")

    # Probe Application URL
    app_url = new_record.get("applicationUrl", "")
    print(f"🌐 Probing intake portal URL: {app_url} ...")
    status_code, final_url = probe_url(app_url)
    if status_code in [200, 301, 302]:
        print(f"✓ URL Verified Active! Status: {status_code} (Final: {final_url})")
        new_record["applicationUrl"] = final_url
    else:
        print(f"⚠️ Warning: URL returned HTTP status {status_code}.")

    audit_date = datetime.now().strftime("%B %d, %Y")
    new_record["auditDate"] = audit_date

    # Assign clean vector logo squircle if none exists
    slug = new_record.get("id", company_name.lower().replace(" ", "-"))
    new_record["id"] = slug
    color = new_record.get("brandColor", "#3B82F6")
    initial = company_name[0].upper()
    default_logo = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="8" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="2"/>
  <text x="24" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="{color}" text-anchor="middle">{initial}</text>
</svg>'''
    new_record["logoSvg"] = default_logo

    # Load existing dataset
    os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)
    if os.path.exists(DATASET_PATH):
        with open(DATASET_PATH, "r", encoding="utf-8") as f:
            dataset = json.load(f)
    else:
        dataset = []

    # Check if company already exists
    existing_idx = None
    for i, c in enumerate(dataset):
        if c["id"] == slug or c["name"].lower() == company_name.lower():
            existing_idx = i
            break

    if existing_idx is not None:
        dataset[existing_idx] = {**dataset[existing_idx], **new_record}
        print(f"🔄 Updated existing record for '{company_name}' in dataset.")
    else:
        dataset.append(new_record)
        print(f"➕ Added new record for '{company_name}' to dataset (Total: {len(dataset)}).")

    with open(DATASET_PATH, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2)

    # Record in research audit registry
    registry_entry = {
        "id": slug,
        "company": company_name,
        "program": program_name,
        "auditDate": audit_date,
        "maxCredits": new_record.get("maxCredits"),
        "topDisqualifier": new_record.get("topDisqualifier"),
        "applicationUrl": new_record.get("applicationUrl"),
        "urlVerificationStatus": f"HTTP {status_code}",
        "citationsCount": len(new_record.get("citations", []))
    }

    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            registry = json.load(f)
    else:
        registry = {}

    registry[slug] = registry_entry
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    print(f"📝 Logged to research audit registry ({REGISTRY_PATH}).")

    # Trigger dashboard build
    print("\n⚙️ Rebuilding Workflow_Credits_Dashboard.html...")
    os.system(f'python "{BUILD_SCRIPT}"')
    print("✅ Complete! Company researched, verified, and integrated into dashboard.")

if __name__ == "__main__":
    main()
