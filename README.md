# Benchmark for solving MDP with tabular methods

## Installation

#### Mandatory

- Clone this repository with git
- 'pip install -r /Requirements.txt'

#### Optional :

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
- Compare value functions at the end to ensure same result
- Add parallelized policy iteration
- Add dual for linear solver
- Add new instances of environments (Blackjack, Cliff Walking, programmation contest 2000)
- Air campaign planning problem https://www.aaai.org/Papers/AAAI/1998/AAAI98-023.pdf
- 2048 2x2, 3x3
- Quels sont les concours de programmation 2000 ?
- Sparses matrices ?


Notes :
- MdpToolbox convert sparse matrices to dense ones, and cannot gain times over Marmot
- MDP Solving is limited relatively to S. Partially Observable MDP ?
- Voir avec les idées de Trystan
- valueIterationGS, policyIteration marmote is not implemented
- marmotePIM gives ValueIterationModified