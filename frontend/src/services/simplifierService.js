import { api } from './api'
export const simplify = async (text, language = 'English') =>
  (await api.post('/api/v1/simplifier/explain', { text, language })).data