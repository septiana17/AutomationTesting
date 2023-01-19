/// <reference types="cypress" />

describe('Login Test Negatif', () => {

  it('Visits the internet with username and password', () => {
    // visit the-internet page
    cy.visit('https://the-internet.herokuapp.com/login')

    // looking for name of Login Page in the-internet
    cy.contains('Login Page')

    // wrong username
    cy.get('#username').type('wrong')

    // wrong password
    cy.get('#password').type('1234')

    // button login
    cy.get('button').click()

    // Should be on aller "Your username is invalid!"
    cy.get('#flash').should('contain', 'Your username is invalid!')

  })

})