import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { createTicket } from "../api/ticketApi";

export default function CreateTicket() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");

  const [description, setDescription] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await createTicket({
        title,
        description,
      });

      navigate("/");
    } catch (error) {
      console.error(error);

      alert("Failed to create ticket");
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-2xl mx-auto bg-slate-900 p-8 rounded-2xl shadow-lg border border-slate-800">
        <h1 className="text-4xl font-bold mb-2">Create Ticket</h1>

        <p className="text-slate-400 mb-8">
          AI will automatically classify and route your issue
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block mb-2 font-semibold">Title</label>

            <input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full p-3 rounded-xl bg-slate-800 border border-slate-700 focus:outline-none focus:border-blue-500"
              placeholder="VPN Issue"
            />
          </div>

          <div>
            <label className="block mb-2 font-semibold">Description</label>

            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full p-3 rounded-xl bg-slate-800 border border-slate-700 h-40 focus:outline-none focus:border-blue-500"
              placeholder="Describe the issue..."
            />
          </div>

          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 transition px-6 py-3 rounded-xl font-bold shadow-lg"
          >
            Create Ticket
          </button>
        </form>
      </div>
    </div>
  );
}
