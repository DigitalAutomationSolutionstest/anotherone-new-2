'use client'

import { Metadata } from 'next/types'
import { Hero } from '@/components/Hero'
import { Features } from '@/components/Features'
import { Pricing } from '@/components/Pricing'
import { Testimonials } from '@/components/Testimonials'
import { FAQ } from '@/components/FAQ'
import { CTA } from '@/components/CTA'
import { Card } from '@/components/Card'
import Footer from '@/components/Footer'
import CustomServicesSection from '@/components/CustomServicesSection'
import TestimonialsCarousel from '@/components/TestimonialsCarousel'

export const metadata: Metadata = {
  title: 'Mini AI Apps - Soluzioni AI e Web Personalizzate',
  description: 'Mini App AI potenti e progetti web personalizzati per la tua azienda. Automazione, efficienza e innovazione.',
}

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      <Hero 
        title="L'intelligenza artificiale o il sito dei tuoi sogni, creati su misura per te."
        subtitle="Mini App AI potenti + Progetti Web e AI personalizzati."
      />
      <CustomServicesSection />
      <TestimonialsCarousel />
      <Footer />
    </div>
  )
}
