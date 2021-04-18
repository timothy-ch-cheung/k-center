context('Step', () => {

    it('Visual regression on /steps page', () => {
        cy.visit('steps')
        cy.compareSnapshot("steps")
    })

})
