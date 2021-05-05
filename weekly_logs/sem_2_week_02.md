# Semester 2 Week 2 Log

## Progress of planned work
| Task                                                              | Progress              | 
| ----------------------------------------------------------------- | --------------------- | 
| Complete Implementation PBS that terminates when a cost is reached| completed             |
| Create file processors for ORLIB/TSPLIB                           | completed ORLIB       |
| benchmark performance of PBS (ORLIB/TSPLIB)                       | blocked - bugs found  |
| Implement brute force solver for Colourful K-Center problem       | completed             |
| write up for complexity/algorithm (brute force algorithms)        | in progress           |

## Difficulties
- while benchmarking the PBS algorithm on ORLIB:
  - Some problem instances won't converge to the optimal cost
  - The ones that do converge take significantly longer than the benchmarks on the paper by W. Pullan (despite using a much more recent processor)

## Extra unplanned work completed
- Added validation for input fields of web GUI (better user experience)
- Added explanation of how time prediction for brute force algorithms are calculated (gives context to the user rather than just giving them a number without explaining)
