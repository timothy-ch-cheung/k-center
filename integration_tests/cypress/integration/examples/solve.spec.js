const {TOLERANCE} = require("../../constants");
context('Solve', () => {

    beforeEach(() => {
        cy.visit('solve')
    })

    it('Visual regression on /solve page', () => {
        cy.compareSnapshot("solve", TOLERANCE)
    })

    it('Visual regression on loading a graph', () => {
        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=basic-instance]').click()
        cy.compareSnapshot("solve_load_graph_basic", TOLERANCE)
    })

    it('Visual regression on solving a graph', () => {
        cy.intercept('POST', 'solve', (req) => {
            req.continue((res) => {
                res.body.solutions[0].timeTaken = 0.001
            })
        })

        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=basic-instance]').click()
        cy.get('[cy-data=algorithm-select]').click()
        cy.get('[cy-data="greedy').click()

        cy.get('[cy-data=solve-submit-btn]').click()
        cy.compareSnapshot("solve_graph_basic_greedy", TOLERANCE)
    })

})
