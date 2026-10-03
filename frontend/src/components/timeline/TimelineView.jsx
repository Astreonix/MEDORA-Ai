import Card from '../common/Card'
import TimelineEvent from './TimelineEvent'
export default function TimelineView({ events = [] }) { return <Card className="timeline-panel"><div className="timeline-list">{events.map((event, index) => <TimelineEvent event={event} uncertain={index === 1} key={`${event.date}-${index}`} />)}</div></Card> }