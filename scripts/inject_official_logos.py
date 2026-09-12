import json
import re

with open("data/official_svg_logos.json", "r", encoding="utf-8") as f:
    official_logos = json.load(f)

# 1. Update data/startup_credits_dataset.json
with open("data/startup_credits_dataset.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

for c in companies:
    cid = c["id"]
    if cid in official_logos:
        c["logoSvg"] = official_logos[cid]
    else:
        for k, v in official_logos.items():
            if cid in k or k in cid:
                c["logoSvg"] = v
                break

with open("data/startup_credits_dataset.json", "w", encoding="utf-8") as f:
    json.dump(companies, f, indent=2)

print("Updated data/startup_credits_dataset.json with official SVG logos!")

# 2. Update build_dashboard.py SVG_LOGOS dictionary
with open("build_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace SVG_LOGOS block in build_dashboard.py
svg_items_code = "SVG_LOGOS = {\n"
for k, svg in official_logos.items():
    svg_items_code += f'    "{k}": """{svg}""",\n'
svg_items_code += "}\n"

new_code = re.sub(r'SVG_LOGOS\s*=\s*\{.*?\}\n', svg_items_code, code, flags=re.DOTALL)

with open("build_dashboard.py", "w", encoding="utf-8") as f:
    f.write(new_code)

print("Updated build_dashboard.py with official SVG_LOGOS!")
