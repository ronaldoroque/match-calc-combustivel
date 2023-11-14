<script>
export default {
  name: "Demonstracao",
  props: {
    display: {type: Boolean, default: false, required: false},
  },
  data() {
    return {
      videoIdList: [
        {id: "2wOyXLJh-Eo", title: "Limpar o formulário", description: "Demonstração da função de limpar os dados do formulário"},
        {id: "L2P3v3OQlVo", title: "Obter dados de uma viagem", description: "Demonstração da geração do relatório de viagem pela interface do usuário"},
        {id: "b4d_WvTznBA", title: "Obter dados e ida e volta", description: "Demonstração da geração do relatório de viagem de ida e volta pela interface do usuário"},
      ],
      tab: null,
      items: [
        'Appetizers', 'Entrees', 'Deserts', 'Cocktails',
      ],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },
  computed: {
    iframeHegth: function () {
      let altura = window.innerWidth / 2.1
      return `${altura}px`
    }
  }
}
</script>

<template>
  <v-row v-if="display" dense class="pb-2">

    <v-tabs v-model="tab" background-color="transparent" dark>
      <v-tab v-for="(video, key) in videoIdList" :key="key">
        {{ video.title }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" class="full-width">
      <v-tab-item v-for="(video, key) in videoIdList" :key="key" class="full-width">
      <v-card dark color="success" class="w-100">
        <iframe width="100%" :height="iframeHegth" ref="frame" :src="`https://www.youtube.com/embed/${video.id}`"
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen></iframe>
      </v-card>
      </v-tab-item>
    </v-tabs-items>


    <!--v-col class="col-12" v-for="(video, key) in videoIdList" :key="key">
      <v-card dark color="success">
        <iframe width="100%" :height="iframeHegth" ref="frame" :src="`https://www.youtube.com/embed/${video.id}`"
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen></iframe>
      </v-card>
    </v-col-->
  </v-row>
</template>

<style scoped>
iframe {
  border: 0;
  max-width: 1185px;
  max-height: 580px;
}
.full-width{
  width: 100%;
}
</style>
