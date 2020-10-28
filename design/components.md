# Componenet Breakdown

## Solution Verifier
- O(nk)
  - Given the solution radius
  - loop through whole data set, check which center it belongs to. Sum the occurences for the M classes and verify that for all M classes, the coverage requirement is met.

## Synthetic data set generator
- α-sepearted and non α-sepearted graphs (A Constant Approximation for Colorful k-Center,
 Bandyapadhyay et al.)
- use known generating centers and uniformly distribute the points at max radius R around it
- 50 clusters is considered a "large" data set (A Genetic Algorithm Using Hyper-Quadtrees
for Low-Dimensional K-means Clustering, Laszlo  and Mukherjee)

## Graph visualisation
- Forwards and Backwards button for algorithm stepping
- Toggle colours for demographics
- Toggle cluster rings for centers
- Allow solver to add a custom label to step (will be useful for when step isn't obvious what it is trying to do e.g. Solving the decision problem from LP1 Bandyapadhyay et al.)