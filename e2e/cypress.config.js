const { defineConfig } = require("cypress");

module.exports = defineConfig({
  viewportWidth: 1000,
  viewportHeight: 800,
  video: true,
  videosFolder: 'cypress/videos',
  videoCompression: true,
  e2e: {
    // baseUrl: 'http://localhost:3000/match-calc-combustivel/',
    baseUrl: 'https://ronaldoroque.github.io/match-calc-combustivel',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
