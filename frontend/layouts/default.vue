<template>
  <v-app style="background-color: #FFFFF6">
  <HeaderApp />
    <v-main>
      <Nuxt />
    </v-main>
    <FooterApp />
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout'
}
</script>
