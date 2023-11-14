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
    <v-col class="col-12">
      <v-card dark color="success">
        <v-card-text>Vídeo embed
        </v-card-text>
      </v-card>
    </v-col>
    <v-col class="col-12">
      <v-card dark color="success">
        <v-card-text>Vídeo embed
        </v-card-text>
      </v-card>
    </v-col>
    <v-col class="col-12">
      <v-card dark color="success">
        <v-card-text>Vídeo embed
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<style scoped>

</style>
