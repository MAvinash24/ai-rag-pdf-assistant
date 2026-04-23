export default function MessageBubble({ msg }) {
  return <div className={`bubble ${msg.type}`}>{msg.text}</div>;
}