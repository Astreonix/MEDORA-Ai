import { useContext } from 'react'
import { LanguageContext } from '../context/LanguageContext'
export default function useLanguage() { return useContext(LanguageContext) }