import { useState, useEffect, useRef } from "react";
import axios from "axios";
import MessageBubble from "./MessageBubble";

export default function ChatBox() {
  const [msgs, setMsgs] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const endRef = useRef();

  // Auto scroll
  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [msgs, loading]);

  const send = async () => {
    if (!input.trim() || loading) return;

    setLoading(true);

    // Add user message
    setMsgs((prev) => [...prev, { type: "user", text: input }]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/query", {
        query: input,
      });

      setMsgs((prev) => [
        ...prev,
        { type: "bot", text: res.data.response },
      ]);
    } catch (err) {
      setMsgs((prev) => [
        ...prev,
        { type: "bot", text: "❌ Error connecting to server" },
      ]);
    }

    setInput("");
    setLoading(false);
  };

  const upload = async (file) => {
    if (!file) return;

    const fd = new FormData();
    fd.append("file", file);

    try {
      await axios.post("http://127.0.0.1:8000/upload-pdf", fd);

      setMsgs((prev) => [
        ...prev,
        { type: "bot", text: "✅ PDF uploaded successfully" },
      ]);
    } catch {
      setMsgs((prev) => [
        ...prev,
        { type: "bot", text: "❌ PDF upload failed" },
      ]);
    }
  };

  return (
    <div className="chat">
      {/* Upload */}
      <div className="upload">
        <input type="file" onChange={(e) => upload(e.target.files[0])} />
      </div>

      {/* Chat window */}
      <div className="window">
        {msgs.map((m, i) => (
          <MessageBubble key={i} msg={m} />
        ))}

        {/* Thinking indicator */}
        {loading && <div className="bubble bot">Thinking...</div>}

        <div ref={endRef}></div>
      </div>

      {/* Input */}
      <div className="input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
        />

        <button onClick={send} disabled={loading}>
          {loading ? "..." : "Send"}
        </button>
      </div>
    </div>
  );
}