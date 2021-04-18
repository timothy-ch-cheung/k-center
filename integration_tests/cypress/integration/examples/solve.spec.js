context('Solve', () => {

    beforeEach(() => {
        cy.visit('solve')
    })

    it('Visual regression on /solve page', () => {
        cy.compareSnapshot("solve")
    })

    it('Visual regression on loading a graph', () => {
        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=basic-instance]').click()
        cy.compareSnapshot("solve_load_graph_basic")
    })

})
