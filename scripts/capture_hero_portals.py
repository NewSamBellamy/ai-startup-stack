# /// script
# dependencies = [
#     "playwright"
# ]
# ///
import os
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "assets/portals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TARGETS = [
    {
        "id": "google-cloud",
        "name": "Google Cloud",
        "url": "https://cloud.google.com/startup",
        "wait": 3,
        "banner_selector": "devsite-consent, .glue-cookie-notification-bar, #onetrust-consent-sdk, [id*='cookie']",
    },
    {
        "id": "microsoft-founders-hub",
        "name": "Microsoft Founders Hub",
        "url": "https://www.microsoft.com/en-us/startups",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, #cookie-banner, .wcpConsentBannerCtrl, [id*='consent']",
    },
    {
        "id": "aws-activate",
        "name": "AWS Activate",
        "url": "https://aws.amazon.com/startups/",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, #awsccc-cb-modal, #awsccc-cs-modal, .m-nav-cookie, [id*='cookie']",
    },
    {
        "id": "nvidia-inception",
        "name": "NVIDIA Inception",
        "url": "https://www.nvidia.com/en-us/startups/",
        "wait": 4,
        "banner_selector": "#onetrust-consent-sdk, #cookie-banner, .cookie-banner, [id*='cookie']",
    },
    {
        "id": "cloudflare-startups",
        "name": "Cloudflare",
        "url": "https://www.cloudflare.com/startups/",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, .ot-sdk-row, [id*='consent'], [id*='cookie']",
    },
    {
        "id": "openai-startups",
        "name": "OpenAI",
        "url": "https://openai.com/business/why-openai/startups/",
        "wait": 4,
        "banner_selector": "#onetrust-consent-sdk, [id*='consent'], [class*='banner'], [class*='cookie']",
    },
    {
        "id": "anthropic-startups",
        "name": "Anthropic",
        "url": "https://claude.com/programs/startups",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, [id*='consent'], [id*='cookie']",
    },
    {
        "id": "oracle-cloud",
        "name": "Oracle Cloud",
        "url": "https://www.oracle.com/cloud/free/",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, #truste-consent-track, .u10, [id*='consent'], [id*='cookie']",
    },
    {
        "id": "scaleway-startups",
        "name": "Scaleway",
        "url": "https://www.scaleway.com/en/startup-program/",
        "wait": 3,
        "banner_selector": "#tarteaucitronRoot, #onetrust-consent-sdk, [id*='consent'], [id*='cookie']",
        "block_fonts": True,
    },
    {
        "id": "perplexity-startups",
        "name": "Perplexity AI",
        "url": "https://www.perplexity.ai/startups",
        "wait": 3,
        "banner_selector": "[id*='consent'], [id*='cookie']",
    },
    {
        "id": "posthog-startups",
        "name": "PostHog",
        "url": "https://posthog.com/startups",
        "wait": 3,
        "banner_selector": "[id*='consent'], [id*='cookie'], [class*='banner']",
    },
    {
        "id": "supabase-startups",
        "name": "Supabase",
        "url": "https://supabase.com/solutions/startups",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, [id*='consent'], [id*='cookie']",
    },
    {
        "id": "stripe-startups",
        "name": "Stripe",
        "url": "https://stripe.com/startups",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, [id*='consent'], [id*='cookie']",
    },
    {
        "id": "deepinfra-startups",
        "name": "DeepInfra",
        "url": "https://deepinfra.com/deepstart",
        "wait": 3,
        "banner_selector": "[id*='consent'], [id*='cookie']",
    },
    {
        "id": "runpod-startups",
        "name": "RunPod",
        "url": "https://www.runpod.io/startup-program",
        "wait": 3,
        "banner_selector": "[id*='consent'], [id*='cookie']",
    },
    {
        "id": "cerebras",
        "name": "Cerebras Cloud",
        "url": "https://www.cerebras.ai/",
        "wait": 3,
        "banner_selector": "#onetrust-consent-sdk, [id*='consent'], [id*='cookie']",
    },
]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-setuid-sandbox",
            ]
        )
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            locale="en-US",
        )
        page = context.new_page()
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

        for item in TARGETS:
            out_file = os.path.join(OUTPUT_DIR, f"{item['id']}.png")
            print(f"[{item['name']}] Capturing hero from {item['url']}...")

            if item.get("block_fonts"):
                page.route("**/*.woff*", lambda route: route.abort())
            else:
                try:
                    page.unroute("**/*.woff*")
                except Exception:
                    pass

            try:
                page.goto(item["url"], wait_until="domcontentloaded", timeout=25000)
                time.sleep(item.get("wait", 3))

                # Clean up cookie banners and modal overlays
                page.evaluate("""() => {
                    const sel = [
                        '#onetrust-consent-sdk',
                        '#cookie-banner',
                        '.cookie-banner',
                        '#awsccc-cb-modal',
                        '#awsccc-cs-modal',
                        '.m-nav-cookie',
                        '.wcpConsentBannerCtrl',
                        'devsite-consent',
                        '.glue-cookie-notification-bar',
                        '#tarteaucitronRoot',
                        '[id*="consent"]',
                        '[class*="consent"]',
                        '[id*="cookie-banner"]',
                        '[class*="cookie-banner"]'
                    ];
                    sel.forEach(s => {
                        try {
                            document.querySelectorAll(s).forEach(el => {
                                el.style.display = 'none';
                                el.remove();
                            });
                        } catch(e) {}
                    });
                    // Also unlock any body scrolling lock
                    document.body.style.overflow = 'auto';
                    document.documentElement.style.overflow = 'auto';
                }""")
                time.sleep(0.5)

                # Capture top hero region (1440 x 820)
                page.screenshot(
                    path=out_file,
                    clip={"x": 0, "y": 0, "width": 1440, "height": 820},
                    animations="disabled"
                )
                print(f"  -> Successfully saved hero to {out_file} (Page Title: {page.title()})")
            except Exception as e:
                print(f"  -> ERROR capturing {item['name']}: {e}")

        browser.close()

if __name__ == "__main__":
    main()
