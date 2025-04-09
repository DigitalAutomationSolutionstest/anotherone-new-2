import React from 'react'
import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <Link href="/" className="flex items-center">
              <span className="text-xl font-bold text-primary">
                Digital Automaton Solutions
              </span>
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            <Link href="/app/dashboard" className="text-gray-700 hover:text-primary">
              Dashboard
            </Link>
            <Link href="/app/feedback" className="text-gray-700 hover:text-primary">
              Feedback
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
} 