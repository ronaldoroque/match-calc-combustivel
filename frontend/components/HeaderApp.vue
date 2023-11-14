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
  <div class="w-100 dark bg-teal-darken-4">
    <v-container class="py-0 bg-teal-darken-4" style="max-width: 1185px" >
      <v-app-bar class="d-print-none px-0 bg-teal-darken-4" dark flat dense style="background-color: #004d40">
        <v-toolbar-title class="px-0">Calculadora de Combustível</v-toolbar-title>
        <v-spacer />
        <v-btn type="button" color="success" small @click="toggleSobre()">
          Sobre
          <v-icon v-if="displaySobre" right>mdi-arrow-collapse-up</v-icon>
          <v-icon v-else right>mdi-information-outline</v-icon>
        </v-btn>
        <v-btn type="button" color="success" small @click="toggleDemonstra()" class="ml-4">
          Demosntração
          <v-icon v-if="displayDemonstra" right>mdi-arrow-collapse-up</v-icon>
          <v-icon v-else right>mdi-movie-cog-outline</v-icon>
        </v-btn>
      </v-app-bar>
      <sobre :display="displaySobre" />
      <demosntracao :display="displayDemonstra" />
    </v-container>
  </div>
</template>

<style scoped>
div.dark {
  background-color: #004d40;
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2), 0px 4px 5px 0px rgba(0, 0, 0, 0.14), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
}

.head_app {
  height: 16rem !important;
}
</style>
