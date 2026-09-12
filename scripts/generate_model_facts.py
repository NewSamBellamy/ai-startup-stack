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

def generate_model_facts(company):
    cid = company["id"]
    name = company["name"]
    program = company["programName"]
    credits = company["maxCredits"]

    prompt = f"""You are an elite AI infrastructure engineer and FinOps auditor.
For {name}'s {program} ({credits} startup credits), provide factual details on exactly what AI models are covered by inference under these credits.

STRICT REQUIREMENTS:
1. Universal guidance for founders (no company names like OmniVeo or Shannon).
2. Bullet-point format, zero dense walls of prose.
3. Detail:
   - "proprietaryModels": Array of 3-5 flagship proprietary/hosted models covered (e.g. "Gemini 3.8 Flash", "Claude 3.5 Sonnet", "GPT-5.6 / GPT-4o", etc.)
   - "openWeightModels": Array of 3-5 open-weights models supported (e.g. "Llama 4", "DeepSeek V3/V4", "Qwen 2.5", "Gemma 4", "Mistral Large")
   - "inferenceMechanics": 1-2 sentence description of how inference is billed against credits (e.g. Serverless pay-per-token API, provisioned throughput, or GPU instances).
   - "tokenRunwayFact": 1 concrete, eye-opening fact on how far these credits stretch for AI workloads (e.g. "At $0.075 per 1M input tokens on Gemini 3.8 Flash, a $350k credit allocation covers over 2 Billion tokens—absorbs your entire production inference for 24 months.").

If the provider is a pure developer tool/fintech (like Stripe or PostHog) with no direct LLM inference endpoint, state that clearly under "inferenceMechanics" and explain what backend AI workloads it supports (e.g. PostHog LLM observability, Stripe Radar AI fraud detection).

Return STRICTLY valid JSON:
{{
  "proprietaryModels": ["Model 1", "Model 2"],
  "openWeightModels": ["Model 1", "Model 2"],
  "inferenceMechanics": "Description",
  "tokenRunwayFact": "Fact description"
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
        print(f"✓ Generated model inference facts for {name}")
        return cid, parsed
    except Exception as e:
        print(f"❌ Error on {name}: {e}")
        return cid, None

def main():
    print(f"🚀 Generating AI model inference facts for {len(companies)} companies...")
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(generate_model_facts, c) for c in companies]
        for f in as_completed(futures):
            cid, parsed = f.result()
            if parsed:
                results[cid] = parsed

    # Update dataset
    for c in companies:
        cid = c["id"]
        if cid in results:
            c["modelInference"] = results[cid]

    with open(DATASET_PATH, "w", encoding="utf-8") as f:
        json.dump(companies, f, indent=2)

    print(f"✅ Successfully updated {DATASET_PATH} with model inference facts!")

if __name__ == "__main__":
    main()
