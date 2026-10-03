import { api } from './api'
export const getDoctorBrief = async () => (await api.post('/api/v1/brief/generate')).data