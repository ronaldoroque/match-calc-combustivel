describe('template spec', () => {
  it('entra no site', () => {
    cy.visit('http://localhost:3000/match-calc-combustivel/')
  })
  it('insere coordenadas', () => {
    cy.visit('http://localhost:3000')
    const coordenadas = {
      origem_longitude: -41.9480517645751,
      origem_latitude: -18.9047485170197,
      destino_longitude: -41.953074390246016,
      destino_latitude: -18.849342234646826
    }
    const mediaConsumoVeiculo = 14
    cy.get('input[id=origemLongitude]').type(coordenadas.origem_longitude)
    cy.get('input[id=origemLatitude]').type(coordenadas.origem_latitude)
    cy.get('input[id=destinoLongitude]').type(coordenadas.destino_longitude)
    cy.get('input[id=destinoLatitude]').type(coordenadas.destino_latitude)
    cy.get('input[id=mediaConsumoVeiculo]').type(mediaConsumoVeiculo)
    cy.get('input[id=idaEVolta]').parent().click()
    cy.get('[data-cy="SubmitForm"]').click()

    cy.get('[data-cy="reportCard"]').should('contain', 'ida e volta')
  })
})