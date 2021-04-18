context('Solve', () => {

    it('Visual regression on /solve page', () => {
        cy.visit('solve')
        cy.compareSnapshot("solve")
    })

})
