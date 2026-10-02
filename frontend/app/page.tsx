const stats = [
  { title: 'Projects', value: '14' },
  { title: 'Events', value: '6' },
  { title: 'Resources', value: '27' },
  { title: 'Discussions', value: '42' }
]

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-slate-950 p-8 text-white">
      <div className="mx-auto max-w-6xl">
        <h1 className="mb-8 text-4xl font-bold">Dashboard</h1>

        <div className="mb-10 grid gap-4 md:grid-cols-4">
          {stats.map((item) => (
            <div key={item.title} className="rounded-xl border border-slate-800 bg-slate-900 p-5">
              <p className="text-sm text-slate-400">{item.title}</p>
              <p className="mt-2 text-3xl font-bold">{item.value}</p>
            </div>
          ))}
        </div>

        <div className="grid gap-6 lg:grid-cols-2">
          <section className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="mb-4 text-xl font-semibold">Upcoming Events</h2>
            <ul className="space-y-3 text-slate-300">
              <li>• AI Seminar: Responsible AI</li>
              <li>• Machine Learning Lab Night</li>
              <li>• Research Showcase</li>
            </ul>
          </section>

          <section className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="mb-4 text-xl font-semibold">Featured Projects</h2>
            <ul className="space-y-3 text-slate-300">
              <li>• Smart Campus Analytics</li>
              <li>• NLP for Student Support</li>
              <li>• Computer Vision for Sustainability</li>
            </ul>
          </section>
        </div>
      </div>
    </main>
  )
}
