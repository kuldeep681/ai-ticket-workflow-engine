import { BrowserRouter, Routes, Route } from "react-router-dom";

import CreateTicket from "./pages/CreateTicket";
import Dashboard from "./pages/Dashboard";
import TicketDetails from "./pages/TicketDetails";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />

        <Route path="/create-ticket" element={<CreateTicket />} />

        <Route path="/tickets/:id" element={<TicketDetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
