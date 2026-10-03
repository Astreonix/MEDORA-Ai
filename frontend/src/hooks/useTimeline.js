import { useEffect, useState } from 'react'
import { getTimeline } from '../services/timelineService'
export default function useTimeline() { const [events, setEvents] = useState([]); const [loading, setLoading] = useState(true); useEffect(() => { getTimeline().then(setEvents).finally(() => setLoading(false)) }, []); return { events, loading } }