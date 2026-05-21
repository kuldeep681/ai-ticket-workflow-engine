import apiClient from "./client";

export const getMessages = async (ticketId) => {
  const response = await apiClient.get(`/tickets/${ticketId}/messages`);

  return response.data;
};

export const addMessage = async (ticketId, payload) => {
  const response = await apiClient.post(
    `/tickets/${ticketId}/messages`,
    payload,
  );

  return response.data;
};

export const generateAIResponse = async (ticketId, question) => {
  const response = await apiClient.post("/rag/query", {
    ticket_id: Number(ticketId),
    question,
  });

  return response.data;
};

export const getWorkflowLogs = async (ticketId) => {
  const response = await apiClient.get(`/tickets/${ticketId}/logs`);

  return response.data;
};
