

describe('template spec', () => {
  beforeEach('Entra no site', () => {
    cy.visit('/')
  })
  it('Inserir dados e limpar', () => {
    cy.fixture('coordenadas').then((coordenadas) => {
      // Insere coordenadas
      cy.get('input[id=origemLatitude]').type(coordenadas.origem_latitude)
      cy.get('input[id=origemLongitude]').type(coordenadas.origem_longitude)
      cy.get('input[id=destinoLatitude]').type(coordenadas.destino_latitude)
      cy.get('input[id=destinoLongitude]').type(coordenadas.destino_longitude)
    })

    const mediaConsumoVeiculo = 14
    cy.get('input[id=mediaConsumoVeiculo]').type(mediaConsumoVeiculo)
    cy.get('input[id=idaEVolta]').parent().click()
    cy.wait(2000)

    // Submete formulário
    cy.get('[data-cy="resetForm"]').click()
    cy.wait(1000)

    // Verifica relatório
    cy.get('input[id=origemLatitude]').should('have.value', '')
    cy.get('input[id=origemLongitude]').should('have.value', '')
    cy.get('input[id=destinoLatitude]').should('have.value', '')
    cy.get('input[id=destinoLongitude]').should('have.value', '')
    cy.get('input[id=mediaConsumoVeiculo]').should('have.value', '')
    cy.get('input[id=mediaConsumoVeiculo]').should('have.value', '')
    cy.get('[data-cy="idaEVolta"]').should('have.value', 'false')
    cy.wait(3000)
  })
})