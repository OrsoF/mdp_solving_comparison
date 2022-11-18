# Benchmark for solving MDP with tabular methods

## Installation

- Clone this repository with git
- 'pip install -r /Requirements.txt'

Fully working under Ubuntu 20.04, requires gurobi license to fullfil all tests.

## Run benchmark

- Run main.py

## Summary

We aim here to compare three MDP solving methods in terms of computing time :
- MdpToolbox
- Linear Programming solving with GurobiPy
- Marmot

To Do:
- Fix Max Iter to compare
- Fix Epsilon for all solvers
- Add Taxi and change Gurobi to a premium license
- Add Ex40
- Fork MdpToolbox
- Add other PI and VI methods
- Compare value functions at the end to ensure same result

Notes :
- MdpToolbox fails to solve two environments
- MdpToolbox convert sparse matrices to dense ones, and cannot gain times over Marmot


