# Signal Newspaper — Next.js Prototype

A real React/Next.js version of the Signal newspaper-style daily intelligence product.

## What changed from the static prototype

- React state and route-like screen transitions
- Structured daily briefing data in `data/brief.ts`
- Reusable screen components inside `components/SignalApp.tsx`
- Simple/Deep reading mode
- Interactive Connect the Dots signals
- Revealable Founder Lens
- Sources & Perspectives screen
- Bottom navigation shell for Today, Explore, Learn, Saved, and Profile

## Run

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

## Architecture direction

The UI is intentionally driven by a typed `DailyBrief` object. A future ingestion pipeline can generate this object from primary sources, trusted reporting, expert podcasts/newsletters, and Signal synthesis without rewriting the frontend.
