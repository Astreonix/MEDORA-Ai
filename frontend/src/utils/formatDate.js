export function formatDate(value) {
  if (!value || /^\[.*\]$/.test(value)) return value || '[date]'
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) return value
  return new Intl.DateTimeFormat('en', { month: 'short', day: 'numeric', year: 'numeric' }).format(date)
}