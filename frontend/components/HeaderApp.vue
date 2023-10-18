<script>

export default {
  name: 'HeaderApp',
  data() {
    return {
      displaySobre: false,
    }
  },
  methods: {
    toggleSobre: function () {
      this.displaySobre = !this.displaySobre
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
          <v-icon v-else right>mdi-arrow-collapse-down</v-icon>
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
    </v-container>
  </div>

  <!--div class="w-100 bg-dark">
    <b-container>
      <b-navbar toggleable type="dark" variant="dark">
        <b-navbar-brand href="#">Calculadora de Combustível</b-navbar-brand>
        <button v-if="expanded" type="button" class="btn btn-secondary float-end ml-auto py-0 py-md-1" size="sm" @click="expanded=!expanded">
                Sobre o Projeto <b-icon icon="chevron-bar-up" class="ml-2"></b-icon></button>
        <button v-else type="button" class="btn btn-secondary float-end ml-auto py-0 py-md-1" size="sm" @click="expanded=!expanded">
                Sobre o Projeto <b-icon icon="chevron-bar-down" class="ml-2"></b-icon></button>

        <b-collapse id="navbar-toggle-collapse" v-model="expanded" is-nav>
          <div class="container text-white">
            <div class="row">
              <div class="col-sm-8 col-md-7 py-4">
                <h4>Sobre o Projeto</h4>
                <p class="text-body-secondary">
                  Neste projeto, os alunos criarão uma aplicação em Python que calculará a quantidade de
                  combustível necessária para percorrer uma determinada distância entre dois pontos,
                  levando em consideração o consumo estimado do veículo fornecido pelo usuário. A
                  aplicação utilizará uma API de mapas para calcular a distância entre os pontos.
                </p>
              </div>
              <div class="col-sm-4 offset-md-1 py-4">
                <h4>Participantes</h4>
                <ul class="list-unstyled">
                  <li><a href="https://www.linkedin.com/in/andrade-rog" class="text-light border-bottom">
                    Rogério Andrade <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon></a></li>
                  <li><a href="https://www.linkedin.com/in/doroque" class="text-light border-bottom">
                    Ronaldo Roque <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon></a></li>
                </ul>
              </div>
            </div>
          </div>
        </b-collapse>
      </b-navbar>
    </b-container>
  </div-->
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
