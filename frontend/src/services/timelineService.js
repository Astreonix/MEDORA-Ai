import { api } from './api'
export const getTimeline = async () => (await api.get('/api/v1/timeline')).data