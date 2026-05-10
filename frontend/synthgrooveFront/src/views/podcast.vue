<script setup lang="ts">
const artistas = [
  {
    nombre: "YCOXXX",
    podcasts: [
      "https://soundcloud.com/ycoxxx/la-otra-cara-de-la-moneda?si=43e4530ffd01498a9c231056d2ad520a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/organiccty/organic-cty-005-ycoxxx?si=30782d51e6824c1699f4fa490b543ab7&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/fanzine-project/ycoxxx-live-at-fanzine-school?si=8006a1c917544e0fb8eb5e4104ee0294&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
    ],
    bio: "Tu descripción aquí...",
    instagram: "https://www.instagram.com/ycox.x.x/",
    soundcloud: "https://soundcloud.com/ycoxxx",
    imagen:
      "/src/assets/img/frontend/synthgrooveFront/src/assets/img/478401797_18151499806359791_2532489274665148093_n.jpg",
  },
  {
    nombre: "OSS",
    podcasts: [
      "https://soundcloud.com/12-inch-spain/archaic-podcast-602-oss?si=04d38866a4b3444b884c536043d8a1e9&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
    ],
    bio: "Tu descripción aquí...",
    instagram: "https://www.instagram.com/disc0sss/",
    soundcloud: "https://soundcloud.com/mylittlehorny",
  },
  {
    nombre: "VELO999",
    podcasts: [
      "https://soundcloud.com/dienachtbrenntclub/015velo999?in=v3loo/sets/collaborative-sesions&si=0dff6cbed6ba4547ae0653de74fa7f4c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/v3loo/synthgroove-showcase-cazuza-orzan-20062025-velo999?si=98d53a16b5c3491b808890fccaa64e94&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
    ],
    bio: "Tu descripción aquí...",
    instagram: "https://www.instagram.com/velo999_/",
    soundcloud: "https://soundcloud.com/v3loo",
  },
  {
    nombre: "WEISHEIT",
    podcasts: [
      "https://soundcloud.com/fisurafsr/an0106-weisheit?in=weisheit_dj/sets/mixes&si=20c30f60bd85489891d0948a177cc312&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/otiumdistrict/odpodcast045-weisheit?in=weisheit_dj/sets/mixes&si=91187875098b49e0b763e5ac97d6c00f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/lineoutradio/weisheit-fanzine-project-residency-16-on-line-out-radio-july-2025?in=weisheit_dj/sets/mixes&si=c086e7b034c348649ba58047074f384d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/weisheit_dj/bcco-new-faces-weisheit?in=weisheit_dj/sets/mixes&si=fa6804a9412e4901a8fa0b3cca26641b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/escea/weisheit-escea-galicia?in=weisheit_dj/sets/mixes&si=cb76d2e81a3446d5b07db86a72b90087&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/adolfo-c-1/podcast-series-weisheit?in=weisheit_dj/sets/mixes&si=ad35646ceb014fd6b8a9fdf55be9bf3f&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/fremdlab/fremd-podcast-22-weisheit?in=weisheit_dj/sets/mixes&si=f2ec329f19d24ae1ad833611b2509b54&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/peligroclub/radio-19?in=weisheit_dj/sets/mixes&si=2e63383566a3407f8f0314234e265640&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
      "https://soundcloud.com/weisheit_dj/grooves-from-home?in=weisheit_dj/sets/mixes&si=68b0e08e4f314d6c96f9495dd1d63132&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
    ],
    bio: "Tu descripción aquí...",
    instagram: "https://www.instagram.com/weisheit_dj/",
    soundcloud: "https://soundcloud.com/weisheit_dj",
  },
];
</script>
<template>
  <div class="podcasts-wrapper">
    <h1 class="titulo">LATEST PODCASTS</h1>
    <div class="separador"></div>

    <div
      v-for="artista in artistas"
      :key="artista.nombre"
      class="artista-bloque"
    >
      <div class="artista-header">
        <h2 class="nombre">{{ artista.nombre }}</h2>
        <span class="count">{{ artista.podcasts.length }} mixes</span>
      </div>
      <div class="separador"></div>

      <div
        v-for="podcast in artista.podcasts"
        :key="podcast"
        class="podcast-item"
      >
        <iframe
          width="100%"
          height="100"
          scrolling="no"
          frameborder="no"
          :src="`https://w.soundcloud.com/player/?url=${podcast}&color=%23002363&auto_play=false`"
        ></iframe>
      </div>

      <div class="separador"></div>
    </div>
  </div>
</template>

<style>
.podcasts-wrapper {
  max-width: 760px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.titulo {
  text-align: left;
  font-size: 0.75rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #666;
  margin-bottom: 1rem;
}

.separador {
  width: 100%;
  height: 1px;
  background-color: #222;
  margin: 1.5rem 0;
}

.artista-bloque {
  margin-bottom: 2rem;
}

.artista-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.nombre {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0;
}

.count {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #444;
}

.podcast-item {
  margin-bottom: 0.75rem;
}
</style>
