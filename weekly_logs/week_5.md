# Week 5
Summary: Setting up the repo and implementing the Gonzalez algorithm

Started putting requirements in writing on the gitlab repo.
## Modules
- Settled with using NetworkX to model the graphs (as it has a convenient way to access nodes and edges plus ability to add attributes which is useful for adding node colours)
- Pytest to make sure my code is adequately tested

## Coding
- Wrote code to verify that a set of centers and a given radius satisfy the covering constraints of the Colourful K-Center problem
- Implemented the Gonzalez algorithm (Greedy heuristic) - since it covers all nodes, it will always satisfy the Colour constraints
    - Found an example where the Gonzalez algorithm produces a sub optimal cost due to covering all nodes where there is an outlier it can exclude
- Extended the Gonzalez algorithm to incrementally reduce the radius it attempts to cover until the constraints aren't covered.
- Created generator function equivalents of the above two algorithms. This will be useful when I do step by step visualisations, to lazily compute the clustering on demand

## Testing
- 19 tests, 98% coverage
- example of outlier scenario mentioned above, in the test case ```test_greedy_basic_graph_outlier_colourful_clustering``` in ```test_greedy.py```

## Difficulties
- still getting used to programming in python again
- generator functions were new to me

## Next Week
- implement prototype for visualisation, work out whether to use:
    - python notebook with mpld3
    - react with mpld3

- re-read the paper by Bandyapadhyay et al. and implement the clustering algorithm