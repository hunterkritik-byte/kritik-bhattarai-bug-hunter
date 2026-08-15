/**
 * Signal After Dark page: offset signal-spine layout, Tracer Cyan accents, and restrained 3D security-console motion.
 * Typography: Space Grotesk for human-facing text; JetBrains Mono for evidence labels and metadata.
 */
import {
  ArrowDownRight,
  ArrowUpRight,
  Github,
  Mail,
  MapPin,
  Radar,
  ScanLine,
  ShieldCheck,
  Terminal,
} from "lucide-react";
import TerminalConsole from "@/components/TerminalConsole";

const assets = {
  hero: "/manus-storage/kritik-signal-hero_0c001e51.png",
  field: "/manus-storage/kritik-field-visual_eb7cf515.png",
  research: "/manus-storage/kritik-research-visual_8da623bd.png",
  contact: "/manus-storage/kritik-contact-visual_c94f662f.png",
  logo: "/manus-storage/kritik-logo-mark_29848a63.png",
};

function SignalLabel({ children }: { children: React.ReactNode }) {
  return <p className="signal-label">{children}</p>;
}

export default function Home() {
  return (
    <div className="site-shell">
      <div className="ambient-noise" aria-hidden="true" />
      <header className="site-header">
        <a className="brand-lockup" href="#top" aria-label="Kritik Bhattarai home">
          <img className="brand-mark" src={assets.logo} alt="Abstract K signal mark" />
          <span className="brand-wordmark">KRITIK<span>/</span>BHATTARAI</span>
        </a>
        <nav className="site-nav" aria-label="Primary navigation">
          <a href="#profile">Profile</a>
          <a href="#method">Method</a>
          <a href="#contact">Contact</a>
        </nav>
        <a className="header-link" href="https://github.com/hunterkritik-byte" target="_blank" rel="noreferrer">
          <Github size={15} aria-hidden="true" /> GitHub
        </a>
      </header>

      <main id="top">
        <section className="hero-section" aria-labelledby="hero-title">
          <div className="hero-copy">
            <SignalLabel>01 / INDEPENDENT SECURITY RESEARCHER</SignalLabel>
            <div className="hero-heading-wrap">
              <p className="hero-kicker"><span className="status-dot" />ONLINE FROM ITAHARI, NEPAL</p>
              <h1 id="hero-title">Trace the surface.<br /><em>Verify the signal.</em></h1>
            </div>
            <p className="hero-intro">
              I’m <strong>Kritik Bhattarai</strong>, a 17-year-old bug bounty hunter from Itahari. I study web attack surfaces, validate security behavior, and report findings responsibly.
            </p>
            <div className="hero-actions">
              <a className="primary-cta" href="mailto:projectvuln@gmail.com">
                Open a secure channel <ArrowUpRight size={17} aria-hidden="true" />
              </a>
              <a className="text-cta" href="#method">View operating principles <ArrowDownRight size={17} aria-hidden="true" /></a>
            </div>
            <div className="hero-meta">
              <span><MapPin size={14} /> Itahari, Nepal</span>
              <span><Radar size={14} /> Bug bounty research</span>
            </div>
          </div>

          <div className="hero-visual" aria-label="Abstract three-dimensional security signal visualization">
            <img className="hero-art" src={assets.hero} alt="Floating cyan wireframe security monolith" />
            <div className="orbital-stage" aria-hidden="true">
              <div className="orbit orbit-one" />
              <div className="orbit orbit-two" />
              <div className="core-shape">
                <span className="core-face core-front" />
                <span className="core-face core-back" />
                <span className="core-face core-left" />
                <span className="core-face core-right" />
              </div>
              <span className="pulse-node node-a" />
              <span className="pulse-node node-b" />
              <span className="pulse-node node-c" />
            </div>
            <p className="visual-caption">ACTIVE SURFACE / <span>MONITORED</span></p>
          </div>
        </section>

        <section className="terminal-section" aria-labelledby="terminal-title">
          <div className="terminal-section-lead">
            <SignalLabel>01.5 / FIELD INSTRUMENT</SignalLabel>
            <h2 id="terminal-title">Run the public <span>signal console.</span></h2>
            <p>This is a portfolio interface, not a live system shell. It only returns public information about my research focus and contact channel.</p>
          </div>
          <TerminalConsole />
        </section>

        <section className="signal-section profile-section" id="profile" aria-labelledby="profile-title">
          <div className="signal-spine" aria-hidden="true"><span /></div>
          <div className="section-number">02</div>
          <div className="profile-grid">
            <div className="section-copy">
              <SignalLabel>FIELD PROFILE</SignalLabel>
              <h2 id="profile-title">Curiosity is the first tool. <span>Care is the second.</span></h2>
              <p>
                My work begins with patient observation: how an application exposes its trust boundaries, how users move through a product, and where a small unexpected behavior could matter.
              </p>
              <p>
                I’m building in public, learning continuously, and keeping responsible disclosure at the center of every research path.
              </p>
              <div className="identity-strip">
                <span>AGE <b>17</b></span><span>BASE <b>ITAHARI</b></span><span>MODE <b>RESEARCH</b></span>
              </div>
              <p className="field-coordinate"><span>FIELD NODE</span> ITAHARI / NEPAL / TERAI SURFACE</p>
            </div>
            <figure className="section-visual field-visual evidence-panel">
              <img src={assets.field} alt="Abstract glowing topographic security network inspired by Nepal" />
              <span className="scan-overlay" aria-hidden="true" />
              <figcaption><MapPin size={14} /> NEPAL / NETWORK TOPOGRAPHY</figcaption>
            </figure>
          </div>
        </section>

        <section className="signal-section method-section" id="method" aria-labelledby="method-title">
          <div className="signal-spine" aria-hidden="true"><span /></div>
          <div className="section-number">03</div>
          <div className="method-intro">
            <div>
              <SignalLabel>OPERATING PRINCIPLES</SignalLabel>
              <h2 id="method-title">Signal, evidence, <span>responsible action.</span></h2>
            </div>
            <p>I focus on clear technical evidence, tight reproduction steps, and research that respects both users and systems.</p>
          </div>
          <div className="method-layout">
            <figure className="section-visual research-visual evidence-panel">
              <img src={assets.research} alt="Transparent geometric cube with cyan research pathway" />
              <span className="scan-overlay" aria-hidden="true" />
              <figcaption><ScanLine size={14} /> EVIDENCE PATH / MINIMIZED</figcaption>
            </figure>
            <div className="principle-stack">
              <article className="principle-card">
                <span className="card-index">01</span><Terminal size={21} aria-hidden="true" />
                <h3>Map deliberately</h3>
                <p>Understand an application’s visible surface before making assumptions about its hidden behavior.</p>
              </article>
              <article className="principle-card">
                <span className="card-index">02</span><Radar size={21} aria-hidden="true" />
                <h3>Validate narrowly</h3>
                <p>Keep testing focused, low-impact, and tied to a clear security question.</p>
              </article>
              <article className="principle-card">
                <span className="card-index">03</span><ShieldCheck size={21} aria-hidden="true" />
                <h3>Report responsibly</h3>
                <p>Communicate impact, steps, and remediation context in a way that helps teams act.</p>
              </article>
            </div>
          </div>
        </section>

        <section className="contact-section" id="contact" aria-labelledby="contact-title">
          <div className="contact-art-wrap" aria-hidden="true"><img src={assets.contact} alt="" /></div>
          <div className="contact-copy">
            <SignalLabel>04 / CONTACT CHANNEL</SignalLabel>
            <h2 id="contact-title">Have a security lead?<br /><span>Open a secure channel.</span></h2>
            <p>For responsible security communication, research collaboration, or a verified lead, reach out directly.</p>
            <div className="contact-links">
              <a href="mailto:projectvuln@gmail.com"><Mail size={18} /> projectvuln@gmail.com <ArrowUpRight size={16} /></a>
              <a href="https://github.com/hunterkritik-byte" target="_blank" rel="noreferrer"><Github size={18} /> github.com/hunterkritik-byte <ArrowUpRight size={16} /></a>
            </div>
          </div>
          <div className="contact-stamp" aria-label="Kritik Bhattarai research status">
            <span>RESEARCHER</span><b>KB</b><span>NEPAL / 2026</span>
          </div>
        </section>
      </main>

      <footer className="site-footer">
        <p>© {new Date().getFullYear()} KRITIK BHATTARAI <span>/</span> SECURITY RESEARCH PORTFOLIO</p>
        <a href="#top">RETURN TO SIGNAL <ArrowUpRight size={13} /></a>
      </footer>
    </div>
  );
}
