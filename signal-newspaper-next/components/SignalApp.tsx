"use client";

import { useState } from "react";
import type { DailyBrief } from "@/data/brief";

type Route = "today" | "signal" | "connect" | "founder" | "sources" | "explore" | "learn" | "saved" | "profile";
type Props = { brief: DailyBrief };
const mainRoutes: Route[] = ["today", "explore", "learn", "saved", "profile"];

export default function SignalApp({ brief }: Props) {
  const [route, setRoute] = useState<Route>("today");
  const [depth, setDepth] = useState<"simple" | "deep">("simple");
  const [activeSignal, setActiveSignal] = useState(0);
  const [founderOpen, setFounderOpen] = useState(false);
  const activeNav = mainRoutes.includes(route) ? route : "today";
  const activeSignalItem = brief.signals[activeSignal];

  function go(next: Route) {
    setRoute(next);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <div className="app-shell">
      <header className="masthead">
        <button className="icon-button" aria-label="Open menu">☰</button>
        <div className="masthead-title">
          <div className="brand">SIGNAL</div>
          <div className="brand-sub">CLEARER CONTEXT FOR BRAVER BUILDERS</div>
        </div>
        <button className="icon-button" aria-label="Search">⌕</button>
      </header>

      <main>
        {route === "today" && <TodayScreen brief={brief} go={go} />}
        {route === "signal" && <KeySignalScreen brief={brief} depth={depth} setDepth={setDepth} go={go} />}
        {route === "connect" && <ConnectScreen brief={brief} activeSignal={activeSignal} setActiveSignal={setActiveSignal} activeSignalItem={activeSignalItem} go={go} />}
        {route === "founder" && <FounderScreen brief={brief} open={founderOpen} setOpen={setFounderOpen} go={go} />}
        {route === "sources" && <SourcesScreen brief={brief} go={go} />}
        {route === "explore" && <Placeholder title="Explore" body="Browse themes, companies, research threads, and ideas beyond today’s brief." />}
        {route === "learn" && <Placeholder title="Learn" body="A personal map of concepts you already understand — so Signal can build forward instead of repeating itself." />}
        {route === "saved" && <Placeholder title="Saved" body="Stories, clips, founder questions, and ideas worth returning to." />}
        {route === "profile" && <Placeholder title="Profile" body="Tune the topics, depth, sources, and founder lenses Signal uses for your daily brief." />}
      </main>

      <nav className="bottom-nav">
        {(["today","explore","learn","saved","profile"] as Route[]).map(item => (
          <button key={item} className={activeNav === item ? "active" : ""} onClick={() => go(item)}>
            <span>{item === "today" ? "◼" : item === "explore" ? "⌕" : item === "learn" ? "▣" : item === "saved" ? "⌑" : "◌"}</span>
            <b>{item[0].toUpperCase() + item.slice(1)}</b>
          </button>
        ))}
      </nav>
    </div>
  );
}

function TodayScreen({ brief, go }: { brief: DailyBrief; go: (r: Route) => void }) {
  return (
    <section className="page">
      <div className="meta-strip">{brief.date.toUpperCase()} <span>•</span> 5 SIGNALS <span>•</span> {brief.readingMinutes} MIN <span>•</span> {brief.sourceCount} SOURCES</div>
      <article className="front-story">
        <div className="news-art hero-news-art"><div className="ai-crate">AI</div><div className="worker one"></div><div className="worker two"></div><div className="skyline"></div></div>
        <div className="front-copy">
          <span className="label">{brief.lead.kicker}</span>
          <h1>{brief.lead.headline}</h1>
          <p>{brief.lead.dek}</p>
          <div className="button-row"><button className="black-button" onClick={() => go("signal")}>Read the brief →</button><button className="text-button" onClick={() => go("connect")}>3 key signals ↓</button></div>
        </div>
      </article>
      <section className="editorial-section"><span className="label">Why it matters</span><p>{brief.lead.whyItMatters}</p></section>
      <section className="big-picture"><span className="label">The big picture</span><div className="news-art landscape-art"><div className="sun"></div><div className="bridge"></div></div><blockquote>“{brief.lead.bigPicture}”<small>— SIGNAL</small></blockquote></section>
    </section>
  );
}

function KeySignalScreen({ brief, depth, setDepth, go }: { brief: DailyBrief; depth: "simple"|"deep"; setDepth: (v:"simple"|"deep")=>void; go:(r:Route)=>void }) {
  return (
    <section className="page">
      <StoryHeader index="01 / 05" title="KEY SIGNAL" back={() => go("today")} />
      <h1 className="story-title">{brief.keySignal.headline}</h1>
      <p className="story-dek">{brief.keySignal.dek}</p>
      <div className="news-art chip-lab"><div className="chip-block">AI</div><div className="engineer"></div></div>
      <div className="fact-pill">✓ Confirmed by {brief.keySignal.confirmedBy} sources</div>
      <div className="segmented"><button className={depth === "simple" ? "active" : ""} onClick={() => setDepth("simple")}>Simple</button><button className={depth === "deep" ? "active" : ""} onClick={() => setDepth("deep")}>Deep</button></div>
      <section className="editorial-section"><span className="label">So what does that actually mean?</span><p>{depth === "simple" ? brief.keySignal.simple : brief.keySignal.deep}</p><div className="definition"><b>{brief.keySignal.term.label} ↗</b><span>{brief.keySignal.term.definition}</span></div></section>
      {depth === "deep" && <section className="editorial-section"><span className="label">Why it matters</span><p>{brief.lead.whyItMatters}</p></section>}
      <button className="wide-button" onClick={() => go("founder")}>Take me deeper →</button>
    </section>
  );
}

