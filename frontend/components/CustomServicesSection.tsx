'use client'

import { Card } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import Link from 'next/link'

const services = [
  {
    title: 'Mini App AI',
    description: 'Applicazioni AI personalizzate per automatizzare i tuoi processi aziendali.',
    href: '/services#mini-app',
  },
  {
    title: 'Siti Web',
    description: 'Siti web moderni e responsive per la tua presenza online.',
    href: '/services#web',
  },
  {
    title: 'Progetti Custom',
    description: 'Soluzioni su misura per le tue esigenze specifiche.',
    href: '/services#custom',
  },
]

export default function CustomServicesSection() {
  return (
    <section className="py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Servizi Personalizzati
          </h2>
          <p className="mt-6 text-lg leading-8 text-muted-foreground">
            Scegli il servizio più adatto alle tue esigenze o contattaci per una soluzione su misura.
          </p>
        </div>
        <div className="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-6 sm:mt-20 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          {services.map((service) => (
            <Card key={service.title} className="p-6">
              <h3 className="text-xl font-semibold">{service.title}</h3>
              <p className="mt-2 text-muted-foreground">{service.description}</p>
              <Button asChild className="mt-4">
                <Link href={service.href}>Scopri di più</Link>
              </Button>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
} 