<script setup lang="ts">
const tracks = [
  "https://soundcloud.com/laburnum-records/premiere-weisheit-i-miss-my?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/laburnum-records/weisheit-in-the-mood-for-more-lbrnm41?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/weisheit_dj/weisheit-unfair-game-master?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/weisheit_dj/weisheit-i-want-to?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/rawppl/premiere-weisheit-movin-up-kkva03?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/belugatracks/bt-premiere-weisheit-snow-trip?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/humansourcerecords/weisheit-the-void-below-us-free-dl?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/weisheit_dj/weisheit-a-donde-iras-unreleased?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/weisheit_dj/weisheit-cycles-orbital-oscillation?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/belugatracks/bt-premiere-weisheit?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/truckingrecords/premiere-weisheit-spittin-facts-and-lies?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
  "https://soundcloud.com/tucca-premiere/471-premiere-weisheit-volver-orbital-oscillation?in=weisheit_dj/sets/trax&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
];
</script>
<template>
  <div class="releases-wrapper">
    <h1 class="titulo-releases">LATEST RELEASES</h1>
    <div class="separador"></div>

    <div v-for="track in tracks" :key="track" class="track-item">
      <iframe
        width="100%"
        height="100"
        scrolling="no"
        frameborder="no"
        :src="`https://w.soundcloud.com/player/?url=${track}&color=%23002363&auto_play=false`"
      ></iframe>
    </div>
  </div>
</template>

<style>
.releases-wrapper {
  max-width: 760px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.titulo-releases {
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
  margin: 1rem 0;
}

.track-item {
  margin-bottom: 0.75rem;
}
</style>
