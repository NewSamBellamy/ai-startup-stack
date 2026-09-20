import SignalApp from "@/components/SignalApp";
import { todayBrief } from "@/data/brief";

export default function HomePage() {
  return <SignalApp brief={todayBrief} />;
}