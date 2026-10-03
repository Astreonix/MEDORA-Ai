import { createContext, useContext, useState } from 'react'
export const LanguageContext = createContext(null)
export function LanguageProvider({ children }) { const [language, setLanguage] = useState('English'); return <LanguageContext.Provider value={{ language, setLanguage }}>{children}</LanguageContext.Provider> }
export function useLanguage() { return useContext(LanguageContext) }