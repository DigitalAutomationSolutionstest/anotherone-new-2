import React from 'react'

export default function Footer() {
  return (
    <footer className="bg-gray-50 border-t">
      <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <p className="text-gray-500">
            © {new Date().getFullYear()} Digital Automaton Solutions. Tutti i diritti riservati.
          </p>
        </div>
      </div>
    </footer>
  )
} 