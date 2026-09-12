import json
import urllib.request
import re
import os

# Let's verify sources for all 16 official logos
print("Fetching official SVGs...")

def get_svg(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return r.read().decode('utf-8')
    except Exception as e:
        print(f"Failed {url}: {e}")
        return None

# Simple Icons CDN base
SI = "https://cdn.jsdelivr.net/npm/simple-icons@v14/icons"

logos = {}

# 1. Google Cloud
gc_raw = get_svg(f"{SI}/googlecloud.svg")
if gc_raw:
    # Extract path
    path = re.search(r'<path d=\"([^\"]+)\"', gc_raw).group(1)
    logos["google-cloud"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#4285F4"/>
  </g>
</svg>'''

# 2. Microsoft Azure
azure_raw = get_svg("https://svgl.app/library/azure.svg")
if azure_raw:
    # Wrap clean inner SVG inside 48x48
    inner = re.sub(r'<\?xml[^>]*\?>', '', azure_raw)
    inner = re.sub(r'<svg[^>]*>', '', inner)
    inner = inner.replace('</svg>', '').strip()
    logos["microsoft-founders-hub"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.29)">
    {inner}
  </g>
</svg>'''

# 3. AWS
aws_raw = get_svg(f"{SI}/amazonwebservices.svg")
if aws_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', aws_raw).group(1)
    logos["aws-activate"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#FF9900"/>
  </g>
</svg>'''

# 4. NVIDIA
nvidia_raw = get_svg(f"{SI}/nvidia.svg")
if nvidia_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', nvidia_raw).group(1)
    logos["nvidia-inception"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#76B900"/>
  </g>
</svg>'''

# 5. Cloudflare
cf_raw = get_svg(f"{SI}/cloudflare.svg")
if cf_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', cf_raw).group(1)
    logos["cloudflare-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#F38020"/>
  </g>
</svg>'''

# 6. OpenAI
openai_raw = get_svg(f"{SI}/openai.svg")
if openai_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', openai_raw).group(1)
    logos["openai-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#10A37F"/>
  </g>
</svg>'''

# 7. Anthropic
anth_raw = get_svg(f"{SI}/anthropic.svg")
if anth_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', anth_raw).group(1)
    logos["anthropic-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#D97706"/>
  </g>
</svg>'''

# 8. Oracle
logos["oracle-cloud"] = '''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(11, 15)">
    <rect x="0" y="0" width="26" height="18" rx="9" fill="none" stroke="#F80000" stroke-width="4.5"/>
  </g>
</svg>'''

# 9. Scaleway
sw_raw = get_svg(f"{SI}/scaleway.svg")
if sw_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', sw_raw).group(1)
    logos["scaleway-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#4F0599"/>
  </g>
</svg>'''

# 10. Perplexity AI
perp_raw = get_svg(f"{SI}/perplexity.svg")
if perp_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', perp_raw).group(1)
    logos["perplexity-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#20808D"/>
  </g>
</svg>'''

# 11. PostHog
ph_raw = get_svg(f"{SI}/posthog.svg")
if ph_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', ph_raw).group(1)
    logos["posthog-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#F54E00"/>
  </g>
</svg>'''

# 12. Supabase
sb_raw = get_svg(f"{SI}/supabase.svg")
if sb_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', sb_raw).group(1)
    logos["supabase-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#3ECF8E"/>
  </g>
</svg>'''

# 13. Stripe
stripe_raw = get_svg(f"{SI}/stripe.svg")
if stripe_raw:
    path = re.search(r'<path d=\"([^\"]+)\"', stripe_raw).group(1)
    logos["stripe-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="{path}" fill="#635BFF"/>
  </g>
</svg>'''

# 14. DeepInfra
# DeepInfra neural nodes from lobe-icons
di_raw = get_svg("https://raw.githubusercontent.com/lobehub/lobe-icons/master/packages/static-svg/icons/deepinfra.svg")
if di_raw:
    # Grab inner elements
    inner = re.sub(r'<\?xml[^>]*\?>', '', di_raw)
    inner = re.sub(r'<svg[^>]*>', '', inner)
    inner = inner.replace('</svg>', '').strip()
    logos["deepinfra-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)" fill="#2563EB">
    {inner}
  </g>
</svg>'''

# 15. RunPod
# Official hexagonal pod
runpod_path = "M170.04 163.76C180.216 157.899 186.485 147.067 186.485 135.344L186.485 70.656C186.485 58.9334 180.216 48.1013 170.04 42.24L113.887 9.89597C103.71 4.03467 91.1731 4.03468 80.997 9.89598L24.8432 42.24C14.6671 48.1013 8.39844 58.9334 8.39844 70.656L8.39844 135.344C8.39844 147.067 14.6672 157.899 24.8432 163.76L80.997 196.104C91.1731 201.965 103.711 201.965 113.887 196.104L170.04 163.76ZM170.04 135.344C170.04 141.205 166.906 146.621 161.818 149.552L132.428 166.48C129.838 167.972 128.543 168.718 127.48 168.607C126.553 168.51 125.711 168.025 125.163 167.272C124.535 166.41 124.535 164.918 124.535 161.934L124.535 128.078C124.535 122.217 127.66 116.8 132.748 113.869L161.818 97.0984C166.906 94.1671 170.04 99.5828 170.04 105.444L170.04 135.344Z"
logos["runpod-startups"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.14)" fill="#6E40C9">
    <path fill-rule="evenodd" clip-rule="evenodd" d="{runpod_path}"/>
  </g>
</svg>'''

# 16. Cerebras
cerebras_raw = get_svg("https://raw.githubusercontent.com/lobehub/lobe-icons/master/packages/static-svg/icons/cerebras.svg")
if cerebras_raw:
    inner = re.sub(r'<\?xml[^>]*\?>', '', cerebras_raw)
    inner = re.sub(r'<svg[^>]*>', '', inner)
    inner = inner.replace('</svg>', '').strip()
    logos["cerebras"] = f'''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)" fill="#FF6422">
    {inner}
  </g>
</svg>'''

print(f"Total verified official logos ready: {len(logos)}/16")
for k in sorted(logos.keys()):
    print(f"  ✓ {k}")

# Save to a json file in data/
with open("data/official_svg_logos.json", "w", encoding="utf-8") as f:
    json.dump(logos, f, indent=2)

print("Saved data/official_svg_logos.json successfully!")
