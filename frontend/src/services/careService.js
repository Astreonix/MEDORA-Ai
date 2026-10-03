import { api } from './api'
export const getProviders = async (params = {}) => (await api.get('/api/v1/care/search', { params })).data