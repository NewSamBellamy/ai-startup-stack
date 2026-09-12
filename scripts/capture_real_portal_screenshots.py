# /// script
# dependencies = [
#     "playwright"
# ]
# ///
import os
import json
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "assets/portals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("data/startup_credits_dataset.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

print(f"📸 Capturing real portal screenshots for {len(companies)} programs...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={'width': 1280, 'height': 800},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    
    for c in companies:
        cid = c["id"]
        url = c["applicationUrl"]
        out_path = os.path.join(OUTPUT_DIR, f"{cid}.png")
        print(f"Fetching {c['name']} -> {url} ...")
        
        try:
            page = context.new_page()
            # Set navigation timeout to 15s to be fast
            page.goto(url, timeout=15000, wait_until="domcontentloaded")
            page.wait_for_timeout(2000)
            page.screenshot(path=out_path, full_page=False)
            page.close()
            print(f"✓ Saved {out_path}")
            c["portalScreenshot"] = f"assets/portals/{cid}.png"
        except Exception as e:
            print(f"⚠️ Error on {c['name']}: {e}")
            # Try basic fallback if failed
            try:
                page.close()
            except:
                pass

    browser.close()

# Update dataset with screenshots
with open("data/startup_credits_dataset.json", "w", encoding="utf-8") as f:
    json.dump(companies, f, indent=2)

print("🎉 All portal screenshots captured and registered in dataset!")
