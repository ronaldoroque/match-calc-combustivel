let development = process.env.NODE_ENV !== 'production'
export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Match Calc Combustível',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { 'http-equiv': 'content-language', content: 'pt-Br' },
      { property: 'og:locale', content: 'pt_BR' },
      { property: 'og:site_name', content: 'Calc. de Combustível' },
      { hid: 'description', name: 'description', content: 'Calculadora de Combustível' },
      { name: 'google', content: 'notranslate' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/logo.ico' }
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
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa'
  ],

  // https://stackoverflow.com/questions/61045853/how-to-include-bootstrap-vue-icons-into-nuxtjs-problem-with-navbar-down-arrows
  bootstrapVue: {
    icons: true
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: development ? 'localhost:8000': 'https://match-calc-combustivel.vercel.app'
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'pt-Br',
      name: 'calc. Combustível',
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

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  // https://v2.nuxt.com/deployments/github-pages/
  router: {
    base: '/match-calc-combustivel/'
  },

  // https://stackoverflow.com/questions/54380719/set-path-to-output-folder-in-nuxt
  generate: {
    dir: '../docs'
  }
}
