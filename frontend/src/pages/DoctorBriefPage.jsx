import { useEffect, useState } from 'react'
import Button from '../components/common/Button'
import { getDoctorBrief } from '../services/briefService'

const sections = [['documented_conditions', 'Documented conditions'], ['current_medications', 'Current medications'], ['recent_tests', 'Recent tests'], ['important_events', 'Important events']]

export default function DoctorBriefPage() {
  const [brief, setBrief] = useState(null)
  const [error, setError] = useState('')
  useEffect(() => { getDoctorBrief().then(setBrief).catch(() => setError('Unable to generate your doctor brief.')) }, [])
  return <main className="screen"><div className="page-heading"><div><p className="eyebrow">READY FOR YOUR NEXT VISIT?</p><h1>Doctor Brief</h1><p>A focused summary you can share with your care team.</p></div><div className="heading-actions"><Button variant="secondary" onClick={() => window.print()}>Print</Button><Button onClick={() => window.print()}>Download PDF</Button></div></div>{error && <p className="error-text" role="alert">{error}</p>}<article className="brief-paper"><div className="brief-title"><div><span>MEDORA</span><h2>Patient health brief</h2><p>Prepared for: [patient name] · [date]</p></div><span className="status-chip">{brief ? 'READY TO REVIEW' : 'LOADING'}</span></div>{sections.map(([key, label]) => <section className="brief-section" key={key}><p className="eyebrow">{label}</p><h3>{brief?.[key]?.join(', ') || '[documented information]'}</h3>{brief?.sources?.[0] && <span className="source-chip">Source: {brief.sources[0]}</span>}</section>)}<section className="brief-section"><p className="eyebrow">Latest available report</p><h3>{brief?.latest_available_report || '[latest available report]'}</h3></section><div className="warning-box"><strong>Missing or uncertain</strong><span>{brief?.uncertain_items?.join(' ') || 'Some information needs confirmation against the original.'}</span></div></article></main>
}
