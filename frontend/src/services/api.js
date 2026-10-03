import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('medora-user')
      localStorage.removeItem('medora-token')
      window.location.assign('/login')
    }
    return Promise.reject(error)
  },
)

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('medora-token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})