function ConnectScreen({ brief, activeSignal, setActiveSignal, activeSignalItem, go }: { brief: DailyBrief; activeSignal:number; setActiveSignal:(n:number)=>void; activeSignalItem:DailyBrief["signals"][number]; go:(r:Route)=>void }) {
  return (
    <section className="page">
      <StoryHeader index="02 / 05" title="CONNECT THE DOTS" back={() => go("today")} />
      <h1 className="story-title">These aren’t three separate stories.</h1>
      <p className="story-dek">They’re evidence of the same transition.</p>
      <div className="signal-orbs">{brief.signals.map((item,i)=><button key={item.id} className={activeSignal === i ? "active" : ""} onClick={()=>setActiveSignal(i)}><span className={`orb-art ${item.art}`}></span><b>{item.title}</b></button>)}</div>
      <div className="tap-note">Tap each signal to see how they connect.</div>
      <div className="signal-list">{brief.signals.map((item,i)=><button key={item.id} className={activeSignal === i ? "active" : ""} onClick={()=>setActiveSignal(i)}><span>{i+1}</span><div><b>{item.title}</b><small>{item.summary}</small></div></button>)}</div>
      <div className="insight-box">{activeSignalItem.insight}</div>
      <div className="dark-story"><div className="globe-art"></div><p><b>The connection:</b><br/>Lower costs drive adoption, adoption drives infrastructure investment, and that infrastructure can push costs down again.</p></div>
    </section>
  );
}

function FounderScreen({ brief, open, setOpen, go }: { brief: DailyBrief; open:boolean; setOpen:(v:boolean)=>void; go:(r:Route)=>void }) {
  return (
    <section className="page">
      <StoryHeader index="03 / 05" title="FOUNDER LENS" back={() => go("signal")} />
      <h1 className="story-title">{brief.founderLens.headline}</h1>
      <p className="story-dek">{brief.founderLens.intro}</p>
      <div className="news-art founder-art"><div className="founder-face"></div><div className="founder-city"></div></div>
      <button className="black-button" onClick={()=>setOpen(!open)}>{open ? "Insights revealed ✓" : "Reveal insights ↓"}</button>
      {open && <div className="founder-items">{brief.founderLens.items.map((item,i)=><article key={item.title}><span>{i+1}</span><div><b>{item.title}</b><p>{item.body}</p></div></article>)}</div>}
      <section className="expert-card"><span className="label">Expert take · {brief.expertTake.duration}</span><div className="audio"><button>▶</button><div className="wave">▂▅▃▇▄▆▂▅▇▃▆▄▇▅▂▆</div></div><blockquote>“{brief.expertTake.quote}”</blockquote><small>— {brief.expertTake.source}</small></section>
      <button className="wide-button" onClick={()=>go("sources")}>See the source trail →</button>
    </section>
  );
}

function SourcesScreen({ brief, go }: { brief: DailyBrief; go:(r:Route)=>void }) {
  return (
    <section className="page">
      <StoryHeader index="04 / 05" title="SOURCES & PERSPECTIVES" back={() => go("today")} />
      <h1 className="story-title">Where this story comes from.</h1>
      <p className="story-dek">We pull from trusted sources and show you why each one matters.</p>
      <div className="source-list">{brief.sources.map((source,i)=><article className="source-card" key={`${source.name}-${i}`}><div className={`source-icon kind-${source.kind}`}></div><div><b>{source.name.toUpperCase()}</b><small>{source.detail}{source.duration ? ` · ${source.duration}` : ""}</small>{source.quote && <em>{source.quote}</em>}</div><span>→</span></article>)}</div>
      <div className="takeaway"><div className="mountain-art"><div className="takeaway-sun"></div></div><span className="label light">If you remember one thing today</span><p>{brief.takeaway}</p><small>Tomorrow, watch:<br/><b>{brief.tomorrowWatch}</b></small></div>
    </section>
  );
}

function StoryHeader({ index, title, back }: { index:string; title:string; back:()=>void }) {
  return <div className="story-header"><button onClick={back}>←</button><div>{index} <span>{title}</span></div><button>⋯</button></div>;
}

function Placeholder({ title, body }: { title:string; body:string }) {
  return <section className="page placeholder"><span className="label">SIGNAL</span><h1 className="story-title">{title}</h1><p className="story-dek">{body}</p></section>;
}