# Week 8
Summary: Created new page/UI that allows user to step through an algorithm and see the centers in the intermediate stages.

## Development
- Client creates an uuid which the server uses to identify the problem client is interest in (stored in memory in a dictionary)
- Every time the client wants to see the next step of the solution they send a POST with the uuid and the result of the next step is returned
- Client repeatedly clicks next until a solution is reached, at which point they will have all stages's state in client side memory so they can step back and forth between stages

## Testing
- Mostly manual testing of the UI (writing automated end-to-end tests in Cypress would be too time costly)
- unit testing [repo now at 54 tests, 97% coverage]. Not much new tests needed as the server side generator algorithm was already unit tested in week 8

## Difficulties
- Re-reading Colourful algorithm (Bandyapadhyay et al.) section 3.2, currently having a lot of difficulty understanding the concepts behind the algorithm for α-separated instances. For example several new concepts that I was not familiar with:
    - Minkowski sums
    - Voronoi regions
    - Exact Perfect matching problem
    - Pfaffian of a matrix