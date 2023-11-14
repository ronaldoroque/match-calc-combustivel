<script>
export default {
  name: "Sobre",
  props: {
    display: {type: Boolean, default: false, required: false},
  },
}
</script>

<template>
  <v-row v-if="display" dense class="pb-2">
    <v-col class="col-12 col-md-8 mb-2">
      <v-card dark color="success">
        <v-card-title>Sobre o Projeto</v-card-title>
        <v-card-text>
          <span class="text_white">
          Neste projeto, os participantes criaram uma aplicação em Python que calcula a quantidade de
          combustível necessária para percorrer uma determinada distância entre dois pontos geográficos,
          levando em consideração o consumo médio de combustível do veículo.
          </span>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col class="col-12 col-md-4 mb-2">
      <v-card dark color="success" class="fill-height">
        <v-card-subtitle class="white--text">Participantes</v-card-subtitle>
        <v-card-text>
          <ul class="list-unstyled">
            <li><a href="https://www.linkedin.com/in/andrade-rog" class="text-light border-bottom text_white">
              Rogério Andrade
              <v-icon class="ml-2" small>mdi-linkedin</v-icon>
            </a></li>
            <li><a href="https://www.linkedin.com/in/doroque" class="text-light border-bottom text_white">
              Ronaldo Roque
              <v-icon class="ml-2" small>mdi-linkedin</v-icon>
            </a></li>
          </ul>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<style scoped>
.text_white{
  color: #fff;
}
</style>
