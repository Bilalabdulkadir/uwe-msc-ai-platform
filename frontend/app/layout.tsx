import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'UWE MSc AI Platform',
  description: 'Community platform for AI students and researchers.'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
