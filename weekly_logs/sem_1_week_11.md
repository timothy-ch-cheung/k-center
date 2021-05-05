# Week 11:
Summary: Completed unit tests for PBS and put in place goals for Christmas break.

# Development
- Integrated PBS algorithm in solver part of the webapp
- No other progress - mostly working on assignments for ML/IDA and Real World Security this week

# Testing
- PBS algorithm unit tests [repo now at 76 tests, 97% coverage]
- Still seems to be some bugs for the 100 point test example, will need more investigation

# Goals over Christmas
Discussed with Rajesh and got feedback on my goals until our next weekly meeting (in order of priority):
- develop stepped visiualisations for GreedyReduce, and algorithm by Bandyapadhyay et al. [2 dev days]
- develop stepped visiualisation for PBS genetic algorithm - this will need a bit of design work since multiple potential solutions need to be visualised [5 dev days]
- memory and cpu profiling of each algorithm [3 dev days]
- Modify PBS to solve Colourful K-Center
        - Change cost function take into account of outliers (this will probably change it from O(n) O(n<sup>2</sup>))
        - Genetic operators need to account for cost (original PBS doesn't)
- Make a start of the skeleton of the report
- Attempt to implement solving exact perfect matching using pfaffians which is used to solve α-seperated instances of Colourful K-Center
