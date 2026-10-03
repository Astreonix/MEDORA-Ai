import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ConfidenceBadge from '../components/common/ConfidenceBadge'
import EmergencyNotice from '../components/common/EmergencyNotice'
import { getDocument } from '../services/documentService'

export default function DocumentDetailPage() {
  const { documentId } = useParams()
  const [document, setDocument] = useState(null)
  const [error, setError] = useState('')
  useEffect(() => { getDocument(documentId).then(setDocument).catch(() => setError('Unable to load this document.')) }, [documentId])
  return <main className="screen"><div className="page-heading"><div><p className="eyebrow">DOCUMENT {documentId}</p><h1>{document?.title || '[document]'}</h1><p>{document ? `${new Date(document.created_at).toLocaleDateString()} · ${document.document_type}` : '[date] · [document type]'}</p></div><span className="status-chip">{document?.processing_status || 'Loading'}</span></div>{error && <p className="error-text" role="alert">{error}</p>}<div className="detail-grid"><div className="document-preview"><div className="paper"><span>MEDICAL DOCUMENT</span><h2>{document?.filename || '[provider name]'}</h2><hr /><pre>{document?.extracted_text || 'Document text will appear here after processing.'}</pre></div></div><section className="card extracted"><p className="eyebrow">EXTRACTED DETAILS</p>{[['Date','[date]'],['Provider','[provider name]'],['Medication','[medication]'],['Lab value','[lab value]']].map(([label, value], i) => <div className="field-row" key={label}><span>{label}</span><strong>{value}</strong><ConfidenceBadge low={i === 3} value={i === 3 ? 'Review' : 'High confidence'} /></div>)}<EmergencyNotice /></section></div></main>
}
