/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        deepTeal: '#0A3F3B',
        teal: '#0F766E',
        brightMint: '#2DD4BF',
        mintWash: '#D7F0EA',
        ground: '#F5F9F8',
        ink: '#0B2B2A',
        muted: '#4A6361',
        border: '#D5E4E1',
        warning: '#F6B63C',
        warningBox: '#FFF4D6',
        prototype: '#E8E4F8',
        prototypeText: '#352A74',
      },
      fontFamily: {
        sora: ['Sora', 'sans-serif'],
        dm: ['DM Sans', 'sans-serif'],
      },
      borderRadius: {
        card: '18px',
        panel: '22px',
      },
    },
  },
  plugins: [],
}