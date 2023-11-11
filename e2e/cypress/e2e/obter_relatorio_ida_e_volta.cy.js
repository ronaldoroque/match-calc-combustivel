describe('template spec', () => {
  beforeEach('Entra no site', () => {
    cy.visit('/')
  })
  it('Obter relatório de Viagem', () => {
    cy.fixture('coordenadas').then((coordenadas) => {
      // Insere coordenadas
      cy.get('input[id=origemLatitude]').type(coordenadas.origem_latitude)
      cy.get('input[id=origemLongitude]').type(coordenadas.origem_longitude)
      cy.get('input[id=destinoLatitude]').type(coordenadas.destino_latitude)
      cy.get('input[id=destinoLongitude]').type(coordenadas.destino_longitude)
    })

    const mediaConsumoVeiculo = 14
    cy.get('input[id=mediaConsumoVeiculo]').type(mediaConsumoVeiculo)
    cy.wait(500)

    cy.get('input[id=idaEVolta]').parent().click()

    // Submete formulário
    cy.wait(1000)
    cy.get('[data-cy="SubmitForm"]').click()

    // Verifica relatório
    cy.get('[data-cy="reportCard"] > h2').should('contain', 'ida e volta')
    cy.get('[data-cy="reportCard"] > h3 > b').should('contain', 'Combustível necessário:')
    cy.wait(6000)
  })
})