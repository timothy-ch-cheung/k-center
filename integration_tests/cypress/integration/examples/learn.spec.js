context('Learn', () => {
  beforeEach(() => {

  })

  it('tutorial has equivalent carousel screenshots', () => {
      cy.visit('learn')
      const SLIDES = 12

      let i
      for (i=0; i < SLIDES; i++) {
          cy.compareSnapshot(`learn_${i}`)
          cy.get('[aria-label="next slide / item"]').click()
          cy.wait(0.25)
      }
      cy.get('[aria-label="next slide / item"]').should('not.exist');
  })
})
