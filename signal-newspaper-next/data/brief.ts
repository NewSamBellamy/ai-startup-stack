export type SourceKind = "primary" | "reporting" | "expert" | "signal";

export type BriefSource = {
  name: string;
  kind: SourceKind;
  detail: string;
  duration?: string;
  quote?: string;
};

export type SignalItem = {
  id: string;
  title: string;
  summary: string;
  insight: string;
  art: "chip" | "office" | "infra";
};

export type DailyBrief = {
  date: string;
  readingMinutes: number;
  sourceCount: number;
  lead: {
    kicker: string;
    headline: string;
    dek: string;
    whyItMatters: string;
    bigPicture: string;
  };
  keySignal: {
    headline: string;
    dek: string;
    confirmedBy: number;
    simple: string;
    deep: string;
    term: { label: string; definition: string };
  };
  signals: SignalItem[];
  founderLens: {
    headline: string;
    intro: string;
    items: { title: string; body: string }[];
    question: string;
  };
  expertTake: {
    source: string;
    duration: string;
    quote: string;
  };
  sources: BriefSource[];
  takeaway: string;
  tomorrowWatch: string;
};

export const todayBrief: DailyBrief = {
  date: "Sat, Sep 19, 2026",
  readingMinutes: 7,
  sourceCount: 23,
  lead: {
    kicker: "Today's shift",
    headline: "AI is moving from product to infrastructure.",
    dek: "Three developments this week quietly made that shift much more real.",
    whyItMatters:
      "AI isn’t just a new app anymore. It’s becoming essential infrastructure — like cloud, chips, and power. That changes who wins, what gets built, and where the opportunities are.",
    bigPicture: "Cheaper AI isn’t the end goal — it’s the beginning."
  },
  keySignal: {
    headline: "A new AI chip just changed the economics.",
    dek: "The newest generation of AI hardware improves the amount of useful work companies can get per dollar spent.",
    confirmedBy: 4,
    simple:
      "It’s becoming significantly cheaper for companies to run powerful AI models. That lowers the barrier to adopt AI across more industries — not just tech.",
    deep:
      "Lower inference costs change the economics of AI products: more use cases can move from demos to production because serving each request becomes cheaper and more predictable.",
    term: {
      label: "Inference",
      definition: "When an already-trained AI model actually performs a task."
    }
  },
  signals: [
    {
      id: "cheap-ai",
      title: "Cheaper AI",
      summary: "Compute costs drop, making powerful models accessible to more companies.",
      insight: "Cheaper AI expands the number of products that can make economic sense.",
      art: "chip"
    },
    {
      id: "enterprise",
      title: "Enterprise adoption",
      summary: "More companies integrate AI into core products and workflows.",
      insight: "The important signal is repeat use inside real businesses, not another impressive demo.",
      art: "office"
    },
    {
      id: "infrastructure",
      title: "Infrastructure buildout",
      summary: "Growing demand drives investment in chips, data centers, networking, and energy.",
      insight: "AI demand creates second-order markets around the infrastructure required to support it.",
      art: "infra"
    }
  ],
  founderLens: {
    headline: "There’s a less obvious opportunity hiding underneath this story.",
    intro: "Most people are focusing on the chip. The bigger opportunity is in what it unlocks.",
    items: [
      {
        title: "What changed economically",
        body: "Inference costs are dropping, compressing the cost to serve entirely new classes of AI products."
      },
      {
        title: "Where opportunity may move",
        body: "Specialized workflow tools, vertical applications, trusted data, and infrastructure services can become more valuable as base intelligence gets cheaper."
      },
      {
        title: "One question worth carrying",
        body: "Which industries are most unprepared for AI becoming dramatically cheaper and more capable?"
      }
    ],
    question: "What becomes newly possible when intelligence gets cheaper?"
  },
  expertTake: {
    source: "Latent Space",
    duration: "38 sec",
    quote: "The thing people are overlooking is not just the chip — it’s what this does to the entire supply chain."
  },
  sources: [
    { name: "Reuters", kind: "reporting", detail: "Original reporting", duration: "4 min read" },
    { name: "Company announcement", kind: "primary", detail: "Primary source", duration: "6 min read" },
    { name: "Latent Space", kind: "expert", detail: "Technical interpretation", duration: "12 min segment" },
    { name: "AI Daily Brief", kind: "expert", detail: "Industry reaction", duration: "6 min listen" },
    { name: "Signal", kind: "signal", detail: "Connected synthesis" }
  ],
  takeaway:
    "AI becoming cheaper isn’t the interesting part. What becomes economically possible because it’s cheaper is.",
  tomorrowWatch: "Enterprise AI deployment costs."
};