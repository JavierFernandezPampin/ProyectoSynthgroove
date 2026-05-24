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
  background: black;
  min-height: 100vh;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.home-main {
  padding: 0 0 3rem;
}

.hero {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: clamp(34rem, 76vh, 52rem);
  margin-inline: auto;
  margin-top: 0;
  overflow: hidden;
  background: #121212;
  isolation: isolate;
}

.hero-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(
      180deg,
      rgba(0, 0, 0, 0.2) 0%,
      rgba(0, 0, 0, 0.42) 50%,
      rgba(0, 0, 0, 0.72) 100%
    ),
    rgba(0, 0, 0, 0.12);
}

.hero-title {
  position: relative;
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
  .hero {
    min-height: 64vh;
  }

  .hero-title {
    padding: 1.5rem;
    letter-spacing: 0.05em;
  }
}
</style>
