# Benchmark for solving MDP with tabular methods

## Installation

- Clone this repository with git
- 'pip install -r /Requirements.txt'
- Install Gurobi solver with a license

Fully working under Ubuntu 20.04, requires gurobi license to fullfil all tests.

## Run benchmark

- Run main.py

## Summary

We aim here to compare three MDP solving methods in terms of computing time :
- MdpToolbox (VI, VIGS, PI, PIM)
- Marmot (VI, VIGS, PI, PIM)
- Linear Programming solving with GurobiPy

To Do:
- Fix Max Iter to compare
- Fix Epsilon for all solvers
- Compare value functions at the end to ensure same result
- Add Grid nxn four rooms
- Add parallelized policy iteration
- Add dual for linear solver
- Add new instances of environments (Blackjack, Cliff Walking, programmation contest 2000)
- Air campaign planning problem https://www.aaai.org/Papers/AAAI/1998/AAAI98-023.pdf
- 2048 2x2, 3x3
- Grid nxn

Notes :
- MdpToolbox convert sparse matrices to dense ones, and cannot gain times over Marmot
- MDP Solving is limited relatively to S. Partially Observable MDP ?


