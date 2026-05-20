import { useEffect, useState, useRef } from "react";

import { useParams } from "react-router-dom";

import {
  getMessages,
  addMessage,
  generateAIResponse,
  getWorkflowLogs,
} from "../api/chatApi";

import { getTicket } from "../api/ticketApi";

export default function TicketDetails() {
  const { id } = useParams();

  const [ticket, setTicket] = useState(null);

  const [messages, setMessages] = useState([]);

  const [logs, setLogs] = useState([]);

  const [message, setMessage] = useState("");

  const [loadingAI, setLoadingAI] = useState(false);

  // ==========================================
  // AUTO SCROLL REFS
  // ==========================================

  const messagesEndRef = useRef(null);

  const logsEndRef = useRef(null);

  // ==========================================
  // FETCH INITIAL DATA
  // ==========================================

  useEffect(() => {
    fetchData();
  }, []);

  // ==========================================
  // AUTO SCROLL MESSAGES
  // ==========================================

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loadingAI]);

  // ==========================================
  // AUTO SCROLL LOGS
  // ==========================================

  useEffect(() => {
    logsEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [logs]);

  // ==========================================
  // FETCH DATA
  // ==========================================

  const fetchData = async () => {
    try {
      const ticketData = await getTicket(id);

      const msgs = await getMessages(id);

      const workflowLogs = await getWorkflowLogs(id);

      setTicket(ticketData);

      setMessages(msgs);

      setLogs(workflowLogs);
    } catch (error) {
      console.error(error);
    }
  };

  // ==========================================
  // SEND MESSAGE + AUTO AI REPLY
  // ==========================================

  const handleSendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    try {
      // CLEAR INPUT
      setMessage("");

      // STORE USER MESSAGE
      await addMessage(id, {
        sender: "user",
        message: userMessage,
      });

      // REFRESH USER MESSAGE
      await fetchData();

      // SHOW AI LOADING
      setLoadingAI(true);

      // GENERATE AI RESPONSE
      const aiResponse = await generateAIResponse(userMessage);

      // STORE AI RESPONSE
      await addMessage(id, {
        sender: "ai",
        message: aiResponse.answer,
      });

      // FINAL REFRESH
      await fetchData();
    } catch (error) {
      console.error(error);
    } finally {
      setLoadingAI(false);
    }
  };

  // ==========================================
  // ENTER KEY SUPPORT
  // ==========================================

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      handleSendMessage();
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-7xl mx-auto">
        {/* ================================== */}
        {/* HEADER */}
        {/* ================================== */}

        <div className="mb-8">
          <h1 className="text-4xl font-bold">Ticket #{id}</h1>

          <p className="text-slate-400 mt-2">
            AI-powered enterprise support workflow
          </p>
        </div>

        {/* ================================== */}
        {/* TICKET INFO */}
        {/* ================================== */}

        {ticket && (
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg mb-8">
            <h2 className="text-2xl font-bold mb-3">{ticket.title}</h2>

            <p className="text-slate-300 mb-6">{ticket.description}</p>

            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="bg-slate-800 p-4 rounded-xl">
                <p className="text-slate-400 text-sm mb-1">Status</p>

                <p className="font-bold">{ticket.status}</p>
              </div>

              <div className="bg-slate-800 p-4 rounded-xl">
                <p className="text-slate-400 text-sm mb-1">Priority</p>

                <p className="font-bold text-blue-400">{ticket.priority}</p>
              </div>

              <div className="bg-slate-800 p-4 rounded-xl">
                <p className="text-slate-400 text-sm mb-1">Category</p>

                <p className="font-bold">{ticket.category}</p>
              </div>

              <div className="bg-slate-800 p-4 rounded-xl">
                <p className="text-slate-400 text-sm mb-1">Department</p>

                <p className="font-bold">{ticket.department}</p>
              </div>
            </div>
          </div>
        )}

        {/* ================================== */}
        {/* MAIN GRID */}
        {/* ================================== */}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* ================================== */}
          {/* CONVERSATION */}
          {/* ================================== */}

          <div className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg flex flex-col h-200">
            <h2 className="text-2xl font-bold mb-6">Conversation</h2>

            {/* ============================== */}
            {/* MESSAGE AREA */}
            {/* ============================== */}

            <div className="flex-1 overflow-y-auto space-y-4 pr-2">
              {messages.map((msg) => (
                <div
                  key={msg.id}
                  className={`flex ${
                    msg.sender === "user" ? "justify-end" : "justify-start"
                  }`}
                >
                  <div
                    className={`max-w-[75%] p-4 rounded-2xl shadow ${
                      msg.sender === "ai" ? "bg-blue-700" : "bg-slate-800"
                    }`}
                  >
                    <p className="font-bold uppercase text-xs tracking-wider mb-2 opacity-80">
                      {msg.sender}
                    </p>

                    <p className="whitespace-pre-wrap leading-relaxed">
                      {msg.message}
                    </p>
                  </div>
                </div>
              ))}

              {/* ========================== */}
              {/* AI LOADING BUBBLE */}
              {/* ========================== */}

              {loadingAI && (
                <div className="flex justify-start">
                  <div className="max-w-[75%] p-4 rounded-2xl shadow bg-blue-700">
                    <p className="font-bold uppercase text-xs tracking-wider mb-2 opacity-80">
                      ai
                    </p>

                    <p className="animate-pulse">Thinking...</p>
                  </div>
                </div>
              )}

              {/* AUTO SCROLL TARGET */}

              <div ref={messagesEndRef} />
            </div>

            {/* ============================== */}
            {/* INPUT */}
            {/* ============================== */}

            <div className="mt-6 flex gap-3">
              <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={handleKeyDown}
                rows="2"
                className="flex-1 p-4 rounded-xl bg-slate-800 border border-slate-700 text-white resize-none focus:outline-none focus:border-blue-500"
                placeholder="Type your message..."
              />

              <button
                onClick={handleSendMessage}
                disabled={loadingAI}
                className="bg-green-600 hover:bg-green-700 transition px-6 rounded-xl font-semibold disabled:opacity-50"
              >
                Send
              </button>
            </div>
          </div>

          {/* ================================== */}
          {/* WORKFLOW LOGS */}
          {/* ================================== */}

          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg flex flex-col h-200">
            <h2 className="text-2xl font-bold mb-6">Workflow Logs</h2>

            <div className="flex-1 overflow-y-auto space-y-4 pr-2">
              {logs.map((log) => (
                <div
                  key={log.id}
                  className="bg-slate-800 border border-slate-700 p-3 rounded-xl"
                >
                  <div className="flex justify-between items-center mb-2">
                    <p className="font-bold text-blue-400">{log.action}</p>
                  </div>

                  <p className="text-slate-300 text-sm">{log.details}</p>
                </div>
              ))}

              {/* AUTO SCROLL TARGET */}

              <div ref={logsEndRef} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
