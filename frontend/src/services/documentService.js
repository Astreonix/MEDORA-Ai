import { api } from './api'
export const getDocuments = async () => (await api.get('/api/v1/documents')).data
export const getDocument = async (id) => (await api.get(`/api/v1/documents/${id}`)).data
export const getDocumentStatus = async (id) => (await api.get(`/api/v1/documents/${id}/status`)).data
export async function uploadDocuments(files) {
  const body = new FormData()
  files.forEach((file) => body.append('files', file))
  return (await api.post('/api/v1/documents/upload', body, { headers: { 'Content-Type': 'multipart/form-data' } })).data
}