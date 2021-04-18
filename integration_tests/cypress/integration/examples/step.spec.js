const {TOLERANCE} = require("../../constants");
context('Step', () => {

    beforeEach(() => {
        cy.visit('steps')
    })

    it('Visual regression on /steps page', () => {
        cy.compareSnapshot("steps", TOLERANCE)
    })

    it('Visual regression on /steps modal', () => {
        cy.get("[data-cy=steps-modal-btn]").click()
        cy.compareSnapshot("steps_modal", TOLERANCE)
    })

})
