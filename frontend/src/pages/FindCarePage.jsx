import { useEffect, useState } from 'react'
import { getProviders } from '../services/careService'

export default function FindCarePage() {
  const [filters, setFilters] = useState({ specialty: '', location: '', visit_type: '', cost: '' })
  const [providers, setProviders] = useState([])
  const [error, setError] = useState('')
  useEffect(() => { getProviders(filters).then(setProviders).catch(() => setError('Unable to load care providers.')) }, [filters])
  const update = (key, value) => setFilters((current) => ({ ...current, [key]: value }))
  return <main className="screen"><div className="prototype-banner"><strong>Prototype sample data only.</strong> Not a verified directory.</div><div className="page-heading"><div><p className="eyebrow">CARE NEAR YOU</p><h1>Find care</h1><p>Search providers and services that fit your needs.</p></div></div><div className="care-filters">{[['specialty', 'Specialty'], ['location', 'Location'], ['visit_type', 'Visit type'], ['cost', 'Cost']].map(([key, label]) => <label key={key}>{label}<select value={filters[key]} onChange={(event) => update(key, event.target.value)}><option value="">[select {label.toLowerCase()}]</option><option value="primary">Primary care</option><option value="specialist">Specialist</option><option value="local">Local</option><option value="verify">Verify with provider</option></select></label>)}</div>{error && <p className="error-text" role="alert">{error}</p>}<div className="providers">{providers.map((provider) => <article className="provider-card" key={provider.id}><span className="prototype-chip">Prototype</span><p className="eyebrow">{provider.specialty}</p><h3>{provider.name}</h3><p>{provider.location} · {provider.visit_type}</p><button className="btn btn-secondary">View details</button></article>)}</div></main>
}
