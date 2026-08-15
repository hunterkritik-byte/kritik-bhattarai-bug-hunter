/**
 * Signal After Dark component: a fixed-command, non-executing terminal interface with a restrained typing status.
 * It performs no network, shell, or code execution—commands only reveal public portfolio information.
 */
import { FormEvent, useEffect, useRef, useState } from "react";

type Entry = {
  command: string;
  response: string[];
};

const statusLines = [
  "collecting surface metadata...",
  "validating responsible research path...",
  "secure channel available...",
];

const commandResponses: Record<string, string[]> = {
  help: ["available commands: help, whoami, focus, contact, clear"],
  whoami: ["Kritik Bhattarai", "independent bug bounty hunter / Itahari, Nepal"],
  focus: ["surface mapping · focused validation · responsible disclosure"],
  contact: ["email: projectvuln@gmail.com", "github: github.com/hunterkritik-byte"],
};

function TypewriterStatus() {
  const [lineIndex, setLineIndex] = useState(0);
  const [characterCount, setCharacterCount] = useState(0);

  useEffect(() => {
    const line = statusLines[lineIndex];
    const isFinished = characterCount >= line.length;
    const timer = window.setTimeout(() => {
      if (isFinished) {
        setLineIndex(current => (current + 1) % statusLines.length);
        setCharacterCount(0);
      } else {
        setCharacterCount(current => current + 1);
      }
    }, isFinished ? 1600 : 34);

    return () => window.clearTimeout(timer);
  }, [characterCount, lineIndex]);

  return (
    <span className="terminal-type" aria-label={statusLines[lineIndex]}>
      {statusLines[lineIndex].slice(0, characterCount)}<span className="terminal-cursor" aria-hidden="true">▋</span>
    </span>
  );
}

export default function TerminalConsole() {
  const [history, setHistory] = useState<Entry[]>([
    { command: "boot", response: ["signal_console v1.0", "public portfolio interface / execution disabled"] },
  ]);
  const [input, setInput] = useState("");
  const outputRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    outputRef.current?.scrollTo({ top: outputRef.current.scrollHeight, behavior: "smooth" });
  }, [history]);

  function runCommand(rawCommand: string) {
    const command = rawCommand.trim().toLowerCase();
    if (!command) return;

    if (command === "clear") {
      setHistory([]);
      setInput("");
      return;
    }

    const response = commandResponses[command] ?? [
      `command not available: ${command}`,
      "type 'help' to view this public demo's fixed commands.",
    ];

    setHistory(current => [...current, { command, response }]);
    setInput("");
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    runCommand(input);
  }

  return (
    <div className="terminal-console" aria-label="Interactive portfolio terminal">
      <div className="terminal-topbar">
        <div className="terminal-title"><span className="terminal-orb" /> KB // SIGNAL CONSOLE</div>
        <span className="terminal-state">DEMO / NO EXECUTION</span>
      </div>
      <div className="terminal-status"><span>STATUS</span><TypewriterStatus /></div>
      <div className="terminal-output" ref={outputRef} aria-live="polite">
        {history.map((entry, index) => (
          <div className="terminal-entry" key={`${entry.command}-${index}`}>
            <p><span className="terminal-prompt">kb@itahari:~$</span> {entry.command}</p>
            {entry.response.map(line => <p className="terminal-response" key={line}>{line}</p>)}
          </div>
        ))}
      </div>
      <div className="terminal-shortcuts" aria-label="Terminal command shortcuts">
        {["help", "whoami", "focus", "contact"].map(command => (
          <button key={command} type="button" onClick={() => runCommand(command)}>{command}</button>
        ))}
      </div>
      <form className="terminal-input-row" onSubmit={handleSubmit}>
        <label htmlFor="signal-command" className="terminal-prompt">kb@itahari:~$</label>
        <input
          id="signal-command"
          value={input}
          onChange={event => setInput(event.target.value)}
          placeholder="type help"
          autoComplete="off"
          spellCheck="false"
        />
        <button type="submit">RUN</button>
      </form>
    </div>
  );
}
