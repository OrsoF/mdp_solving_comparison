# Benchmark for solving MDP with tabular methods

## Installation

- Clone this repository with git
- 'pip install -r /Requirements.txt'

Fully working under Ubuntu 20.04, requires gurobi license to fullfil all tests.

## Run benchmark

- Run main.py

## Summary

We aim here to compare three MDP solving methods in terms of computing time :
- MdpToolbox (VI, VIGS, PI, PIM)
- Linear Programming solving with GurobiPy
- Marmot (VI, VIGS, PI, PIM)

To Do:
- Fix Max Iter to compare
- Fix Epsilon for all solvers
- Compare value functions at the end to ensure same result
- Add Grid nxn four rooms
- Add parallelized policy iteration
- Add dual for linear solver

Notes :
- MdpToolbox fails to solve two environments
- MdpToolbox convert sparse matrices to dense ones, and cannot gain times over Marmot


