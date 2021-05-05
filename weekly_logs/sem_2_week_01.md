# Semester 2 Week 1 Log
## Takeaways from project inspection
- Feedback: 
  - Well defined project with clear goals and a working implementation of important parts
  - Test sets and Stability (in terms of running time and solution cost) are important for evaluating the perfomrance of a genetic algorithm
  - Is the genetic algorithm sensitive to small changes in the data
- Actions:
  - One possible way to address this to generate problem instances with different parameters for properties of the data such as:
    - class imbalance (number of red vs blue points)
    - center separation (clusters which are very far away from eachother or close)
    - outliers (percentage of data points which are outliers)
  - In the meeting with Rajesh in week 1, he also suggested another way was to test the algorithms on multiple standard machine learning data sets not neccessarily used on the K-Center problem
    - Without the known optimal costs, we can only compare Colourful PBS against O(1)-Colourful relative to eachother

## Progress over break
- Unit tests for PBS algorithm
- Optimise PBS algorithm implementation for 5 fold performance increase (mostly from minimising NetworkX calls), these issues were found from performance profiling with cProfile
- Bugfix to Colourful K-Center problem instance generator not creating graphs with valid optimal costs
- Experimented with PBS population update conditions to maintain diversity (although in testing they didn't make any signficant difference)
- Create new algorithm Colourful PBS which are my modifications to the PBS algorithm which allow it to create solutions to the Colourful K-Center problem
- Add step by step visualisation of greedy_reduce, O(1)-Colourful pseudo, and O(1)-Colourful algorithms

## Progress in week 1
- Add stepped visualistaion for PBS algorithm
  - each individual in the population can be viewed at the end of each generation
  - room for improvement: add step by step explanation of the local search algorithm and genetic operator
- Implement a version of PBS which terminates when a given cost is reached - this will:
  -  be useful for analysing which genetic operators contributed to finding the target cost the most often (similar to W. Pullan 2008)
  -  allow for comparisons with their benchmarking

# Plan for remainder of semester 2
## Week 2
- Complete Implementation PBS that terminates when a cost is reached. 
- Create file processors for ORLIB/TSPLIB to benchmark performance of PBS
- Implement brute force solver for Colourful K-Center problem (do write up for complexity/algorithm for introduction of report)
## Week 3
- Complete draft of introduction:
  - introduce Colourful K-Center and how it builds on original K-Center
  - Aims and motiviation section
- Implement step by step visualisation for local search and genetic operators of PBS algorithms
## Week 4
- Attempt to implement alpha seperate part of O(1)-Colourful algorithm (not sure if feasible)
- Complete draft for explaining algorithms:
  - Greedy (Gonzalez 1985)
  - PBS (2008)
  - O(1)-Colourful (2019)
  - Colourful PBS
## Week 5
- Review implementaiton of Colourful PBS:
  - Do changes need to be made to consider class imbalance?
  - Is the permutation approach by W. Pullan the best method, or should more traditional roulette selection be used?
## Week 6
- Complete draft for method 
- Run time benchmarks
## Week 7
- Run more time benchmarks
- Collate results and produce most important graphs and tables
## Week 8
- Run memory benchmarks
- Write up results and perform analysis
## Week 9
- Write up evaluation
## Week 10
- Editing and Review of report

# Two K-Center problems:
Discrete and continuous

