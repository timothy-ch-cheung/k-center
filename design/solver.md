# Solver design

## Packages
- NetworkX
- Numpy
- Pyomo

## requirements
- Two operation modes
  - Solve (compute whole solution)
  - Step (step through the solution - for visualisation purposes)

### Step mode
either:
- step through the algorithm
- solve algorithm and keep a log of each step - not such a good idea as each step could take a long time and user would have to wait

## parameters
- constraints
- k
- graph (NetworkX)

## return
set of centers
