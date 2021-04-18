const {TOLERANCE} = require("../../constants");
context('Learn', () => {

  it('tutorial has equivalent carousel screenshots', () => {
      cy.visit('learn')
      const SLIDES = 11

      let i
      for (i=0; i < SLIDES; i++) {
          cy.compareSnapshot(`learn_${i.toString().padStart(2, "0")}`, TOLERANCE)
          cy.get('[aria-label="next slide / item"]').click()
          cy.wait(0.25)
      }

      cy.compareSnapshot(`learn_${i}`, TOLERANCE)
      cy.get('[aria-label="next slide / item"]').should('have.css', 'display', 'none')
  })

})
