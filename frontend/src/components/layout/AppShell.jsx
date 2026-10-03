import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Sidebar from './Sidebar'
import Navbar from './Navbar'
export default function AppShell() { const [open, setOpen] = useState(false); return <div className="app-shell"><div className={open ? 'sidebar-overlay show' : 'sidebar-overlay'} onClick={() => setOpen(false)} /><div className={open ? 'mobile-sidebar show' : 'mobile-sidebar'}><Sidebar /></div><Sidebar /><div className="main-content"><Navbar onMenu={() => setOpen(true)} /><Outlet /></div></div> }