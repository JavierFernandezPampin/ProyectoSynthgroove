<template>
  <div class="home-shell">
    <main class="home-main">
      <section class="hero" aria-labelledby="home-title">
        <video
          class="hero-video"
          autoplay
          muted
          loop
          playsinline
          preload="auto"
          aria-hidden="true"
        >
          <source src="/videoInicio.mp4" type="video/mp4" />
        </video>
        <div class="hero-overlay"></div>
        <h1 id="home-title" class="hero-title">
          Bienvenido a la experiencia Synthgroove
        </h1>
      </section>
    </main>
  </div>
</template>
<style scoped>
.home-shell {
  flex: 1;
  display: flex;
  background: black;
  min-height: 0;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.home-main {
  flex: 1;
  display: flex;
  min-height: 0;
  padding: 0;
}

.hero {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 64vh;
  overflow: hidden;
  background: #000;
}

.hero-video {
  width: 75%;
  height: auto;
  max-height: 150%;
  object-fit: contain;
  display: block;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.25);
  pointer-events: none;
}

.hero-title {
  position: absolute;
  z-index: 1;
  margin: 0;
  max-width: 16ch;
  padding: 2rem;
  text-align: center;
  font-size: clamp(2.4rem, 6vw, 5.8rem);
  font-weight: 700;
  line-height: 0.98;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #f7f1e8;
  text-wrap: balance;
  text-shadow: 0 4px 26px rgba(0, 0, 0, 0.55);
}

@media (max-width: 720px) {
  .hero-video {
    width: 200%;
    height: auto;
    object-fit: contain;
    display: block;
  }
  .hero-title {
    padding: 1.5rem;
    letter-spacing: 0.05em;
  }
}
</style>
