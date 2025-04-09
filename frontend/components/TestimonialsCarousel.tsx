'use client'

import { useState } from 'react'
import { Card } from '@/components/ui/card'
import { Button } from '@/components/ui/button'

const testimonials = [
  {
    content: "Mini AI Apps ha rivoluzionato il modo in cui gestiamo i nostri processi aziendali. L'automazione con l'AI ci ha fatto risparmiare ore di lavoro.",
    author: "Marco Rossi",
    role: "CEO, Tech Solutions",
  },
  {
    content: "Il sito web che hanno creato per noi è moderno, veloce e perfettamente ottimizzato per il mobile. Ottimo lavoro!",
    author: "Laura Bianchi",
    role: "Marketing Manager, Innovazione Spa",
  },
  {
    content: "La loro competenza in ambito AI è impressionante. Hanno creato una soluzione personalizzata che si adatta perfettamente alle nostre esigenze.",
    author: "Giuseppe Verdi",
    role: "CTO, Digital Enterprise",
  },
]

export default function TestimonialsCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)

  const next = () => {
    setCurrentIndex((current) => (current + 1) % testimonials.length)
  }

  const previous = () => {
    setCurrentIndex((current) => (current - 1 + testimonials.length) % testimonials.length)
  }

  return (
    <section className="py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Cosa dicono i nostri clienti
          </h2>
          <p className="mt-6 text-lg leading-8 text-muted-foreground">
            Scopri le esperienze di chi ha scelto Mini AI Apps per le proprie soluzioni digitali.
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl">
          <Card className="p-8">
            <blockquote className="text-lg font-semibold leading-8">
              "{testimonials[currentIndex].content}"
            </blockquote>
            <div className="mt-6">
              <p className="text-base font-semibold">{testimonials[currentIndex].author}</p>
              <p className="text-sm text-muted-foreground">{testimonials[currentIndex].role}</p>
            </div>
          </Card>
          <div className="mt-6 flex justify-center gap-4">
            <Button variant="outline" onClick={previous}>
              Precedente
            </Button>
            <Button onClick={next}>
              Successivo
            </Button>
          </div>
        </div>
      </div>
    </section>
  )
} 