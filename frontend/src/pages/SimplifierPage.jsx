import { useState } from 'react'
import Card from '../components/common/Card'
import { simplify } from '../services/simplifierService'

export default function SimplifierPage() {
  const [term, setTerm] = useState('')
  const [language, setLanguage] = useState('English')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(event) {
    event.preventDefault()
    if (!term.trim() || loading) return
    setLoading(true)
    setError('')
    try {
      setResult(await simplify(term.trim(), language))
    } catch (requestError) {
      setError(requestError.response?.data?.detail || 'Unable to simplify this text.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="screen">
      <div className="page-heading">
        <div><p className="eyebrow">MAKE IT CLEARER</p><h1>Simplifier</h1><p>Turn medical language into something easier to understand.</p></div>
        <div className="language-toggle">
          <button className={language === 'English' ? 'active' : ''} onClick={() => setLanguage('English')}>English</button>
          <button className={language === 'Roman Urdu' ? 'active' : ''} onClick={() => setLanguage('Roman Urdu')}>Roman Urdu</button>
        </div>
      </div>
      <div className="simplifier-grid">
        <Card>
          <form onSubmit={handleSubmit}>
            <label className="field-label">Paste a medical term or sentence<textarea value={term} onChange={(event) => setTerm(event.target.value)} placeholder="[medical term or sentence]" /></label>
            <button className="btn btn-primary" disabled={loading || !term.trim()}>{loading ? 'Explaining...' : 'Explain simply'}</button>
          </form>
          {error && <p className="error-text" role="alert">{error}</p>}
        </Card>
        <Card>
          <p className="eyebrow">SIMPLE EXPLANATION</p>
          <h2>{result?.simple_explanation || '[simple explanation]'}</h2>
          <p className="eyebrow">ROMAN URDU</p>
          <p className="simple-copy">{result?.roman_urdu || '[Roman Urdu explanation]'}</p>
          {result?.preserved_facts && <div className="fact-list"><p className="eyebrow">PRESERVED FACTS</p><p>{Object.values(result.preserved_facts).flat().join(', ') || 'No numeric facts detected.'}</p></div>}
          <div className="mint-note">{result?.disclaimer || 'Doses, dates, lab values and measurements never change during simplification.'}</div>
        </Card>
      </div>
    </main>
  )
}
