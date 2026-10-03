import { ACCEPTED_FILE_TYPES, MAX_UPLOAD_SIZE } from './constants'

export function validateFile(file) {
  if (!file) return { valid: false, error: 'Please choose a file.' }
  if (!ACCEPTED_FILE_TYPES.includes(file.type)) return { valid: false, error: 'Use a PDF, JPG or PNG file.' }
  if (file.size > MAX_UPLOAD_SIZE) return { valid: false, error: 'Files must be 20 MB or smaller.' }
  return { valid: true, error: '' }
}

export function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

export function validatePassword(password) {
  return typeof password === 'string' && password.length >= 6
}