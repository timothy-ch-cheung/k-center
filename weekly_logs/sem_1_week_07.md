# Week 7
Summary: Created a program which generates Colourful K-Center problems with a known optimal solution. Benchmarked the three algorithms on instances of sizes 100, 1000 and 5000.

## Development
- Integrated the react app and flask server. Program now sends problem instances from flask which are displayed by D3. 
    - React client sends a POST request with the problem and parameters it wants to solve and the server returns a graph for it to render
    - Solution also contains the time it took to find the solution
- replaced the linear searches in greedy_reduce and constant_colourful algorithms with binary search algorithms.


## Testing
- unit testing [repo now at 51 tests, 97% coverage]
- for greedy and greedy_reduce, the majority of the running time was taken by calculating the weight cost for graph (This time isn't counted in the benchmark as it is the same cost for all three algorithms)
- larger data sets such as 5200 nodes took 1 hour 21 minutes to solve with a complete binary search. 
    - LP1 is very expensive to run, taking about 3 minutes for the 5200 node instance with the binary search taking 25 splits (log(n<sup>2</sup>)) to complete
    - I modifed the binary search to run sqrt(log(n)) (5 splits) and log(n) (13 splits). 5 splits wasn't very good as it couldn't converge to the optimal cost. 13 was much better
    - Found the constant-colourful algorithm is heavily reliant on a good "guess" of the optimal otherwise it will produce solutions with higher costs than greedy. 

## Difficulties
From testing the Constant Colourful algorithm (Bandyapadhyay et al.), I found that I hadn't implemented the part of the algorithm which solves α-separated instances so some problem instances don't give a solution. I will have to go back and implement that (and read the reference papers to understand the maths)