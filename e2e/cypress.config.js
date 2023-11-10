const { defineConfig } = require("cypress");

module.exports = defineConfig({
  viewportWidth: 1000,
  viewportHeight: 1000,
  video: true,
  videosFolder: 'cypress/videos',
  videoCompression: true,
  e2e: {
    baseUrl: 'http://localhost:3000/match-calc-combustivel/',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
