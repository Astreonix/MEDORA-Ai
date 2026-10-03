import Icon from '../common/Icon'
export default function UploadDropzone({ files = [], onChange }) {
  return <label className="dropzone"><input type="file" multiple onChange={(event) => onChange?.(Array.from(event.target.files || []))} /><span className="drop-icon"><Icon name="upload" /></span><strong>{files.length ? `${files.length} file(s) selected` : 'Drop your reports here'}</strong><span>or click to browse</span><small>PDF, JPG or PNG up to 20 MB</small></label>
}