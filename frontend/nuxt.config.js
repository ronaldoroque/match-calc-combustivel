import colors from 'vuetify/es5/util/colors'

let development = process.env.NODE_ENV !== 'production'

export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - Calc. Combustível',
    title: 'Home',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { 'http-equiv': 'content-language', content: 'pt-BR' },
      { property: 'og:locale', content: 'pt-BR' },
      { property: 'og:site_name', content: 'Calc. de Combustível' },
      { hid: 'description', name: 'description', content: 'Calculadora de Combustível' },
      { name: 'google', content: 'notranslate' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/match-calc-combustivel/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    // '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: development ? 'localhost:8000': 'https://match-calc-combustivel.vercel.app'
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'pt-Br',
      name: 'Calc. Combustível',
      short_name: 'Calc. Combustível',
      description: 'Calculadora de Combustível',
      background_color: '#fff',
      theme_color: '#fff'
    },
    meta: {
      charset: 'utf-8',
      theme_color: '#fff'
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.teal.darken3,
          dark_green: colors.teal.darken4
        },
        light: {
          primary: colors.teal.darken4,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.teal.darken3,
          dark_green: colors.teal.darken4
        }
      }
    }
  },

  // https://v2.nuxt.com/deployments/github-pages/
  router: {
    base: '/match-calc-combustivel/'
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  // https://stackoverflow.com/questions/54380719/set-path-to-output-folder-in-nuxt
  generate: {
    dir: '../docs'
  }
}
