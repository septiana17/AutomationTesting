/// <reference types="cypress" />

describe('Login Test Positif', () => {

  it('Visits the internet with username and password', () => {
    // visit the-internet page
    cy.visit('https://the-internet.herokuapp.com/login')

    // looking for name of Login Page in the-internet
    cy.contains('Login Page')

    // username
    cy.get('#username').type('tomsmith')

    // password
    cy.get('#password').type('SuperSecretPassword!')

    // button login
    cy.get('button').click()

    // Should be on a new URL which includes '/secure'
    cy.url().should('include', '/secure')

    cy.get('#flash').should('contain', 'You logged into a secure area!')

  })

})