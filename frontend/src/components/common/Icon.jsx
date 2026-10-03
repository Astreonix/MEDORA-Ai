const paths = {
  home: 'M3 10.5 12 3l9 7.5M5 9v11h14V9M9 20v-6h6v6',
  upload: 'M12 16V4m0 0L7 9m5-5 5 5M4 20h16',
  docs: 'M6 3h9l3 3v15H6zM9 12h6M9 16h6M14 3v4h4',
  timeline: 'M5 4v16M5 7h8M5 12h11M5 17h7',
  spark: 'm12 3 1.5 6.5L20 11l-6.5 1.5L12 19l-1.5-6.5L4 11l6.5-1.5z',
  simplify: 'M4 6h16M4 12h10M4 18h7',
  brief: 'M5 4h14v16H5zM8 8h8M8 12h8M8 16h5',
  care: 'M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11zM12 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
  arrow: 'M4 12h16m-6-6 6 6-6 6',
  menu: 'M4 7h16M4 12h16M4 17h16',
  chevron: 'm9 6 6 6-6 6',
}
export default function Icon({ name, size = 18 }) { return <svg aria-hidden="true" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={paths[name] || paths.docs} /></svg> }
