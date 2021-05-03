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
        cy.get('[cy-data=greedy]').click()

        cy.get('[cy-data=solve-submit-btn]').click()
        cy.compareSnapshot("solve_graph_basic_greedy", TOLERANCE)
    })

    it('Visual regression on alert for attempting to brute force large instance', () => {
        cy.intercept('POST', 'solve', (req) => {
            req.continue((res) => {
                res.body.alert.message = "Solving was not attempted, on this server, it would take 6 years,19 weeks,4 days,9 hours,31 minutes,56.605 seconds to solve"
            })
        })

        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=large-instance]').click()
        cy.get('[cy-data=algorithm-select]').click()
        cy.get('[cy-data=brute_force_colourful_k_center]').click()
        cy.get('[cy-data=solve-submit-btn]').click()

        cy.compareSnapshot("solve_graph_brute_force_alert", TOLERANCE)
        cy.get('[cy-data=extra-info-link]').click()
        cy.compareSnapshot("solve_graph_brute_force_alert_expanded", TOLERANCE)
    })

    it('Shows available algorithms', () => {
        cy.get('[cy-data=algorithm-select]').click()
        cy.compareSnapshot("solve_available_algorithms", TOLERANCE)
    })
})
