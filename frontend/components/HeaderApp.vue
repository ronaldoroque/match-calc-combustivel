<script>

export default {
  name: 'HeaderApp',
  data() {
    return {
      displaySobre: false,
      displayDemonstra: false,
    }
  },
  methods: {
    toggleSobre: function () {
      this.displaySobre = !this.displaySobre
    },
    toggleDemonstra: function () {
      this.displayDemonstra = !this.displayDemonstra
    },
  }
}
</script>

<template>
  <div class="w-100 dark">
    <v-container class="py-0" style="max-width: 1185px;">
      <v-app-bar class="d-print-none px-0" dark flat dense>
        <v-toolbar-title class="px-0">Calculadora de Combustível</v-toolbar-title>
        <v-spacer />
        <v-btn type="button" color="blue-grey" small @click="toggleSobre()">
          Sobre
          <v-icon v-if="displaySobre" right>mdi-arrow-collapse-up</v-icon>
          <v-icon v-else right>mdi-information-outline</v-icon>
        </v-btn>
        <v-btn type="button" color="blue-grey" small @click="toggleDemonstra()" class="ml-4">
          Demosntração
          <v-icon v-if="displayDemonstra" right>mdi-arrow-collapse-up</v-icon>
          <v-icon v-else right>mdi-movie-cog-outline</v-icon>
        </v-btn>
      </v-app-bar>

      <v-row v-if="displaySobre" dense class="pb-2">
        <v-col class="col-12 col-md-8 mb-2">
          <v-card dark>
            <v-card-title>Sobre o Projeto</v-card-title>
            <v-card-text>
              Neste projeto, os participantes criaram uma aplicação em Python que calcula a quantidade de
              combustível necessária para percorrer uma determinada distância entre dois pontos geográfica,
              levando em consideração o consumo médio de combustível do veículo.
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="col-12 col-md-4 mb-2">
          <v-card dark class="fill-height">
            <v-card-subtitle class="white--text">Participantes</v-card-subtitle>
            <v-card-text>
              <ul class="list-unstyled">
                <li><a href="https://www.linkedin.com/in/andrade-rog" class="text-light border-bottom">
                  Rogério Andrade
                  <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon>
                </a></li>
                <li><a href="https://www.linkedin.com/in/doroque" class="text-light border-bottom">
                  Ronaldo Roque
                  <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon>
                </a></li>
              </ul>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-row v-if="displayDemonstra" dense class="pb-2">
        <v-col class="col-12 col-md-4">
          <v-card dark>
            <v-card-text>Vídeo embed
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="col-12 col-md-4">
          <v-card dark>
            <v-card-text>Vídeo embed
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="col-12 col-md-4">
          <v-card dark>
            <v-card-text>Vídeo embed
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped>
div.dark {
  background-color: #272727;
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2), 0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
}

.head_app {
  height: 16rem !important;
}
</style>
