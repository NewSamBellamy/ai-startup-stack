import json
import os

with open("data/startup_credits_dataset.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

# Crisp SVG vector logos for each company
SVG_LOGOS = {
    "google-cloud": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M12.19 2.38a9.344 9.344 0 0 0-9.234 6.893c.053-.02-.055.013 0 0-3.875 2.551-3.922 8.11-.247 10.941l.006-.007-.007.03a6.717 6.717 0 0 0 4.077 1.356h5.173l.03.03h5.192c6.687.053 9.376-8.605 3.835-12.35a9.365 9.365 0 0 0-2.821-4.552l-.043.043.006-.05A9.344 9.344 0 0 0 12.19 2.38zm-.358 4.146c1.244-.04 2.518.368 3.486 1.15a5.186 5.186 0 0 1 1.862 4.078v.518c3.53-.07 3.53 5.262 0 5.193h-5.193l-.008.009v-.04H6.785a2.59 2.59 0 0 1-1.067-.23h.001a2.597 2.597 0 1 1 3.437-3.437l3.013-3.012A6.747 6.747 0 0 0 8.11 8.24c.018-.01.04-.026.054-.023a5.186 5.186 0 0 1 3.67-1.69z" fill="#4285F4"/>
  </g>
</svg>""",
    "microsoft-founders-hub": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.29)">
    <defs>
    <linearGradient id="a" x1="-1032.17" x2="-1059.21" y1="145.31" y2="65.43" gradientTransform="matrix(1 0 0 -1 1075 158)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#114a8b"/>
      <stop offset="1" stop-color="#0669bc"/>
    </linearGradient>
    <linearGradient id="b" x1="-1023.73" x2="-1029.98" y1="108.08" y2="105.97" gradientTransform="matrix(1 0 0 -1 1075 158)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-opacity=".3"/>
      <stop offset=".07" stop-opacity=".2"/>
      <stop offset=".32" stop-opacity=".1"/>
      <stop offset=".62" stop-opacity=".05"/>
      <stop offset="1" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="c" x1="-1027.16" x2="-997.48" y1="147.64" y2="68.56" gradientTransform="matrix(1 0 0 -1 1075 158)" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3ccbf4"/>
      <stop offset="1" stop-color="#2892df"/>
    </linearGradient>
  </defs>
  <path fill="url(#a)" d="M33.34 6.54h26.04l-27.03 80.1a4.15 4.15 0 0 1-3.94 2.81H8.15a4.14 4.14 0 0 1-3.93-5.47L29.4 9.38a4.15 4.15 0 0 1 3.94-2.83z"/>
  <path fill="#0078d4" d="M71.17 60.26H29.88a1.91 1.91 0 0 0-1.3 3.31l26.53 24.76a4.17 4.17 0 0 0 2.85 1.13h23.38z"/>
  <path fill="url(#b)" d="M33.34 6.54a4.12 4.12 0 0 0-3.95 2.88L4.25 83.92a4.14 4.14 0 0 0 3.91 5.54h20.79a4.44 4.44 0 0 0 3.4-2.9l5.02-14.78 17.91 16.7a4.24 4.24 0 0 0 2.67.97h23.29L71.02 60.26H41.24L59.47 6.55z"/>
  <path fill="url(#c)" d="M66.6 9.36a4.14 4.14 0 0 0-3.93-2.82H33.65a4.15 4.15 0 0 1 3.93 2.82l25.18 74.62a4.15 4.15 0 0 1-3.93 5.48h29.02a4.15 4.15 0 0 0 3.93-5.48z"/>
  </g>
</svg>""",
    "aws-activate": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path class="aws-letters" d="M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.063.056.127.056.183 0 .08-.048.16-.152.24l-.503.335a.383.383 0 0 1-.208.072c-.08 0-.16-.04-.239-.112a2.47 2.47 0 0 1-.287-.375 6.18 6.18 0 0 1-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.28 0-.568.031-.863.103-.295.072-.583.16-.862.272a2.287 2.287 0 0 1-.28.104.488.488 0 0 1-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 0 1 .224-.167c.279-.144.614-.264 1.005-.36a4.84 4.84 0 0 1 1.246-.151c.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 0 0-.735-.136 6.02 6.02 0 0 0-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.295.846.191.2.47.296.838.296zm6.41.862c-.144 0-.24-.024-.304-.08-.064-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 0 1-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 0 1 .32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 0 1 .311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 0 1-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 0 1-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 0 1-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 0 0 .415-.758.777.777 0 0 0-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 0 1-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 0 1 .24.2.43.43 0 0 1 .071.263v.375c0 .168-.064.256-.184.256a.83.83 0 0 1-.303-.096 3.652 3.652 0 0 0-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.734.167-1.142.167zM21.698 16.207c-2.626 1.94-6.442 2.969-9.722 2.969-4.598 0-8.74-1.7-11.87-4.526-.247-.223-.024-.527.272-.351 3.384 1.963 7.559 3.153 11.877 3.153 2.914 0 6.114-.607 9.06-1.852.439-.2.814.287.383.607zM22.792 14.961c-.336-.43-2.22-.207-3.074-.103-.255.032-.295-.192-.063-.36 1.5-1.053 3.967-.75 4.254-.399.287.36-.08 2.826-1.485 4.007-.215.184-.423.088-.327-.151.32-.79 1.03-2.57.695-2.994z" fill="#FF9900"/>
  </g>
</svg>""",
    "nvidia-inception": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M8.948 8.798v-1.43a6.7 6.7 0 0 1 .424-.018c3.922-.124 6.493 3.374 6.493 3.374s-2.774 3.851-5.75 3.851c-.398 0-.787-.062-1.158-.185v-4.346c1.528.185 1.837.857 2.747 2.385l2.04-1.714s-1.492-1.952-4-1.952a6.016 6.016 0 0 0-.796.035m0-4.735v2.138l.424-.027c5.45-.185 9.01 4.47 9.01 4.47s-4.08 4.964-8.33 4.964c-.37 0-.733-.035-1.095-.097v1.325c.3.035.61.062.91.062 3.957 0 6.82-2.023 9.593-4.408.459.371 2.34 1.263 2.73 1.652-2.633 2.208-8.772 3.984-12.253 3.984-.335 0-.653-.018-.971-.053v1.864H24V4.063zm0 10.326v1.131c-3.657-.654-4.673-4.46-4.673-4.46s1.758-1.944 4.673-2.262v1.237H8.94c-1.528-.186-2.73 1.245-2.73 1.245s.68 2.412 2.739 3.11M2.456 10.9s2.164-3.197 6.5-3.533V6.201C4.153 6.59 0 10.653 0 10.653s2.35 6.802 8.948 7.42v-1.237c-4.84-.6-6.492-5.936-6.492-5.936z" fill="#76B900"/>
  </g>
</svg>""",
    "cloudflare-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M16.5088 16.8447c.1475-.5068.0908-.9707-.1553-1.3154-.2246-.3164-.6045-.499-1.0615-.5205l-8.6592-.1123a.1559.1559 0 0 1-.1333-.0713c-.0283-.042-.0351-.0986-.021-.1553.0278-.084.1123-.1484.2036-.1562l8.7359-.1123c1.0351-.0489 2.1601-.8868 2.5537-1.9136l.499-1.3013c.0215-.0561.0293-.1128.0147-.168-.5625-2.5463-2.835-4.4453-5.5499-4.4453-2.5039 0-4.6284 1.6177-5.3876 3.8614-.4927-.3658-1.1187-.5625-1.794-.499-1.2026.119-2.1665 1.083-2.2861 2.2856-.0283.31-.0069.6128.0635.894C1.5683 13.171 0 14.7754 0 16.752c0 .1748.0142.3515.0352.5273.0141.083.0844.1475.1689.1475h15.9814c.0909 0 .1758-.0645.2032-.1553l.12-.4268zm2.7568-5.5634c-.0771 0-.1611 0-.2383.0112-.0566 0-.1054.0415-.127.0976l-.3378 1.1744c-.1475.5068-.0918.9707.1543 1.3164.2256.3164.6055.498 1.0625.5195l1.8437.1133c.0557 0 .1055.0263.1329.0703.0283.043.0351.1074.0214.1562-.0283.084-.1132.1485-.204.1553l-1.921.1123c-1.041.0488-2.1582.8867-2.5527 1.914l-.1406.3585c-.0283.0713.0215.1416.0986.1416h6.5977c.0771 0 .1474-.0489.169-.126.1122-.4082.1757-.837.1757-1.2803 0-2.6025-2.125-4.727-4.7344-4.727" fill="#F38020"/>
  </g>
</svg>""",
    "openai-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z" fill="#10A37F"/>
  </g>
</svg>""",
    "anthropic-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z" fill="#D97706"/>
  </g>
</svg>""",
    "oracle-cloud": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(11, 15)">
    <rect x="0" y="0" width="26" height="18" rx="9" fill="none" stroke="#F80000" stroke-width="4.5"/>
  </g>
</svg>""",
    "scaleway-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M16.605 11.11v5.72a1.77 1.77 0 01-1.54 1.69h-4a1.43 1.43 0 01-1.31-1.22 1.09 1.09 0 010-.18 1.37 1.37 0 011.37-1.36h1.74a1 1 0 001-1v-3.62a1.4 1.4 0 011.18-1.39h.17a1.37 1.37 0 011.39 1.36zm-6.46 1.74V9.26a1 1 0 011-1h1.85a1.37 1.37 0 001.37-1.37 1 1 0 000-.17 1.45 1.45 0 00-1.41-1.2h-3.96a1.81 1.81 0 00-1.58 1.66v5.7a1.37 1.37 0 001.37 1.37h.21a1.4 1.4 0 001.15-1.4zm12-4.29V20a4.53 4.53 0 01-4.15 4h-7.58a8.57 8.57 0 01-8.56-8.57V4.54A4.54 4.54 0 016.395 0h7.18a8.56 8.56 0 018.56 8.56zm-2.74 0a5.83 5.83 0 00-5.82-5.82h-7.19a1.79 1.79 0 00-1.8 1.8v10.89a5.83 5.83 0 005.82 5.8h7.44a1.79 1.79 0 001.54-1.48z" fill="#4F0599"/>
  </g>
</svg>""",
    "perplexity-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M22.3977 7.0896h-2.3106V.0676l-7.5094 6.3542V.1577h-1.1554v6.1966L4.4904 0v7.0896H1.6023v10.3976h2.8882V24l6.932-6.3591v6.2005h1.1554v-6.0469l6.9318 6.1807v-6.4879h2.8882V7.0896zm-3.4657-4.531v4.531h-5.355l5.355-4.531zm-13.2862.0676 4.8691 4.4634H5.6458V2.6262zM2.7576 16.332V8.245h7.8476l-6.1149 6.1147v1.9723H2.7576zm2.8882 5.0404v-3.8852h.0001v-2.6488l5.7763-5.7764v7.0111l-5.7764 5.2993zm12.7086.0248-5.7766-5.1509V9.0618l5.7766 5.7766v6.5588zm2.8882-5.0652h-1.733v-1.9723L13.3948 8.245h7.8478v8.087z" fill="#20808D"/>
  </g>
</svg>""",
    "posthog-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M9.854 14.5 5 9.647.854 5.5A.5.5 0 0 0 0 5.854V8.44a.5.5 0 0 0 .146.353L5 13.647l.147.146L9.854 18.5l.146.147v-.049c.065.03.134.049.207.049h2.586a.5.5 0 0 0 .353-.854L9.854 14.5zm0-5-4-4a.487.487 0 0 0-.409-.144.515.515 0 0 0-.356.21.493.493 0 0 0-.089.288V8.44a.5.5 0 0 0 .147.353l9 9a.5.5 0 0 0 .853-.354v-2.585a.5.5 0 0 0-.146-.354l-5-5zm1-4a.5.5 0 0 0-.854.354V8.44a.5.5 0 0 0 .147.353l4 4a.5.5 0 0 0 .853-.354V9.854a.5.5 0 0 0-.146-.354l-4-4zm12.647 11.515a3.863 3.863 0 0 1-2.232-1.1l-4.708-4.707a.5.5 0 0 0-.854.354v6.585a.5.5 0 0 0 .5.5H23.5a.5.5 0 0 0 .5-.5v-.6c0-.276-.225-.497-.499-.532zm-5.394.032a.8.8 0 1 1 0-1.6.8.8 0 0 1 0 1.6zM.854 15.5a.5.5 0 0 0-.854.354v2.293a.5.5 0 0 0 .5.5h2.293c.222 0 .39-.135.462-.309a.493.493 0 0 0-.109-.545L.854 15.501zM5 14.647.854 10.5a.5.5 0 0 0-.854.353v2.586a.5.5 0 0 0 .146.353L4.854 18.5l.146.147h2.793a.5.5 0 0 0 .353-.854L5 14.647z" fill="#F54E00"/>
  </g>
</svg>""",
    "supabase-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M11.9 1.036c-.015-.986-1.26-1.41-1.874-.637L.764 12.05C-.33 13.427.65 15.455 2.409 15.455h9.579l.113 7.51c.014.985 1.259 1.408 1.873.636l9.262-11.653c1.093-1.375.113-3.403-1.645-3.403h-9.642z" fill="#3ECF8E"/>
  </g>
</svg>""",
    "stripe-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)">
    <path d="M13.976 9.15c-2.172-.806-3.356-1.426-3.356-2.409 0-.831.683-1.305 1.901-1.305 2.227 0 4.515.858 6.09 1.631l.89-5.494C18.252.975 15.697 0 12.165 0 9.667 0 7.589.654 6.104 1.872 4.56 3.147 3.757 4.992 3.757 7.218c0 4.039 2.467 5.76 6.476 7.219 2.585.92 3.445 1.574 3.445 2.583 0 .98-.84 1.545-2.354 1.545-1.875 0-4.965-.921-6.99-2.109l-.9 5.555C5.175 22.99 8.385 24 11.714 24c2.641 0 4.843-.624 6.328-1.813 1.664-1.305 2.525-3.236 2.525-5.732 0-4.128-2.524-5.851-6.594-7.305h.003z" fill="#635BFF"/>
  </g>
</svg>""",
    "deepinfra-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)" fill="#2563EB">
    <title>DeepInfra</title><path d="M3.294 7.821A2.297 2.297 0 011 5.527a2.297 2.297 0 012.294-2.295A2.297 2.297 0 015.59 5.527 2.297 2.297 0 013.294 7.82zm0-3.688a1.396 1.396 0 000 2.79 1.396 1.396 0 000-2.79zM3.294 14.293A2.297 2.297 0 011 11.998a2.297 2.297 0 012.294-2.294 2.297 2.297 0 012.295 2.294 2.297 2.297 0 01-2.295 2.295zm0-3.688a1.395 1.395 0 000 2.788 1.395 1.395 0 100-2.788zM3.294 20.761A2.297 2.297 0 011 18.467a2.297 2.297 0 012.294-2.295 2.297 2.297 0 012.295 2.295 2.297 2.297 0 01-2.295 2.294zm0-3.688a1.396 1.396 0 000 2.79 1.396 1.396 0 000-2.79zM20.738 7.821a2.297 2.297 0 01-2.295-2.294 2.297 2.297 0 012.294-2.295 2.297 2.297 0 012.295 2.295 2.297 2.297 0 01-2.294 2.294zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.626-1.395-1.395-1.395zM20.738 14.293a2.297 2.297 0 01-2.295-2.295 2.297 2.297 0 012.294-2.294 2.297 2.297 0 012.295 2.294 2.297 2.297 0 01-2.294 2.295zm0-3.688c-.769 0-1.395.625-1.395 1.393a1.396 1.396 0 002.79 0c0-.77-.626-1.393-1.395-1.393zM20.738 20.761a2.297 2.297 0 01-2.295-2.294 2.297 2.297 0 012.294-2.295 2.297 2.297 0 012.295 2.295 2.297 2.297 0 01-2.294 2.294zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.626-1.395-1.395-1.395zM12.016 11.057a2.297 2.297 0 01-2.294-2.294 2.297 2.297 0 012.294-2.295 2.297 2.297 0 012.295 2.295 2.297 2.297 0 01-2.295 2.294zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.625-1.395-1.395-1.395zM12.017 4.589a2.297 2.297 0 01-2.295-2.295A2.297 2.297 0 0112.017 0a2.297 2.297 0 012.294 2.294 2.297 2.297 0 01-2.294 2.295zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.626-1.395-1.395-1.395zM12.017 17.529a2.297 2.297 0 01-2.295-2.295 2.297 2.297 0 012.295-2.294 2.297 2.297 0 012.294 2.294 2.297 2.297 0 01-2.294 2.295zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.626-1.395-1.395-1.395zM12.016 24a2.297 2.297 0 01-2.294-2.295 2.297 2.297 0 012.294-2.294 2.297 2.297 0 012.295 2.294A2.297 2.297 0 0112.016 24zm0-3.688a1.396 1.396 0 101.395 1.395c0-.77-.625-1.395-1.395-1.395z"></path><path d="M8.363 8.222a.742.742 0 01-.277-.053l-1.494-.596a.75.75 0 11.557-1.392l1.493.595a.75.75 0 01-.278 1.446h-.001zM8.363 14.566a.743.743 0 01-.277-.053l-1.494-.595a.75.75 0 11.557-1.393l1.493.596a.75.75 0 01-.278 1.445h-.001zM17.124 11.397a.741.741 0 01-.277-.054l-1.493-.595a.75.75 0 11.555-1.392l1.493.595a.75.75 0 01-.278 1.446zM17.124 5.05a.744.744 0 01-.277-.054L15.354 4.4a.75.75 0 01.555-1.392l1.493.596a.75.75 0 01-.278 1.445zM17.124 17.739a.743.743 0 01-.277-.053l-1.494-.596a.75.75 0 11.556-1.392l1.493.596a.75.75 0 01-.278 1.445zM6.91 17.966a.75.75 0 01-.279-1.445l1.494-.595a.749.749 0 11.556 1.392l-1.493.595a.743.743 0 01-.277.053H6.91zM6.91 11.66a.75.75 0 01-.279-1.446l1.494-.595a.75.75 0 01.556 1.392l-1.493.595a.743.743 0 01-.277.053H6.91zM6.91 5.033a.75.75 0 01-.279-1.446l1.494-.595a.75.75 0 01.556 1.392l-1.493.596a.744.744 0 01-.277.053H6.91zM8.363 21.364a.743.743 0 01-.277-.053l-1.494-.596a.75.75 0 01.555-1.392l1.494.595a.75.75 0 01-.278 1.446zM15.63 8.223a.75.75 0 01-.278-1.447l1.494-.595a.75.75 0 01.556 1.393l-1.494.595a.744.744 0 01-.276.054h-.002zM15.63 14.567a.75.75 0 01-.278-1.446l1.494-.596a.75.75 0 01.556 1.394l-1.494.595a.743.743 0 01-.276.053h-.002zM15.63 21.363a.749.749 0 01-.278-1.445l1.494-.595a.75.75 0 11.555 1.392l-1.494.595a.741.741 0 01-.277.053z"></path>
  </g>
</svg>""",
    "runpod-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.14)" fill="#6E40C9">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M170.04 163.76C180.216 157.899 186.485 147.067 186.485 135.344L186.485 70.656C186.485 58.9334 180.216 48.1013 170.04 42.24L113.887 9.89597C103.71 4.03467 91.1731 4.03468 80.997 9.89598L24.8432 42.24C14.6671 48.1013 8.39844 58.9334 8.39844 70.656L8.39844 135.344C8.39844 147.067 14.6672 157.899 24.8432 163.76L80.997 196.104C91.1731 201.965 103.711 201.965 113.887 196.104L170.04 163.76ZM170.04 135.344C170.04 141.205 166.906 146.621 161.818 149.552L132.428 166.48C129.838 167.972 128.543 168.718 127.48 168.607C126.553 168.51 125.711 168.025 125.163 167.272C124.535 166.41 124.535 164.918 124.535 161.934L124.535 128.078C124.535 122.217 127.66 116.8 132.748 113.869L161.818 97.0984C166.906 94.1671 170.04 99.5828 170.04 105.444L170.04 135.344Z"/>
  </g>
</svg>""",
    "cerebras": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)" fill="#FF6422">
    <title>Cerebras</title><path clip-rule="evenodd" d="M14.121 2.701a9.299 9.299 0 000 18.598V22.7c-5.91 0-10.7-4.791-10.7-10.701S8.21 1.299 14.12 1.299V2.7zm4.752 3.677A7.353 7.353 0 109.42 17.643l-.901 1.074a8.754 8.754 0 01-1.08-12.334 8.755 8.755 0 0112.335-1.08l-.901 1.075zm-2.255.844a5.407 5.407 0 00-5.048 9.563l-.656 1.24a6.81 6.81 0 016.358-12.043l-.654 1.24zM14.12 8.539a3.46 3.46 0 100 6.922v1.402a4.863 4.863 0 010-9.726v1.402z"></path><path d="M15.407 10.836a2.24 2.24 0 00-.51-.409 1.084 1.084 0 00-.544-.152c-.255 0-.483.047-.684.14a1.58 1.58 0 00-.84.912c-.074.203-.11.416-.11.631 0 .218.036.43.11.631a1.594 1.594 0 00.84.913c.2.093.43.14.684.14.216 0 .417-.046.602-.135.188-.09.35-.225.475-.392l.928 1.006c-.14.14-.3.261-.482.363a3.367 3.367 0 01-1.083.38c-.17.026-.317.04-.44.04a3.315 3.315 0 01-1.182-.21 2.825 2.825 0 01-.961-.597 2.816 2.816 0 01-.644-.929 2.987 2.987 0 01-.238-1.21c0-.444.08-.847.238-1.21.15-.35.368-.666.643-.929.278-.261.605-.464.962-.596a3.315 3.315 0 011.182-.21c.355 0 .712.068 1.072.204.361.138.685.36.944.649l-.962.97z"></path>
  </g>
</svg>""",
    "cerebras-cloud-startups": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(1.16)" fill="#FF6422">
    <title>Cerebras</title><path clip-rule="evenodd" d="M14.121 2.701a9.299 9.299 0 000 18.598V22.7c-5.91 0-10.7-4.791-10.7-10.701S8.21 1.299 14.12 1.299V2.7zm4.752 3.677A7.353 7.353 0 109.42 17.643l-.901 1.074a8.754 8.754 0 01-1.08-12.334 8.755 8.755 0 0112.335-1.08l-.901 1.075zm-2.255.844a5.407 5.407 0 00-5.048 9.563l-.656 1.24a6.81 6.81 0 016.358-12.043l-.654 1.24zM14.12 8.539a3.46 3.46 0 100 6.922v1.402a4.863 4.863 0 010-9.726v1.402z"></path><path d="M15.407 10.836a2.24 2.24 0 00-.51-.409 1.084 1.084 0 00-.544-.152c-.255 0-.483.047-.684.14a1.58 1.58 0 00-.84.912c-.074.203-.11.416-.11.631 0 .218.036.43.11.631a1.594 1.594 0 00.84.913c.2.093.43.14.684.14.216 0 .417-.046.602-.135.188-.09.35-.225.475-.392l.928 1.006c-.14.14-.3.261-.482.363a3.367 3.367 0 01-1.083.38c-.17.026-.317.04-.44.04a3.315 3.315 0 01-1.182-.21 2.825 2.825 0 01-.961-.597 2.816 2.816 0 01-.644-.929 2.987 2.987 0 01-.238-1.21c0-.444.08-.847.238-1.21.15-.35.368-.666.643-.929.278-.261.605-.464.962-.596a3.315 3.315 0 011.182-.21c.355 0 .712.068 1.072.204.361.138.685.36.944.649l-.962.97z"></path>
  </g>
</svg>""",
    "together-ai-startup-program": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.28)">
    <title>together.ai</title><path d="M23.197 4.503A6 6 0 0015 2.307a5.973 5.973 0 00-2.995 4.933l5.996.008v.515h-5.996c.039.937.298 1.87.8 2.74a6 6 0 1010.39-6z"></path><path d="M.805 4.5A6 6 0 003 12.697a5.972 5.972 0 005.77.127L5.779 7.627l.446-.257 2.997 5.192A6 6 0 10.804 4.5z"></path><path d="M12 23.894a6 6 0 005.999-6c0-2.13-1.1-3.996-2.775-5.06l-3.005 5.189-.444-.258 2.997-5.192A6 6 0 1012 23.894z"></path>
  </g>
</svg>""",
    "mistral-ai-startup-access": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.28)">
    <title>Mistral</title><path clip-rule="evenodd" d="M3.428 3.4h3.429v3.428h3.429v3.429h-.002 3.431V6.828h3.427V3.4h3.43v13.714H24v3.429H13.714v-3.428h-3.428v-3.429h-3.43v3.428h3.43v3.429H0v-3.429h3.428V3.4zm10.286 13.715h3.428v-3.429h-3.427v3.429z"></path>
  </g>
</svg>""",
    "groqcloud-builder-program": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.28)">
    <title>Groq</title><path d="M12.036 2c-3.853-.035-7 3-7.036 6.781-.035 3.782 3.055 6.872 6.908 6.907h2.42v-2.566h-2.292c-2.407.028-4.38-1.866-4.408-4.23-.029-2.362 1.901-4.298 4.308-4.326h.1c2.407 0 4.358 1.915 4.365 4.278v6.305c0 2.342-1.944 4.25-4.323 4.279a4.375 4.375 0 01-3.033-1.252l-1.851 1.818A7 7 0 0012.029 22h.092c3.803-.056 6.858-3.083 6.879-6.816v-6.5C18.907 4.963 15.817 2 12.036 2z"></path>
  </g>
</svg>""",
    "lambda-labs-startup-credits": """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect width="48" height="48" rx="10" class="logo-backdrop" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.2"/>
  <g transform="translate(10, 10) scale(0.28)">
    <title>Lambda</title><path d="M2 2h20v20H2V2zm1.768 18.237h16.459V3.761H3.768v16.476zm3.515-14.91l3.479 6.176-3.871 7.154h2.493l2.58-4.883 2.747 4.883h2.54L9.82 5.324l-2.538.002z"></path>
  </g>
</svg>""",
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
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       DISCIPLINED DESIGN SYSTEM TOKENS & TYPOGRAPHY
       Strict 2-Font Hierarchy (Zero Vibe-Coded Fonts):
       1. Inter: UI, Headings, Controls, Brand Wordmark & Body
       2. Geist Mono: Citations, Codes, Per-Million Rates & Technical Telemetry
       ========================================================================== */
    :root {{
      --font-display: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-ui: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, monospace;

      /* Calm Light Paper Palette */
      --bg-page: #F7F7F8;
      --bg-shell: #FFFFFF;
      --bg-card: #FFFFFF;
      --bg-card-hover: #FBFBFC;
      --bg-card-active: #F8F9FA;
      --bg-card-subtle: #F8FAFC;
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
      --bg-card-subtle: #14181E;
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

    [data-theme="dark"] .aws-letters {{
      fill: #FFFFFF !important;
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

    .app-shell.mobile-mode .controls-row {{
      padding: 12px 16px;
      flex-direction: column;
      align-items: stretch;
      gap: 10px;
    }}

    .app-shell.mobile-mode .category-pills {{
      flex-wrap: wrap;
      gap: 6px;
    }}

    .app-shell.mobile-mode .search-box {{
      max-width: 100%;
      min-width: 100%;
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

    /* Controls: Category Filter Pills & Live Search Bar */
    .controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 14px 32px;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--bg-card-subtle);
      flex-wrap: wrap;
    }}

    .category-pills {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .cat-pill {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-family: var(--font-ui);
      font-size: 12px;
      font-weight: 500;
      padding: 6px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      user-select: none;
      box-shadow: var(--shadow-subtle);
      white-space: nowrap;
    }}

    .cat-pill:hover {{
      color: var(--text-primary);
      border-color: var(--border-hover);
      background: var(--bg-card-hover);
    }}

    .cat-pill.active {{
      background: var(--text-primary);
      color: var(--bg-shell);
      border-color: var(--text-primary);
      font-weight: 600;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    }}

    [data-theme="dark"] .cat-pill.active {{
      background: #F8FAFC;
      color: #0F172A;
      border-color: #F8FAFC;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
    }}

    .search-box {{
      position: relative;
      display: flex;
      align-items: center;
      flex: 1;
      min-width: 240px;
      max-width: 360px;
    }}

    .search-box input,
    #program-search {{
      width: 100%;
      height: 35px;
      padding: 0 14px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      color: var(--text-primary);
      font-family: var(--font-ui);
      font-size: 12.5px;
      outline: none;
      box-shadow: var(--shadow-subtle);
      transition: all 0.15s ease;
    }}

    .search-box input::placeholder,
    #program-search::placeholder {{
      color: var(--text-faint);
      font-family: var(--font-ui);
      font-size: 12px;
    }}

    .search-box input:focus,
    #program-search:focus {{
      border-color: var(--border-hover);
      box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15);
      background: var(--bg-shell);
    }}

    .carousel-empty-state {{
      width: 100%;
      padding: 36px 20px;
      text-align: center;
      color: var(--text-muted);
      font-family: var(--font-ui);
      font-size: 13.5px;
      background: var(--bg-card-subtle);
      border-radius: var(--radius-tile);
      border: 1px dashed var(--border-subtle);
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
      .controls-row {{
        padding: 12px 16px;
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
      }}
      .category-pills {{
        flex-wrap: wrap;
        gap: 6px;
      }}
      .search-box {{
        max-width: 100%;
        min-width: 100%;
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

    .portal-screenshot-dark {{
      display: none;
    }}

    [data-theme="dark"] .portal-screenshot-light {{
      display: none;
    }}

    [data-theme="dark"] .portal-screenshot-dark {{
      display: block;
    }}

    [data-theme="dark"] .portal-preview-card {{
      background: #0E1217;
      border-color: rgba(255, 255, 255, 0.1);
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6);
    }}

    [data-theme="dark"] .portal-mockup-header {{
      background: #14181F;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}

    [data-theme="dark"] .mockup-address {{
      background: #0B0E12;
      border-color: rgba(255, 255, 255, 0.08);
      color: #94A3B8;
    }}

    [data-theme="dark"] .mockup-dots span {{
      opacity: 0.6;
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
        <span class="brand-count">{len(companies)} PROGRAMS</span>
      </div>
      <p class="brand-subtitle">The Pre-Flight Audited Cloud Compute, Foundation Model &amp; SaaS Treasury for AI Founders.</p>
    </div>

    <!-- Controls Row: Category Filter Pills & Live Search Bar -->
    <div class="controls-row">
      <div class="category-pills">
        <button class="cat-pill active" onclick="setCategory('All')">All</button>
        <button class="cat-pill" onclick="setCategory('Hyperscalers')">Hyperscalers</button>
        <button class="cat-pill" onclick="setCategory('Frontier AI')">Frontier AI</button>
        <button class="cat-pill" onclick="setCategory('GPU &amp; Compute')">GPU &amp; Compute</button>
        <button class="cat-pill" onclick="setCategory('Dev Infra')">Dev Infra</button>
      </div>
      <div class="search-box">
        <input type="text" id="program-search" placeholder="Search 20 programs, models, disqualifiers..." oninput="handleSearch(this.value)" />
      </div>
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
    let currentCategory = 'all';
    let searchQuery = '';

    const CATEGORY_MAP = {{
      'hyperscalers': ['google-cloud', 'microsoft-founders-hub', 'aws-activate', 'oracle-cloud'],
      'frontier-ai': ['openai-startups', 'anthropic-startups', 'perplexity-startups', 'deepinfra-startups', 'cerebras-cloud-startups', 'together-ai-startup-program', 'mistral-ai-startup-access', 'groqcloud-builder-program'],
      'gpu-compute': ['nvidia-inception', 'scaleway-startups', 'runpod-startups', 'lambda-labs-startup-credits'],
      'dev-infra': ['cloudflare-startups', 'supabase-startups', 'posthog-startups', 'stripe-startups']
    }};

    function setCategory(cat) {{
      currentCategory = cat;
      const normalizedCat = cat.toLowerCase().replace(/[\s&]+/g, '-');

      const pills = document.querySelectorAll('.cat-pill');
      pills.forEach(btn => {{
        const btnText = btn.textContent.trim().toLowerCase().replace(/[\s&]+/g, '-');
        const isMatch = (normalizedCat === 'all' && (btnText === 'all' || btnText === '')) ||
                        (normalizedCat.includes('hyper') && btnText.includes('hyper')) ||
                        (normalizedCat.includes('frontier') && btnText.includes('frontier')) ||
                        ((normalizedCat.includes('gpu') || normalizedCat.includes('compute')) && (btnText.includes('gpu') || btnText.includes('compute'))) ||
                        ((normalizedCat.includes('dev') || normalizedCat.includes('infra')) && (btnText.includes('dev') || btnText.includes('infra')));
        if (isMatch) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      renderCarousel();
    }}

    function handleSearch(q) {{
      searchQuery = q || '';
      renderCarousel();
    }}

    function getFilteredCompanies() {{
      const q = searchQuery.trim().toLowerCase();
      const normCat = currentCategory.toLowerCase().replace(/[\s&]+/g, '-');

      return COMPANIES_DATA.filter(c => {{
        // Category filtering
        if (normCat !== 'all') {{
          let allowedIds = [];
          if (normCat.includes('hyper')) {{
            allowedIds = CATEGORY_MAP['hyperscalers'];
          }} else if (normCat.includes('frontier')) {{
            allowedIds = CATEGORY_MAP['frontier-ai'];
          }} else if (normCat.includes('gpu') || normCat.includes('compute')) {{
            allowedIds = CATEGORY_MAP['gpu-compute'];
          }} else if (normCat.includes('dev') || normCat.includes('infra')) {{
            allowedIds = CATEGORY_MAP['dev-infra'];
          }}
          if (!allowedIds.includes(c.id)) {{
            return false;
          }}
        }}

        // Search filtering: matches name, programName, topDisqualifier, perkHighlight, or eligibleServices
        if (q) {{
          const inName = c.name && c.name.toLowerCase().includes(q);
          const inProgram = c.programName && c.programName.toLowerCase().includes(q);
          const inDisqualifier = c.topDisqualifier && c.topDisqualifier.toLowerCase().includes(q);
          const inPerk = c.perkHighlight && c.perkHighlight.toLowerCase().includes(q);
          const inServices = Array.isArray(c.eligibleServices)
            ? c.eligibleServices.some(s => s && s.toLowerCase().includes(q))
            : (typeof c.eligibleServices === 'string' && c.eligibleServices.toLowerCase().includes(q));

          if (!inName && !inProgram && !inDisqualifier && !inPerk && !inServices) {{
            return false;
          }}
        }}

        return true;
      }});
    }}

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
      const filtered = getFilteredCompanies();

      if (filtered.length === 0) {{
        track.innerHTML = '<div class="carousel-empty-state">No programs match your search or filter.</div>';
        renderDetail();
        return;
      }}

      if (!filtered.some(c => c.id === selectedId)) {{
        selectedId = filtered[0].id;
      }}

      track.innerHTML = filtered.map(c => {{
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

      renderDetail();
    }}

    function renderDetail() {{
      const container = document.getElementById('detail-view');
      const filtered = getFilteredCompanies();

      if (filtered.length === 0) {{
        container.innerHTML = `
          <div class="carousel-empty-state" style="margin: 20px 0; border: none; padding: 48px 24px;">
            <p style="font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 6px;">No programs match your search or filter.</p>
            <p style="font-size: 13px; color: var(--text-muted);">Try adjusting your category filter or search terms above.</p>
          </div>
        `;
        return;
      }}

      const c = COMPANIES_DATA.find(item => item.id === selectedId) || filtered[0] || COMPANIES_DATA[0];

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
              <img src="${{c.portalScreenshot || ('assets/portals/' + c.id + '.png')}}" alt="${{c.name}} Official Portal Preview (Light)" class="portal-screenshot-img portal-screenshot-light" />
              <img src="${{'assets/portals/dark/' + c.id + '.png'}}" alt="${{c.name}} Official Portal Preview (Dark)" class="portal-screenshot-img portal-screenshot-dark" onerror="this.style.display='none'; this.previousElementSibling.style.display='block';" />
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

            <div class="model-citations-box" style="margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border-subtle);">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                <span style="font-family: var(--font-mono); font-size: 10.5px; font-weight: 600; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px;">
                  Verified Live Citations & Docs (Audited Sep 14, 2026)
                </span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 5px;">
                ${{c.citations.map((cite, i) => `
                  <div style="display: flex; align-items: center; gap: 8px; font-size: 11.5px; font-family: var(--font-mono);">
                    <span style="color: var(--accent-green); font-weight: 700;">[${{i+1}}]</span>
                    <a href="${{cite.url}}" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none;">
                      ${{cite.title}} &#8599;
                    </a>
                  </div>
                `).join('')}}
              </div>
            </div>
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
