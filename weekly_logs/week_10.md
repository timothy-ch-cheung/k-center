# Week 10
Summary: Implemented PBS algorithm

# Development
- Algorithm implemented and seems to be working with the basic example (achieves optimal cost, for original k-center problem, the best algorithm so far)
- A fairly large algorithm at ~300 loc

# Testing
- unit testing [repo now at 68 tests, 97% coverage]
- test coverage hasn't dropped but this is due to a single integration test for the whole algorithm
- will need to go back and add unit tests to the genetic operators

# Plans for next week
- fully unit test PBS algorithm

# Medium term plans for Christmas break
- well defined:
    - develop stepped visiualisations for GreedyReduce, and algorithm by Bandyapadhyay et al. [2 dev days]
    - develop stepped visiualisation for PBS genetic algorithm - this will need a bit of design work since multiple potential solutions need to be visualised [5 dev days]
    - memory and cpu profiling of each algorithm [3 dev days]
- investigatory:
    - Modify PBS to solve Colourful K-Center
        - Change cost function take into account of outliers (this will probably change it from O(n) O(n<sup>2</sup>))
        - Genetic operators need to account for cost (original PBS doesn't)
    - Attempting to implement the 3-approximation algorithm for Colourful K-Center by Jia et al.
    - Attempting to implement the algorithm for α-seperated by Bandyapadhyay et al.