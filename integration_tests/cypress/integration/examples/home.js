const {TOLERANCE} = require("../../constants");
context('Solve', () => {

    it('tutorial has equivalent carousel screenshots', () => {
        cy.visit("/")
        cy.compareSnapshot("home", TOLERANCE)
    })

})