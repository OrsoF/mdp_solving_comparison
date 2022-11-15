# mdp_solving_comparison

Run main.py to launch the comparison.

We aim here to compare three MDP solving methods in terms of computing time :
- MdpToolbox
- Linear Programming solving with GurobiPy
- Marmot

To Do:
- Fix Max Iter to compare
- Fix Epsilon for all solvers
- Add Taxi and change Gurobi to a premium license
- Add Ex40

Notes :
- MdpToolbox fails to solve two environments
- MdpToolbox convert sparse matrices to dense ones, and cannot gain times over Marmot
