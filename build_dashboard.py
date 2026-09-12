import json
import os

with open("data/startup_credits_dataset.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

# Crisp SVG vector logos for each company
SVG_LOGOS = {
    "google-cloud": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <path d="M29.5 19.5L25 15L20.5 19.5L16 15L25 6L34 15L29.5 19.5Z" fill="#EA4335"/>
  <path d="M38.5 28.5L34 24L38.5 19.5L43 24L34 33L38.5 28.5Z" fill="#4285F4"/>
  <path d="M19.5 38.5L15 34L19.5 29.5L15 25L6 34L15 43L19.5 38.5Z" fill="#FBBC05"/>
  <path d="M28.5 38.5L33 34L28.5 29.5L33 25L42 34L33 43L28.5 38.5Z" fill="#34A853"/>
  <path d="M19.5 19.5H28.5V28.5H19.5V19.5Z" fill="#4285F4"/>
  <circle cx="24" cy="24" r="5.5" fill="#1A73E8"/>
</svg>""",
    "microsoft-founders-hub": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <rect x="8" y="8" width="14" height="14" rx="2" fill="#F25022"/>
  <rect x="26" y="8" width="14" height="14" rx="2" fill="#7FBA00"/>
  <rect x="8" y="26" width="14" height="14" rx="2" fill="#00A4EF"/>
  <rect x="26" y="26" width="14" height="14" rx="2" fill="#FFB900"/>
</svg>""",
    "aws-activate": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#1A2433"/>
  <path d="M14 22L19 14H24L17 26H12L14 22Z" fill="#FF9900"/>
  <path d="M22 26L28 14H33L25 26H22Z" fill="#FFFFFF"/>
  <path d="M10 32C18 37 30 37 38 31" stroke="#FF9900" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M38 31L35 34M38 31L34 29" stroke="#FF9900" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",
    "nvidia-inception": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#0E1210"/>
  <path d="M10 24C10 16.268 16.268 10 24 10C29.8 10 34.7 13.5 36.7 18.5C35.2 16.8 31.8 14.8 27.5 14.8C20.6 14.8 15 20.4 15 27.3C15 31.6 17.5 34.8 20.8 36.3C14.5 34.5 10 29.8 10 24Z" fill="#76B900"/>
  <path d="M24 18C20.7 18 18 20.7 18 24C18 27.3 20.7 30 24 30C26.5 30 28.7 28.4 29.5 26.2C28.8 26.7 27.5 27 26.2 27C24.5 27 23.1 25.6 23.1 23.9C23.1 22.2 24.5 20.8 26.2 20.8C27.5 20.8 28.8 21.1 29.5 21.6C28.7 19.4 26.5 18 24 18Z" fill="#76B900"/>
</svg>""",
    "cloudflare-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#1C1814"/>
  <path d="M30.8 19.2C30.2 14.7 26.4 11.2 21.7 11.2C17.6 11.2 14.1 14 13 17.8C10.2 18.5 8 21 8 24.1C8 27.6 10.9 30.5 14.4 30.5H30.5C33.5 30.5 36 28 36 25C36 22.2 33.7 19.8 30.8 19.2Z" fill="#F38020"/>
  <path d="M30.5 30.5H35.2C37.8 30.5 40 28.3 40 25.7C40 23.3 38.3 21.4 36 21C35.8 19.2 34.5 17.7 32.8 17.2C33.6 19.2 33.2 21.6 31.8 23.2C30.5 24.6 28.6 25.4 26.6 25.4H24.5L23 30.5H30.5Z" fill="#FAAD3F"/>
</svg>""",
    "openai-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#0A1813"/>
  <path d="M36.4 22.8C36.1 21.4 35.3 20.1 34.1 19.3C34.3 17.8 33.9 16.2 32.9 15C31.5 13.3 29.3 12.5 27.2 13C26.5 11.8 25.3 10.9 23.9 10.5C21.7 9.8 19.4 10.5 18 12.1C16.5 12.4 15.2 13.3 14.4 14.6C13.2 16.6 13.3 19.1 14.4 21C13.8 22.3 13.8 23.9 14.3 25.2C15 27.2 16.7 28.5 18.8 28.8C19.3 30.2 20.4 31.2 21.8 31.7C24.1 32.5 26.6 31.8 28.1 30.1C29.6 29.8 30.8 28.9 31.6 27.6C32.8 25.6 32.7 23.1 31.6 21.2C32.2 19.9 32.2 18.3 31.7 17M24 16L29 19V25L24 28L19 25V19L24 16Z" stroke="#10A37F" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",
    "anthropic-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#1C1814"/>
  <path d="M19 12L10 34H16L18 29H26L28 34H34L25 12H19ZM20 24L22 18L24 24H20Z" fill="#D97706"/>
  <path d="M31 12L37 34H32L30.5 28.5L34 16L31 12Z" fill="#CC785C"/>
</svg>""",
    "oracle-cloud": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#1E0D0B"/>
  <rect x="8" y="16" width="32" height="16" rx="8" stroke="#C74634" stroke-width="4"/>
</svg>""",
    "scaleway-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#150B20"/>
  <path d="M14 14H22V22H14V14Z" fill="#4F0599"/>
  <path d="M26 14H34V22H26V14Z" fill="#7A1CDE"/>
  <path d="M14 26H22V34H14V26Z" fill="#9B4BFF"/>
  <path d="M26 26H34V34H26V26Z" fill="#C59BFF"/>
</svg>""",
    "perplexity-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#0C1B1B"/>
  <path d="M24 10V38M14 16L34 32M34 16L14 32M10 24H38" stroke="#20B2AA" stroke-width="3" stroke-linecap="round"/>
  <circle cx="24" cy="24" r="5" fill="#0C1B1B" stroke="#20B2AA" stroke-width="2.5"/>
</svg>""",
    "posthog-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#20110A"/>
  <path d="M11 28C11 20 17 14 25 14C33 14 38 19 38 27C38 31 35 34 31 34H17C13.7 34 11 31.3 11 28Z" fill="#F54E00"/>
  <circle cx="31" cy="23" r="2.5" fill="#FFFFFF"/>
  <circle cx="23" cy="23" r="2" fill="#FFFFFF"/>
  <path d="M11 28L8 25M15 18L13 14M22 14L22 10M29 15L32 12" stroke="#FFD02F" stroke-width="2.5" stroke-linecap="round"/>
</svg>""",
    "supabase-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#0D1E17"/>
  <path d="M25 10L13 26H23L21 38L35 20H24L25 10Z" fill="#3ECF8E"/>
</svg>""",
    "stripe-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#12102A"/>
  <path d="M28.5 19.5C28.5 17.5 26.8 16.5 24 16.5C20.5 16.5 17.5 18 17.5 18L16 13.5C16 13.5 19.8 12 24.2 12C30 12 34 15 34 20C34 26.5 25.5 25.5 25.5 29C25.5 30.5 27 31.5 29.5 31.5C33 31.5 36.2 30 36.2 30L37.5 34.5C37.5 34.5 34 36 29.2 36C23 36 20 33 20 28C20 21.2 28.5 22.5 28.5 19.5Z" fill="#635BFF"/>
</svg>""",
    "deepinfra-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#160E26"/>
  <circle cx="16" cy="16" r="4" fill="#8B5CF6"/>
  <circle cx="32" cy="16" r="4" fill="#8B5CF6"/>
  <circle cx="24" cy="32" r="5" fill="#A78BFA"/>
  <path d="M16 16L24 32M32 16L24 32M16 16H32" stroke="#8B5CF6" stroke-width="2.5"/>
</svg>""",
    "runpod-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" fill="#150E28"/>
  <rect x="12" y="14" width="24" height="20" rx="4" stroke="#8B5CF6" stroke-width="2.5"/>
  <circle cx="18" cy="24" r="2.5" fill="#C4B5FD"/>
  <circle cx="24" cy="24" r="2.5" fill="#A78BFA"/>
  <circle cx="30" cy="24" r="2.5" fill="#8B5CF6"/>
  <path d="M18 34V37M30 34V37M12 20H36" stroke="#8B5CF6" stroke-width="2"/>
</svg>"""
}

for c in companies:
    c["logoSvg"] = SVG_LOGOS.get(c["id"], SVG_LOGOS["google-cloud"])

companies_json_str = json.dumps(companies).replace("</script>", "<\\/script>")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>AI Startup Stack — Startup Credits & GPU Treasury</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600&family=Parkinsans:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       MINIMAL EDITORIAL TOKENS & TYPOGRAPHY SYSTEM
       Strict 3-Font Hierarchy (No Default System Fonts):
       1. Parkinsans: Display, Brand & Numbers
       2. Plus Jakarta Sans: Interface, UI Controls & Body Copy
       3. Geist Mono: Citations, Codes, URLs & Technical Metadata
       ========================================================================== */
    :root {{
      --font-display: 'Parkinsans', sans-serif;
      --font-ui: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'Geist Mono', monospace;

      /* Calm Light Paper Palette */
      --bg-page: #F7F7F8;
      --bg-shell: #FFFFFF;
      --bg-card: #FFFFFF;
      --bg-card-hover: #FBFBFC;
      --bg-card-active: #F8F9FA;
      --bg-subtle: #F8F9FA;
      --bg-tag: #F1F3F5;
      --bg-pill: #F3F4F6;
      --bg-logo: #F8FAFC;

      /* Borders */
      --border-subtle: #EBECEF;
      --border-hover: #CBD5E1;
      --border-active: #0F172A;
      --border-card: #EBECEF;

      /* Typography Ink */
      --text-primary: #0F172A;
      --text-secondary: #475569;
      --text-muted: #64748B;
      --text-faint: #94A3B8;
      --text-reading: #2D3748;

      /* Accents */
      --accent-green: #059669;
      --accent-green-subtle: #F0FDF4;
      --accent-green-text: #065F46;
      --accent-green-pill: #DCFCE7;
      --accent-blue: #2563EB;
      --accent-red: #E11D48;
      --accent-red-subtle: #FFF1F2;
      --accent-red-text: #9F1239;

      /* Elevation */
      --shadow-subtle: 0 1px 2px rgba(0, 0, 0, 0.04);
      --shadow-card-hover: 0 6px 16px -2px rgba(0, 0, 0, 0.05);
      --shadow-card-active: 0 0 0 1.5px var(--border-active), 0 4px 14px rgba(0, 0, 0, 0.06);
      --shadow-shell: 0 12px 36px -8px rgba(15, 23, 42, 0.05), 0 0 0 1px rgba(15, 23, 42, 0.03);
      --shadow-shell-mobile: 0 20px 40px -10px rgba(15, 23, 42, 0.15), 0 0 0 8px #E2E8F0;

      --radius-tile: 16px;
      --radius-panel: 20px;
    }}

    /* Dark Mode Palette */
    [data-theme="dark"] {{
      --bg-page: #0B0D0F;
      --bg-shell: #121519;
      --bg-card: #171B21;
      --bg-card-hover: #1D222A;
      --bg-card-active: #212730;
      --bg-subtle: #171B21;
      --bg-tag: #1F242C;
      --bg-pill: #1C2128;
      --bg-logo: #14171C;

      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.20);
      --border-active: #FFFFFF;
      --border-card: rgba(255, 255, 255, 0.08);

      --text-primary: #F8FAFC;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      --text-faint: #475569;
      --text-reading: #CBD5E1;

      --accent-green: #10B981;
      --accent-green-subtle: rgba(16, 185, 129, 0.12);
      --accent-green-text: #6EE7B7;
      --accent-green-pill: rgba(52, 211, 153, 0.15);
      --accent-blue: #3B82F6;
      --accent-red: #F43F5E;
      --accent-red-subtle: rgba(244, 63, 94, 0.12);
      --accent-red-text: #FDA4AF;

      --shadow-subtle: none;
      --shadow-card-hover: 0 8px 24px rgba(0, 0, 0, 0.5);
      --shadow-card-active: 0 0 0 1.5px #FFFFFF, 0 8px 24px rgba(0, 0, 0, 0.6);
      --shadow-shell: 0 24px 60px -12px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.05);
      --shadow-shell-mobile: 0 25px 60px -15px rgba(0, 0, 0, 0.95), 0 0 0 8px #1A1F26;
    }}

    [data-theme="dark"] .logo-backdrop {{
      fill: #1A1F26 !important;
      stroke: rgba(255, 255, 255, 0.12) !important;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background-color: var(--bg-page);
      color: var(--text-primary);
      font-family: var(--font-ui);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding: 24px 16px 40px 16px;
      transition: background-color 0.2s ease, color 0.2s ease;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* Top Control Bar */
    .top-bar {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      width: 100%;
      max-width: 980px;
      margin-bottom: 12px;
      padding: 0 4px;
      gap: 8px;
    }}

    .theme-pill {{
      display: inline-flex;
      align-items: center;
      background: var(--bg-shell);
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      padding: 3px 4px;
      box-shadow: var(--shadow-subtle);
    }}

    .theme-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-family: var(--font-ui);
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      padding: 4px 10px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}

    .theme-btn:hover {{
      color: var(--text-primary);
    }}

    .theme-btn.active {{
      background: var(--bg-subtle);
      color: var(--text-primary);
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }}

    .viewport-toggle {{
      background: var(--bg-shell);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-family: var(--font-ui);
      font-size: 11px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 999px;
      cursor: pointer;
      box-shadow: var(--shadow-subtle);
      transition: all 0.15s ease;
    }}

    .viewport-toggle:hover {{
      color: var(--text-primary);
      border-color: var(--border-hover);
    }}

    /* Master Clean Shell */
    .app-shell {{
      width: 100%;
      max-width: 980px;
      background-color: var(--bg-shell);
      border-radius: var(--radius-panel);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-shell);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
      transition: max-width 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, border-color 0.2s ease;
    }}

    .app-shell.mobile-mode {{
      max-width: 410px;
      border-radius: 32px;
      box-shadow: var(--shadow-shell-mobile);
    }}

    /* Minimalist Header */
    .app-header {{
      padding: 28px 32px 20px 32px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .header-title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .brand-logo-lockup {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-primary);
      user-select: none;
    }}

    .brand-logo-img {{
      height: 32px;
      width: auto;
      display: block;
      object-fit: contain;
    }}

    body.dark-mode .brand-logo-img.logo-light {{
      display: none;
    }}

    body.dark-mode .brand-logo-img.logo-dark {{
      display: block;
    }}

    body:not(.dark-mode) .brand-logo-img.logo-dark {{
      display: none;
    }}

    .brand-wordmark {{
      font-family: var(--font-display);
      font-size: 21px;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--text-primary);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      line-height: 1;
    }}

    .wordmark-ai {{
      color: var(--text-primary);
      font-weight: 800;
    }}

    .wordmark-name {{
      color: var(--text-primary);
      font-weight: 700;
    }}

    .brand-count {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 500;
      background: var(--bg-subtle);
      padding: 3px 8px;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
    }}

    .brand-subtitle {{
      font-family: var(--font-ui);
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 400;
      letter-spacing: -0.1px;
    }}

    /* Carousel Track Section */
    .carousel-section {{
      padding: 24px 32px 20px 32px;
      position: relative;
    }}

    .carousel-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .carousel-label {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-muted);
    }}

    .carousel-nav {{
      display: flex;
      gap: 6px;
    }}

    .nav-btn {{
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-size: 12px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}

    .nav-btn:hover {{
      background: var(--bg-card-hover);
      color: var(--text-primary);
      border-color: var(--border-hover);
    }}

    .carousel-track {{
      display: flex;
      gap: 14px;
      overflow-x: auto;
      scroll-behavior: smooth;
      padding: 4px 2px 10px 2px;
      scrollbar-width: none;
    }}

    .carousel-track::-webkit-scrollbar {{
      display: none;
    }}

    /* Strict Square Tile (196x196px, 1:1 ratio) */
    .square-tile {{
      width: 196px;
      min-width: 196px;
      height: 196px;
      aspect-ratio: 1 / 1;
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: var(--radius-tile);
      padding: 18px 16px 16px 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      cursor: pointer;
      box-shadow: var(--shadow-subtle);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
      position: relative;
    }}

    .square-tile:hover {{
      background: var(--bg-card-hover);
      border-color: var(--border-hover);
      transform: translateY(-2px);
      box-shadow: var(--shadow-card-hover);
    }}

    .square-tile.active {{
      background: var(--bg-card-active);
      border-color: var(--border-active);
      box-shadow: var(--shadow-card-active);
    }}

    .tile-logo-box {{
      width: 46px;
      height: 46px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 4px;
      transition: transform 0.2s ease;
    }}

    .square-tile:hover .tile-logo-box {{
      transform: scale(1.05);
    }}

    .tile-name {{
      font-family: var(--font-ui);
      font-size: 14.5px;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.25;
      letter-spacing: -0.2px;
      margin-top: 4px;
    }}

    .tile-bottom {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      width: 100%;
    }}

    .tile-amount {{
      font-family: var(--font-display);
      font-size: 16.5px;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.4px;
      font-variant-numeric: tabular-nums;
    }}

    .tile-dq-pill {{
      font-family: var(--font-mono);
      font-size: 9.5px;
      font-weight: 600;
      color: #991B1B;
      background: rgba(239, 68, 68, 0.08);
      border: 1px solid rgba(239, 68, 68, 0.2);
      padding: 2px 7px;
      border-radius: 999px;
      display: inline-block;
      line-height: 1.3;
      white-space: nowrap;
      max-width: 170px;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    body.dark-mode .tile-dq-pill {{
      color: #FCA5A5;
      background: rgba(239, 68, 68, 0.15);
      border-color: rgba(239, 68, 68, 0.3);
    }}

    /* Reading & Program Detail View */
    .detail-view {{
      padding: 28px 32px 36px 32px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      animation: fadeIn 0.2s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .detail-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .detail-identity {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .detail-logo {{
      width: 50px;
      height: 50px;
      border-radius: 12px;
      padding: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .audit-tag {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 600;
      color: var(--text-muted);
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-subtle);
      padding: 2px 8px;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .audit-tag.verified {{
      color: var(--accent-green);
      background: rgba(5, 150, 105, 0.08);
      border-color: rgba(5, 150, 105, 0.2);
    }}

    .audit-dot {{
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--accent-green);
    }}

    .detail-titles h2 {{
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.3px;
    }}

    .detail-titles p {{
      font-family: var(--font-ui);
      font-size: 12.5px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .detail-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-apply {{
      background: var(--text-primary);
      color: var(--bg-shell);
      font-family: var(--font-ui);
      font-size: 12.5px;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: 999px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: opacity 0.15s ease;
    }}

    .btn-apply:hover {{
      opacity: 0.88;
    }}

    .btn-copy {{
      background: none;
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-family: var(--font-ui);
      font-size: 12px;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .btn-copy:hover {{
      color: var(--text-primary);
      border-color: var(--border-hover);
    }}

    /* Minimal Key Facts Strip (3 quiet metrics) */
    .facts-strip {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      padding: 18px 0;
      border-bottom: 1px solid var(--border-subtle);
    }}

    @media (max-width: 600px) {{
      .facts-strip {{
        grid-template-columns: 1fr;
        gap: 12px;
      }}
    }}

    .fact-box {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .fact-label {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .fact-val {{
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.4px;
      font-variant-numeric: tabular-nums;
    }}

    .fact-sub {{
      font-family: var(--font-ui);
      font-size: 11.5px;
      color: var(--text-muted);
    }}

    /* 3-Tab Segmented Control */
    .tab-strip {{
      display: flex;
      gap: 6px;
      padding: 16px 0;
      border-bottom: 1px solid var(--border-subtle);
      overflow-x: auto;
      scrollbar-width: none;
    }}
    .tab-strip::-webkit-scrollbar {{
      display: none;
    }}

    @media (max-width: 640px) {{
      body {{
        padding: 12px 8px 32px 8px;
      }}
      .app-header {{
        padding: 20px 16px 16px 16px;
      }}
      .carousel-section {{
        padding: 18px 16px 16px 16px;
      }}
      .detail-view {{
        padding: 20px 16px 28px 16px;
      }}
      .viewport-toggle {{
        display: none;
      }}
      .detail-header {{
        flex-direction: column;
        align-items: flex-start;
        gap: 14px;
      }}
      .detail-actions {{
        width: 100%;
        justify-content: flex-start;
      }}
    }}

    .tab-item {{
      background: none;
      border: none;
      font-family: var(--font-ui);
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
      cursor: pointer;
      padding: 6px 14px;
      border-radius: 8px;
      transition: all 0.15s ease;
    }}

    .tab-item:hover {{
      color: var(--text-primary);
      background: var(--bg-subtle);
    }}

    .tab-item.active {{
      color: var(--text-primary);
      background: var(--bg-subtle);
      font-weight: 600;
    }}

    /* Tab Content Area */
    .tab-body {{
      padding-top: 22px;
      min-height: 280px;
    }}

    /* Tab 1: Deep Research Essay */
    .essay-view {{
      max-width: 820px;
    }}

    .essay-text {{
      font-family: var(--font-ui);
      font-size: 15px;
      line-height: 1.7;
      color: var(--text-reading);
    }}

    .essay-text p {{
      margin-bottom: 20px;
    }}

    .services-block {{
      margin-top: 24px;
      padding-top: 18px;
      border-top: 1px solid var(--border-subtle);
    }}

    .product-breakdown-section {{
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .breakdown-title {{
      font-family: var(--font-ui);
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .product-item-card {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: border-color 0.15s ease;
    }}

    .product-item-card:hover {{
      border-color: var(--border-hover);
    }}

    .product-item-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .product-name {{
      font-family: var(--font-ui);
      font-size: 14px;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .product-role {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 500;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .product-what {{
      font-family: var(--font-ui);
      font-size: 12.5px;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    .product-why {{
      font-family: var(--font-ui);
      font-size: 12.5px;
      color: var(--text-primary);
      line-height: 1.5;
    }}

    .perks-section {{
      margin-top: 22px;
      background: rgba(5, 150, 105, 0.04);
      border: 1px solid rgba(5, 150, 105, 0.2);
      border-radius: 10px;
      padding: 14px 18px;
    }}

    .perks-title {{
      font-family: var(--font-ui);
      font-size: 13.5px;
      font-weight: 700;
      color: var(--accent-green);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .perks-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .perk-bullet {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-family: var(--font-ui);
      font-size: 12.5px;
      color: var(--text-primary);
      line-height: 1.5;
    }}

    .perk-icon {{
      color: var(--accent-green);
      font-size: 12px;
      line-height: 1.5;
    }}

    .finops-warning-box {{
      margin-top: 18px;
      background: rgba(239, 68, 68, 0.04);
      border: 1px solid rgba(239, 68, 68, 0.2);
      border-radius: 10px;
      padding: 14px 18px;
      font-family: var(--font-ui);
      font-size: 12px;
      line-height: 1.55;
      color: var(--text-secondary);
    }}

    .finops-warning-box .warn-label {{
      font-weight: 700;
      color: #DC2626;
      display: block;
      margin-bottom: 4px;
      font-size: 12.5px;
    }}

    .model-inference-section {{
      margin-top: 22px;
      background: rgba(37, 99, 235, 0.03);
      border: 1px solid rgba(37, 99, 235, 0.18);
      border-radius: 10px;
      padding: 16px 18px;
    }}

    .model-section-title {{
      font-family: var(--font-ui);
      font-size: 13.5px;
      font-weight: 700;
      color: var(--accent-blue);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .model-group-label {{
      font-family: var(--font-mono);
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    .model-chips-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }}

    .model-chip {{
      font-family: var(--font-ui);
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-primary);
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 3px 9px;
      border-radius: 6px;
    }}

    .model-chip.open {{
      color: var(--text-secondary);
      background: rgba(0,0,0,0.03);
    }}

    body.dark-mode .model-chip.open {{
      background: rgba(255,255,255,0.05);
    }}

    .inference-note {{
      font-family: var(--font-ui);
      font-size: 12px;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 8px;
    }}

    .runway-fact-box {{
      margin-top: 10px;
      padding: 10px 14px;
      background: rgba(16, 185, 129, 0.08);
      border-left: 3px solid var(--accent-green);
      border-radius: 0 6px 6px 0;
      font-family: var(--font-ui);
      font-size: 12px;
      line-height: 1.55;
      color: var(--text-primary);
    }}

    .services-title {{
      font-family: var(--font-mono);
      font-size: 10.5px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--text-muted);
      margin-bottom: 10px;
    }}

    .services-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .service-tag {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-secondary);
      background: var(--bg-tag);
      border: 1px solid var(--border-subtle);
      padding: 3px 8px;
      border-radius: 6px;
    }}

    /* Real Portal Screenshot Browser Mockup */
    .portal-preview-card {{
      margin: 18px 0 22px 0;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: var(--shadow-subtle);
      transition: all 0.2s ease;
      max-width: 860px;
    }}

    .portal-preview-card:hover {{
      border-color: var(--border-hover);
      box-shadow: var(--shadow-card-hover);
    }}

    .portal-mockup-header {{
      padding: 8px 14px;
      background: var(--bg-shell);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }}

    .mockup-dots {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .mockup-dots span {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      display: inline-block;
    }}

    .mockup-dots .red {{ background: #EF4444; opacity: 0.8; }}
    .mockup-dots .yellow {{ background: #F59E0B; opacity: 0.8; }}
    .mockup-dots .green {{ background: #10B981; opacity: 0.8; }}

    .mockup-address {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--text-muted);
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 2px 10px;
      border-radius: 999px;
      max-width: 420px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .mockup-open-btn {{
      font-family: var(--font-ui);
      font-size: 11px;
      font-weight: 600;
      color: var(--accent-blue);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }}

    .mockup-viewport {{
      width: 100%;
      max-height: 380px;
      overflow: hidden;
      position: relative;
      background: #090A0C;
    }}

    .portal-screenshot-img {{
      width: 100%;
      height: auto;
      display: block;
      object-fit: cover;
      object-position: top;
      transition: transform 0.3s ease;
    }}

    .portal-preview-card:hover .portal-screenshot-img {{
      transform: scale(1.015);
    }}

    /* Tab 2: Requirements & Pitfalls */
    .checklist-group {{
      display: flex;
      flex-direction: column;
      gap: 24px;
      max-width: 840px;
    }}

    .section-heading {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .list-items {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .clean-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      font-size: 13px;
      line-height: 1.55;
      color: var(--text-secondary);
    }}

    .clean-item.danger {{
      background: var(--bg-card-subtle);
      border-color: var(--border-subtle);
      color: var(--text-secondary);
    }}

    .item-bullet {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 12px;
      line-height: 1.4;
      flex-shrink: 0;
    }}

    .item-bullet.green {{
      color: var(--accent-green);
    }}

    .item-bullet.red {{
      color: var(--text-muted);
    }}

    /* Tab 3: Application & Sources */
    .sources-view {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 840px;
    }}

    .source-card {{
      padding: 14px 16px;
      border-radius: 10px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .source-card.primary {{
      border-color: var(--border-active);
    }}

    .source-title {{
      font-family: var(--font-ui);
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-primary);
    }}

    .source-url {{
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--accent-blue);
      text-decoration: none;
      word-break: break-all;
    }}

    .source-url:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <!-- Minimal Top Bar -->
  <div class="top-bar">
    <div class="theme-pill">
      <button class="theme-btn active" id="btn-theme-light" onclick="setTheme('light')">☀️ Light</button>
      <button class="theme-btn" id="btn-theme-dark" onclick="setTheme('dark')">🌙 Dark</button>
    </div>
    <button class="viewport-toggle" id="btn-viewport" onclick="toggleViewport()">Mobile Mode</button>
  </div>

  <!-- Master Clean Shell -->
  <div class="app-shell" id="app-shell">

    <!-- Minimal Header -->
    <div class="app-header">
      <div class="header-title-row">
        <div class="brand-logo-lockup">
          <img src="assets/ai_stack_logo_mark.png" alt="AI Startup Stack" class="brand-logo-img logo-light" />
          <img src="assets/ai_stack_logo_mark_white.png" alt="AI Startup Stack" class="brand-logo-img logo-dark" />
          <div class="brand-wordmark">
            <span class="wordmark-ai">AI</span>
            <span class="wordmark-name">Startup Stack</span>
          </div>
        </div>
        <span class="brand-count">16 PROGRAMS</span>
      </div>
      <p class="brand-subtitle">The Pre-Flight Audited Cloud Compute, Foundation Model &amp; SaaS Treasury for AI Founders.</p>
    </div>

    <!-- Minimal Carousel -->
    <div class="carousel-section">
      <div class="carousel-top-bar">
        <span class="carousel-label">All Offerings</span>
        <div class="carousel-nav">
          <button class="nav-btn" onclick="scrollCarousel('left')" title="Scroll left">&#8592;</button>
          <button class="nav-btn" onclick="scrollCarousel('right')" title="Scroll right">&#8594;</button>
        </div>
      </div>

      <div class="carousel-track" id="carousel-track">
        <!-- Rendered via JavaScript -->
      </div>
    </div>

    <!-- Reading & Deep Research View -->
    <div class="detail-view" id="detail-view">
      <!-- Rendered via JavaScript -->
    </div>

  </div>

  <script>
    const COMPANIES_DATA = {companies_json_str};

    let selectedId = COMPANIES_DATA[0].id;
    let activeTab = 'essay';
    let currentTheme = 'light';
    let isMobileView = false;

    function setTheme(theme) {{
      currentTheme = theme;
      const html = document.documentElement;
      const btnLight = document.getElementById('btn-theme-light');
      const btnDark = document.getElementById('btn-theme-dark');

      if (theme === 'dark') {{
        html.setAttribute('data-theme', 'dark');
        btnDark.classList.add('active');
        btnLight.classList.remove('active');
      }} else {{
        html.removeAttribute('data-theme');
        btnLight.classList.add('active');
        btnDark.classList.remove('active');
      }}
    }}

    function toggleViewport() {{
      isMobileView = !isMobileView;
      const shell = document.getElementById('app-shell');
      const btn = document.getElementById('btn-viewport');

      if (isMobileView) {{
        shell.classList.add('mobile-mode');
        btn.textContent = 'Desktop Mode';
      }} else {{
        shell.classList.remove('mobile-mode');
        btn.textContent = 'Mobile Mode';
      }}
    }}

    function scrollCarousel(dir) {{
      const track = document.getElementById('carousel-track');
      const offset = dir === 'left' ? -220 : 220;
      track.scrollBy({{ left: offset, behavior: 'smooth' }});
    }}

    function selectCompany(id) {{
      selectedId = id;
      renderCarousel();
      renderDetail();
    }}

    function setTab(tab) {{
      activeTab = tab;
      renderDetail();
    }}

    function copyLink(url) {{
      navigator.clipboard.writeText(url);
      const btn = document.getElementById('btn-copy-url');
      if (btn) {{
        btn.textContent = 'Copied ✓';
        setTimeout(() => {{ btn.textContent = 'Copy Link'; }}, 2000);
      }}
    }}

    function renderCarousel() {{
      const track = document.getElementById('carousel-track');
      track.innerHTML = COMPANIES_DATA.map(c => {{
        const isSelected = c.id === selectedId;
        return `
          <div class="square-tile ${{isSelected ? 'active' : ''}}" onclick="selectCompany('${{c.id}}')">
            <div class="tile-logo-box">
              ${{c.logoSvg}}
            </div>
            <div class="tile-name">${{c.name}}</div>
            <div class="tile-bottom">
              <div class="tile-amount">${{c.maxCredits}}</div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function renderDetail() {{
      const container = document.getElementById('detail-view');
      const c = COMPANIES_DATA.find(item => item.id === selectedId) || COMPANIES_DATA[0];

      container.innerHTML = `
        <div class="detail-header">
          <div class="detail-identity">
            <div class="detail-logo">
              ${{c.logoSvg}}
            </div>
            <div class="detail-titles">
              <h2>${{c.name}}</h2>
              <p>${{c.programName}} &bull; ${{c.org}}</p>
            </div>
          </div>
          <div class="detail-actions">
            <button class="btn-copy" id="btn-copy-url" onclick="copyLink('${{c.applicationUrl}}')">Copy Link</button>
            <a href="${{c.applicationUrl}}" target="_blank" rel="noopener noreferrer" class="btn-apply">Apply &#8599;</a>
          </div>
        </div>

        <!-- 3 Minimal Key Facts -->
        <div class="facts-strip">
          <div class="fact-box">
            <span class="fact-label">Max Allocation</span>
            <span class="fact-val">${{c.maxCredits}}</span>
            <span class="fact-sub">${{c.equityTaken}}</span>
          </div>
          <div class="fact-box">
            <span class="fact-label">Primary Barrier</span>
            <span class="fact-val" style="font-size: 13.5px; font-weight: 600; line-height: 1.35; color: var(--text-primary);">${{c.topDisqualifier}}</span>
            <span class="fact-sub">Eligibility requirement</span>
          </div>
          <div class="fact-box">
            <span class="fact-label">Review Window</span>
            <span class="fact-val">${{c.turnaroundTime}}</span>
            <span class="fact-sub">Intake review turnaround</span>
          </div>
        </div>

        <!-- Real Official Portal Preview Mockup -->
        <div class="portal-preview-card">
          <div class="portal-mockup-header">
            <div class="mockup-dots">
              <span class="red"></span>
              <span class="yellow"></span>
              <span class="green"></span>
            </div>
            <div class="mockup-address">
              <span>&#128274;</span>
              <span>${{c.applicationUrl}}</span>
            </div>
            <a href="${{c.applicationUrl}}" target="_blank" rel="noopener noreferrer" class="mockup-open-btn">
              Visit Live Official Portal &#8599;
            </a>
          </div>
          <div class="mockup-viewport">
            <a href="${{c.applicationUrl}}" target="_blank" rel="noopener noreferrer" title="Click to open ${{c.name}} portal">
              <img src="${{c.portalScreenshot || ('assets/portals/' + c.id + '.png')}}" alt="${{c.name}} Official Portal Preview" class="portal-screenshot-img" onerror="this.parentElement.parentElement.parentElement.style.display='none'" />
            </a>
          </div>
        </div>

        <!-- 3-Tab Segmented Control -->
        <div class="tab-strip">
          <button class="tab-item ${{activeTab === 'essay' ? 'active' : ''}}" onclick="setTab('essay')">Program Breakdown</button>
          <button class="tab-item ${{activeTab === 'requirements' ? 'active' : ''}}" onclick="setTab('requirements')">Requirements & Watchpoints</button>
          <button class="tab-item ${{activeTab === 'sources' ? 'active' : ''}}" onclick="setTab('sources')">Official Portal & Citations</button>
        </div>

        <!-- Tab Body -->
        <div class="tab-body">
          ${{renderTabContent(c)}}
        </div>
      `;
    }}

    function renderTabContent(c) {{
      if (activeTab === 'essay') {{
        const summary = `
          <div style="background: var(--bg-card-subtle); border-left: 3px solid var(--accent-green); padding: 14px 18px; border-radius: 0 8px 8px 0; margin-bottom: 22px; font-family: var(--font-ui); font-style: italic; font-size: 14.5px; line-height: 1.6; color: var(--text-primary);">
            &ldquo;${{c.executiveSummary}}&rdquo;
          </div>
        `;

        const productCards = (c.productBreakdown || []).map(p => `
          <div class="product-item-card">
            <div class="product-item-header">
              <span class="product-name">${{p.product}}</span>
              <span class="product-role">${{p.role}}</span>
            </div>
            <div class="product-what"><strong>What it is:</strong> ${{p.whatItIs}}</div>
            <div class="product-why"><strong>Why it's helpful:</strong> ${{p.founderValue}}</div>
          </div>
        `).join('');

        const hiddenPerksList = (c.hiddenPerks || []).map(h => `
          <li class="perk-bullet">
            <span class="perk-icon">&#10022;</span>
            <span>${{h}}</span>
          </li>
        `).join('');

        const hiddenPerksSection = c.hiddenPerks && c.hiddenPerks.length > 0 ? `
          <div class="perks-section">
            <div class="perks-title">
              <span>&#9733;</span>
              <span>Included Perks Founders Often Miss</span>
            </div>
            <ul class="perks-list">
              ${{hiddenPerksList}}
            </ul>
          </div>
        ` : '';

        const finopsBox = c.finOpsWarning ? `
          <div class="finops-warning-box">
            <span class="warn-label">&#9888; FinOps Watch: What Credits Do NOT Cover</span>
            <div>${{c.finOpsWarning}}</div>
          </div>
        ` : '';

        const services = (c.eligibleServices || []).map(s => `<span class="service-tag">${{s}}</span>`).join('');

        const mi = c.modelInference;
        const modelInferenceSection = mi && (mi.proprietaryModels?.length > 0 || mi.openWeightModels?.length > 0 || mi.inferenceMechanics) ? `
          <div class="model-inference-section">
            <div class="model-section-title">
              <span>&#9889;</span>
              <span>Covered AI Models & Inference Mechanics</span>
            </div>
            
            ${{mi.proprietaryModels && mi.proprietaryModels.length > 0 ? `
              <div class="model-group-label">Flagship Hosted Models Covered:</div>
              <div class="model-chips-row">
                ${{mi.proprietaryModels.map(m => `<span class="model-chip">${{m}}</span>`).join('')}}
              </div>
            ` : ''}}

            ${{mi.openWeightModels && mi.openWeightModels.length > 0 ? `
              <div class="model-group-label">Open-Weights & Specialized Models Supported:</div>
              <div class="model-chips-row">
                ${{mi.openWeightModels.map(m => `<span class="model-chip open">${{m}}</span>`).join('')}}
              </div>
            ` : ''}}

            <div class="inference-note">
              <strong>Billing Mechanics:</strong> ${{mi.inferenceMechanics}}
            </div>

            ${{mi.tokenRunwayFact ? `
              <div class="runway-fact-box">
                <strong>Token Runway Fact:</strong> ${{mi.tokenRunwayFact}}
              </div>
            ` : ''}}
          </div>
        ` : '';

        return `
          <div class="essay-view">
            ${{summary}}

            <div class="product-breakdown-section">
              <div class="breakdown-title">
                <span>&#128736;</span>
                <span>What You Can Actually Build & Run With These Credits</span>
              </div>
              <p style="font-family: var(--font-ui); font-size: 12.5px; color: var(--text-secondary); margin-bottom: 8px;">
                Most founders only use a fraction of their credit allotment. Here is what this platform actually offers and how each product accelerates your runway:
              </p>
              ${{productCards}}
            </div>

            ${{modelInferenceSection}}
            ${{hiddenPerksSection}}
            ${{finopsBox}}

            <div style="margin-top: 20px; font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">
              Grounding Citations: ${{c.citations.map((cite, i) => `<a href="${{cite.url}}" target="_blank" rel="noopener noreferrer" style="color: var(--text-secondary); text-decoration: underline; margin-right: 14px;">[${{i+1}}] ${{cite.title}}</a>`).join('')}}
            </div>

            <div class="services-block">
              <div class="services-title">Eligible Infrastructure & Developer Stack:</div>
              <div class="services-tags">
                ${{services}}
              </div>
            </div>
          </div>
        `;
      }}

      if (activeTab === 'requirements') {{
        const topDqBanner = `
          <div style="background: var(--bg-card-subtle); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 14px 16px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px; flex-wrap: wrap; gap: 6px;">
              <span style="font-family: var(--font-mono); font-size: 10.5px; font-weight: 600; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px;">
                Primary Eligibility Watchpoint
              </span>
              <span style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted);">
                ${{c.disqualifierSource}}
              </span>
            </div>
            <div style="font-family: var(--font-ui); font-size: 13.5px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">
              ${{c.topDisqualifier}}
            </div>
            <div style="font-family: var(--font-ui); font-size: 12px; line-height: 1.5; color: var(--text-secondary);">
              ${{c.disqualifierDetail}}
            </div>
          </div>
        `;

        const reqs = c.requirements.map(r => `
          <div class="clean-item">
            <span class="item-bullet green">&#10003;</span>
            <div>${{r}}</div>
          </div>
        `).join('');

        const pitfalls = c.rejectionPitfalls.map(p => `
          <div class="clean-item danger">
            <span class="item-bullet red">&#10005;</span>
            <div>${{p}}</div>
          </div>
        `).join('');

        const factors = c.successFactors.map(f => `
          <div class="clean-item">
            <span class="item-bullet green">&#9733;</span>
            <div>${{f}}</div>
          </div>
        `).join('');

        return `
          <div class="checklist-group">
            ${{topDqBanner}}
            <div>
              <div class="section-heading">Eligibility Requirements</div>
              <div class="list-items">${{reqs}}</div>
            </div>
            <div>
              <div class="section-heading">Common Rejection Triggers</div>
              <div class="list-items">${{pitfalls}}</div>
            </div>
            <div>
              <div class="section-heading">How to Ensure Approval</div>
              <div class="list-items">${{factors}}</div>
            </div>
          </div>
        `;
      }}

      if (activeTab === 'sources') {{
        const portal = `
          <div class="source-card primary">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span class="source-title">Official Program Intake Portal</span>
            </div>
            <a href="${{c.applicationUrl}}" target="_blank" rel="noopener noreferrer" class="source-url" style="display: flex; align-items: center; justify-content: space-between;">
              <span>${{c.applicationUrl}}</span>
              <span style="font-weight: 700;">Apply Directly &#8599;</span>
            </a>
          </div>
        `;
        const cites = c.citations.map(cite => `
          <div class="source-card">
            <span class="source-title">${{cite.title}}</span>
            <a href="${{cite.url}}" target="_blank" rel="noopener noreferrer" class="source-url">${{cite.url}}</a>
          </div>
        `).join('');

        const provenance = c.interactionId ? `
          <div class="source-card" style="border-left: 3px solid #3B82F6; background: rgba(59, 130, 246, 0.04); margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span class="source-title" style="color: #2563EB;">Gemini Deep Research Audit Log</span>
              <span style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted);">${{c.researchStatus || 'VERIFIED'}}</span>
            </div>
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary); margin-bottom: 2px;">File: ${{c.sourceLogFile || 'Internal Research Archive'}}</div>
            <div style="font-family: var(--font-mono); font-size: 10.5px; color: var(--text-muted); word-break: break-all;">Interaction ID: ${{c.interactionId}}</div>
          </div>
        ` : '';

        return `
          <div class="sources-view">
            <div style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--text-muted); margin-bottom: 12px; letter-spacing: 0.5px;">Verified Grounding & Application Gateways (Audited: ${{c.researchAuditDate || c.auditDate || 'September 11, 2026'}}):</div>
            ${{provenance}}
            ${{portal}}
            ${{cites}}
          </div>
        `;
      }}

      return '';
    }}

    // Initial render
    renderCarousel();
    renderDetail();
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("AI_Startup_Stack.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated index.html and AI_Startup_Stack.html in C:/Users/shann/Desktop/AI_Startup_Stack!")
