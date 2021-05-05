# Week 4
Summary: reading in areas of clustering related to k-center fairness and reading in evolutionary approaches to k-center

## Genetic algorithms reading
#### A Genetic Algorithm Using Hyper-Quadtrees for Low-Dimensional K-means Clustering
- Issues with genetic algorithms include inefficient crossover operators and expensive fitness functions
- Technique of swapping subtrees may also be compatible with K-Center

#### A Memetic Genetic Algorithm for the Vertex p-center Problem
- Proposes an algorithm called PBS (population based search), two mutation operators and two crossover operators. I plan to use these operators and see their performance K-Center with fairness constraints

## Fair K-Center reading
#### A Technique for Obtaining True Approximations for k-Center with Covering Constraints (Anegg et al. 2020)
- introduces Fair colourful k-center, an additional fairness constraint on the colourful problem. Each element needs to be covered with a given probability.
- didn't understand algorithm will need to do background reading on "round-or-cut" and "ellipsoid" methods

#### How to Solve Fair k-Center in Massive Data Models
- Presents a streaming and distributed algorithm. The procedures used in those algorithms create representative subsets which could be useful for reducing the search space in my project.

## Other related reading
#### Algorithms for Facility Location Problems with Outliers
- two concepts of robustness; robust (p out of n clients must be covered) and penalty (uncovered clients incurr a cost)
- A simple algorithm which greedily selects the "disk" with the most uncovered points (3-approximation)

#### Clustering to minimize the maximum inter-cluster distance
- Defines the K-Center as three sub problems (two optimisation and on decision)
- Simple 2-approximation algorithm for the unconstrained K-Center problem
- Only approximation proof I understand so far

#### Solving the p-Center Problem with Tabu Search and Variable Neighborhood Search
- Talks about an interesting varaition of Gonzalez's greedy heuristic where all starting points are enumerated
- Will require more understanding about neighbourhood search to understand the algorithm

## Currently reading
#### Fair k-Centers via Maximum Matching
- Relates to K-Center fairness defined by a requirement of demographic for the Centers of the solution rather than a coverage requirement so might not be as relevant to my project.