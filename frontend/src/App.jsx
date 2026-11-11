
import './App.css'

function App() {
  return (
    <main className="portfolio">
      <div className="portfolio-background">
        <div className="glow glow-cyan"></div>
        <div className="glow glow-purple"></div>
        <div className="background-grid"></div>
      </div>

      <div className="portfolio-content">
        <header className="site-header">
          <a href="#home" className="brand">
            <span className="brand-symbol">B.</span>
            <span>BRITNEY<span className="brand-accent">.DEV</span></span>
          </a>

          <nav className="main-navigation">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
          </nav>

          <a href="#contact" className="header-contact">
            Let's connect <span>↗</span>
          </a>
        </header>

        <section className="hero-section" id="home">
          <div className="hero-copy">
            <div className="availability">
              <span className="availability-dot"></span>
              SOFTWARE DEVELOPER / INFORMATION SYSTEMS
            </div>

            <p className="hero-intro">Hello, world! I'm</p>

            <h1>
              Britney
              <span className="hero-lastname">Norman.</span>
            </h1>

            <div className="hero-description">
              <span className="description-line"></span>
              <p>
                I build digital experiences where
                <strong> technology meets creativity.</strong>
                <br />
                Exploring full-stack development, intelligent
                systems and meaningful solutions.
              </p>
            </div>

            <div className="hero-actions">
              <a href="#projects" className="primary-button">
                Explore my work <span>↗</span>
              </a>

              <a href="#about" className="secondary-button">
                Discover my story
              </a>
            </div>

            <div className="hero-index">
              <span>01 / 06</span>
              <span>INDEPENDENT THINKER. DIGITAL BUILDER.</span>
            </div>
          </div>

          <div className="hero-visual">
            <div className="visual-placeholder">
              <span className="visual-orbit orbit-one"></span>
              <span className="visual-orbit orbit-two"></span>

              <div className="visual-center">
                <span className="visual-initial">B</span>
                <span className="visual-caption">
                  THE DEVELOPER UNIVERSE
                </span>
              </div>

              <div className="floating-label label-top">
                <span>01</span> CREATIVE MIND
              </div>

              <div className="floating-label label-bottom">
                <span>02</span> BUILDING THE FUTURE
              </div>
            </div>

            <div className="visual-coordinate">
              <span>COORDINATES</span>
              <span>DS / TZ</span>
            </div>
          </div>
        </section>

        <footer className="hero-footer">
          <span>DESIGNED TO THINK DIFFERENTLY.</span>
          <span>SCROLL TO EXPLORE ↓</span>
          <span>© 2026 BRITNEY NORMAN</span>
        </footer>
      </div>
    </main>
  )
}

export default App
