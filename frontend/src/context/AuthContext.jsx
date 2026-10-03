import { createContext, useContext, useMemo, useState } from 'react'
import { login, register } from '../services/authService'
const AuthContext = createContext(null)
export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => JSON.parse(localStorage.getItem('medora-user') || 'null'))
  const signIn = async (credentials) => { const result = await login(credentials); const next = result.user; localStorage.setItem('medora-user', JSON.stringify(next)); if (result.token) localStorage.setItem('medora-token', result.token); setUser(next); return next }
  const signUp = async (details) => { const result = await register(details); const next = result.user; localStorage.setItem('medora-user', JSON.stringify(next)); if (result.token) localStorage.setItem('medora-token', result.token); setUser(next); return next }
  const signOut = () => { localStorage.removeItem('medora-user'); localStorage.removeItem('medora-token'); setUser(null) }
  return <AuthContext.Provider value={useMemo(() => ({ user, signIn, signUp, signOut }), [user])}>{children}</AuthContext.Provider>
}
export function useAuth() { return useContext(AuthContext) }