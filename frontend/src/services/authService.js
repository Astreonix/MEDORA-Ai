import { api } from './api'

export async function login(credentials) {
  const { data } = await api.post('/api/v1/auth/login', credentials)
  return data
}
export async function register(details) {
  const { data } = await api.post('/api/v1/auth/register', details)
  return data
}