export default function Modal({ open, title, children, onClose }) {
  if (!open) return null
  return <div className="modal-backdrop" role="presentation" onClick={onClose}><section className="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" onClick={(event) => event.stopPropagation()}><div className="modal-header"><h2 id="modal-title">{title}</h2><button type="button" onClick={onClose} aria-label="Close dialog">×</button></div>{children}</section></div>
}