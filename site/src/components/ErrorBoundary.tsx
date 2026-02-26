"use client";

import { Component, type ReactNode } from "react";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
}

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(): State {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex items-center justify-center h-screen bg-background text-center px-6">
          <div>
            <h2 className="gta-title text-3xl sm:text-5xl mb-4">Oops</h2>
            <p className="text-foreground/50 text-sm sm:text-base mb-8">
              Quelque chose s&apos;est mal pass&eacute;. Rechargez la page pour continuer.
            </p>
            <button
              onClick={() => window.location.reload()}
              className="px-8 py-3 border border-pink/40 rounded-full text-pink tracking-[0.15em] uppercase text-sm
                         hover:bg-pink/10 transition-all duration-300 cursor-pointer"
            >
              Recharger
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
