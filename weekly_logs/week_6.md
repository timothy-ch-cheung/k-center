# Week 6
Summary: Implementing the Colourful K-Center algorithm by Bandyapadhyay

Decided not to use mpld3 as it was too inflexible, I used D3 directly instead.

## Development
- created a React JS application which contains a D3 Chart
- D3 chart renders graphs given some json data. Also has an interactive legend which can toggle centers and points. Tooltips for displaying the coordinate and class of each point.
- created a bare-bones flask server which serves the react application (this will be used later to communicate between the python and JS for visualisation and stepping through solutions)
- coded the clustering algorithm and LP2 from the paper by Bandyapadhyay et al.
- already had a prototype for LP1 so just cleaned up the code
- combined the three sub procedures together to create the solver. The paper doesn't specify how the algorithm makes "guesses" at the optimum using LP1. I have just used a (sorted) linear search for now (for the sake of simplicity) but can refactor it to a binary search later

## Testing
- added unit tests for all three procedures and added integration tests for the solver [repo now at 37 tests, 100% coverage]
- found in the small 5 point (3 blue points, 2 red points) example, the Bandyapadhyay algorithm (arguably) produced solutions
which weren't as good as the greedy algorithm. The greedy algorithm go a cost of 0.854. The Bandyapadhyay algorithm correctly "guessed" the optimal cost of 0.728. But the Bandyapadhyay algorithm will always double the cost (to account for choosing the wrong centers) making it 1.456.

## Difficulties
- Pyomo for linear programming is new to me, got stuck quite a lot when implementing LP1 and LP2

## Next Week
- implement the integration between the React app and Python K-Center solvers. Aim to get at least solving and returning the solution for the D3 Chart to display at minimum.
- Investigate what benchmarking options there are
- Re-read the paper by Jia et al. to understand their algorithm which uses Bandyapadhyay's (constant pseudo approximation) algorithm to create a true 3-approximation to the Colourful K-Center problem. Implement it.
- If I have time, create the generator equivalent of the Bandyapadhyay algorithm.

## Revised goals after talking with supervisor
- implement the integration between the React app and Python K-Center solvers. Aim to get at least solving and returning the solution for the D3 Chart to display at minimum.
- Investigate what benchmarking options there are
- Look at performance of algorithms against large data sets