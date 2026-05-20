import apiClient from "./client";

export const getTickets = async () => {
  const response = await apiClient.get("/tickets");
  return response.data;
};

export const getTicket = async (id) => {
  const response = await apiClient.get(`/tickets/${id}`);
  return response.data;
};

export const createTicket = async (payload) => {
  const response = await apiClient.post("/tickets", payload);

  return response.data;
};

export const updateTicketStatus = async (id, payload) => {
  const response = await apiClient.patch(`/tickets/${id}/status`, payload);

  return response.data;
};
