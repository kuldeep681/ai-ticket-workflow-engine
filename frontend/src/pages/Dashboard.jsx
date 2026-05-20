import { useEffect, useState } from "react";

import { getTickets } from "../api/ticketApi";

import { Link } from "react-router-dom";

export default function Dashboard() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    fetchTickets();
  }, []);

  const fetchTickets = async () => {
    try {
      const data = await getTickets();

      setTickets(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex justify-between items-center mb-10">
          <div>
            <h1 className="text-4xl font-bold">AI Ticket Dashboard</h1>

            <p className="text-slate-400 mt-2">
              Intelligent AI-powered enterprise ticket workflow
            </p>
          </div>

          <Link to="/create-ticket">
            <button className="bg-blue-600 hover:bg-blue-700 transition px-6 py-3 rounded-xl font-semibold shadow-lg">
              + Create Ticket
            </button>
          </Link>
        </div>

        <div className="space-y-5">
          {tickets.length === 0 ? (
            <div className="bg-slate-900 border border-slate-800 p-10 rounded-2xl text-center text-slate-400">
              No tickets found
            </div>
          ) : (
            tickets.map((ticket) => (
              <Link key={ticket.id} to={`/tickets/${ticket.id}`}>
                <div className="bg-slate-900 border border-slate-800 hover:border-blue-500 transition p-6 rounded-2xl shadow-lg mb-4">
                  <div className="flex justify-between items-start">
                    <div className="flex-1">
                      <h2 className="text-2xl font-bold mb-2">
                        {ticket.title}
                      </h2>

                      <p className="text-slate-300 mb-4">
                        {ticket.description}
                      </p>

                      <div className="grid grid-cols-2 gap-3 text-sm">
                        <div className="bg-slate-800 px-3 py-2 rounded-lg">
                          <span className="text-slate-400">Category:</span>{" "}
                          {ticket.category}
                        </div>

                        <div className="bg-slate-800 px-3 py-2 rounded-lg">
                          <span className="text-slate-400">Department:</span>{" "}
                          {ticket.department}
                        </div>
                      </div>
                    </div>

                    <div className="text-right ml-6">
                      <div className="bg-slate-800 px-3 py-1 rounded-lg text-sm mb-2">
                        {ticket.status}
                      </div>

                      <div className="text-sm font-semibold text-blue-400">
                        {ticket.priority} Priority
                      </div>
                    </div>
                  </div>
                </div>
              </Link>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
