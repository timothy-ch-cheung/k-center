const {TOLERANCE} = require("../../constants");
context('Step', () => {

    beforeEach(() => {
        cy.visit('steps')
    })

    it('Visual regression on /steps page', () => {
        cy.compareSnapshot("steps", TOLERANCE)
    })

    it('Visual regression on /steps modal', () => {
        cy.get("[cy-data=steps-modal-btn]").click()
        cy.compareSnapshot("steps_modal", TOLERANCE)
    })

    it('Visual regression on stepped walk through for greedy algorithm', () => {
        cy.get("[cy-data=steps-modal-btn]").click()
        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=basic-instance]').click()
        cy.get('[cy-data=algorithm-select]').click()
        cy.get('[cy-data=greedy]').click()

        cy.get('[cy-data=solve-submit-btn]').click()
        cy.compareSnapshot("steps_walkthrough_00", TOLERANCE)
        cy.get('[cy-data=page-prev]').should('be.disabled')

        const STEPS = 3
        for(let i = 1; i < STEPS + 1; i++) {
            cy.get('[cy-data=page-next]').click()
            cy.compareSnapshot(`steps_walkthrough_${i.toString().padStart(2, "0")}`, TOLERANCE)
        }
        cy.get('[cy-data=page-next]').should('be.disabled')
        cy.get('[cy-data=page-prev]').should('not.be.disabled')

        for(let i = 0; i < STEPS -1; i++) {
            cy.get('[cy-data=page-prev]').click()
        }
        cy.get('[cy-data=page-prev]').should('be.disabled')
        cy.get('[cy-data=page-next]').should('not.be.disabled')
    })

    it('Visual regression on stepped walk through for colourful PBS algorithm', () => {
        cy.get("[cy-data=steps-modal-btn]").click()
        cy.get('[cy-data=problem-instance-select]').click()
        cy.get('[cy-data=medium-instance]').click()
        cy.get('[cy-data=algorithm-select]').click()
        cy.get('[cy-data=colourful_pbs]').click()

        cy.get('[cy-data=solve-submit-btn]').click()
        cy.compareSnapshot("steps_walkthrough_colourful_pbs_large_00", TOLERANCE)

        cy.intercept('POST', 'next', { fixture: 'colourful_pbs_medium_1.json' })
        cy.get('[cy-data=page-next]').click()
        cy.compareSnapshot("steps_walkthrough_colourful_pbs_large_01", TOLERANCE)

        cy.intercept('POST', 'next', { fixture: 'colourful_pbs_medium_2.json' })
        cy.get('[cy-data=page-next]').click()
        cy.compareSnapshot("steps_walkthrough_colourful_pbs_large_02", TOLERANCE)
        cy.get('[cy-data=zoom-individual-btn]').click()
        cy.compareSnapshot("steps_walkthrough_colourful_pbs_large_03", TOLERANCE)
    })

    it('Shows available algorithms', () => {
        cy.get("[cy-data=steps-modal-btn]").click()
        cy.get('[cy-data=algorithm-select]').click()
        cy.compareSnapshot("step_available_algorithms", TOLERANCE)
    })
})
