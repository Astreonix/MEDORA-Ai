import { api } from './api'
export const askMedora = async (question, language = 'English', sessionId = null) =>
  (await api.post('/api/v1/chat/ask', { question, language, session_id: sessionId })).data