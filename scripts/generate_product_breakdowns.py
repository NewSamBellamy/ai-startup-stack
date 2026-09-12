# /// script
# dependencies = [
#     "google-genai>=2.3.0",
#     "pydantic"
# ]
# ///
import json
import os
from google import genai
from concurrent.futures import ThreadPoolExecutor, as_completed

client = genai.Client()

DATASET_PATH = "data/startup_credits_dataset.json"

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    companies = json.load(f)

def generate_product_breakdown(company):
    cid = company["id"]
    name = company["name"]
    program = company["programName"]
    credits = company["maxCredits"]

    prompt = f"""You are a seasoned startup CTO and FinOps expert.
Many founders who receive {name}'s {program} ({credits} in credits) have NO IDEA what the platform actually offers or what half the products do. They only use 1-2 basic features and leave tens of thousands of dollars on the table.

Generate a structured, plain-English product breakdown for {name} explaining exactly what products can be used with the credits and why each one is game-changing for a startup.

STRICT FORMAT REQUIREMENTS:
1. NO long dense paragraphs. Everything must be crisp, scannable bullet points.
2. Provide 5 to 7 key platform products/services covered by the credits.
3. For each product, explain:
   - "product": Name of product (e.g. "Vertex AI", "BigQuery", "Cloud Run")
   - "role": Short category (e.g. "Serverless Container Hosting", "Foundational AI Models", "Data Warehouse")
   - "whatItIs": 1 plain-English sentence describing what it actually is (no jargon).
   - "founderValue": 1-2 punchy sentences explaining why it is helpful, how founders use it, and how it saves them thousands.
4. "hiddenPerks": 2 to 3 high-value perks included in the program founders often miss (e.g. Google Workspace credits, 20 GitHub Enterprise seats, direct 24/7 senior engineer support, hardware discounts).
5. "finOpsWarning": 1-2 sentence warning of what the credits DO NOT cover (e.g. domains, marketplace third-party software, egress).

Return STRICTLY valid JSON with schema:
{{
  "products": [
    {{
      "product": "Product Name",
      "role": "Category",
      "whatItIs": "Clear explanation",
      "founderValue": "Concrete startup benefit"
    }}
  ],
  "hiddenPerks": [
    "Perk 1 description",
    "Perk 2 description"
  ],
  "finOpsWarning": "Warning description"
}}"""

    try:
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
        parsed = json.loads(text)
        print(f"✓ Generated product breakdown for {name}")
        return cid, parsed
    except Exception as e:
        print(f"❌ Error on {name}: {e}")
        return cid, None

def main():
    print(f"🚀 Generating plain-English product breakdowns for {len(companies)} companies...")
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(generate_product_breakdown, c) for c in companies]
        for f in as_completed(futures):
            cid, parsed = f.result()
            if parsed:
                results[cid] = parsed

    # Update dataset
    for c in companies:
        cid = c["id"]
        if cid in results:
            c["productBreakdown"] = results[cid]["products"]
            c["hiddenPerks"] = results[cid]["hiddenPerks"]
            c["finOpsWarning"] = results[cid]["finOpsWarning"]

    with open(DATASET_PATH, "w", encoding="utf-8") as f:
        json.dump(companies, f, indent=2)

    print(f"✅ Successfully added structured product breakdowns to {DATASET_PATH}!")

if __name__ == "__main__":
    main()
