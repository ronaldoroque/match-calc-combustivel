describe('template spec', () => {
  beforeEach('Entra no site', () => {
    cy.visit('/')
    cy.wait(1000)
  })
  it('Obter relatório de Viagem', () => {
    const coordenadas = {
      origem_longitude: -41.9480517645751,
      origem_latitude: -18.9047485170197,
      destino_longitude: -41.953074390246016,
      destino_latitude: -18.849342234646826
    }
    const mediaConsumoVeiculo = 14

    // Insere coordenadas
    cy.get('input[id=origemLatitude]').type(coordenadas.origem_latitude)
    cy.get('input[id=origemLongitude]').type(coordenadas.origem_longitude)
    cy.get('input[id=destinoLatitude]').type(coordenadas.destino_latitude)
    cy.get('input[id=destinoLongitude]').type(coordenadas.destino_longitude)
    cy.get('input[id=mediaConsumoVeiculo]').type(mediaConsumoVeiculo)
    cy.get('input[id=idaEVolta]').parent().click()
    cy.wait(3000)

    // Submete formulário
    cy.get('[data-cy="SubmitForm"]').click()
    cy.wait(1000)

    // Verifica relatório
    cy.get('[data-cy="reportCard"]').should('contain', 'ida e volta')
    cy.get('[data-cy="reportCard"]').should('contain', '18,43 Km')
    cy.wait(6000)
  })
})