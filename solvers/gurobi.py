from gurobipy import Model, LinExpr, GRB

from time import thread_time_ns as thread_time

class SolverPL:
    def __init__(self, env):
        self.env = env

        start_time = thread_time()

        self.model = Model("MDP")
        self.model.setParam('OutputFlag', 0)
        self.model.setParam(GRB.Param.Threads, 1)
        self.model.setParam('LogToConsole', 0)
        self.var = []
        for _ in range(self.env.S):
            self.var.append(self.model.addVar(vtype=GRB.CONTINUOUS))
        
        self.model.update()

        self.obj = LinExpr()

        for i in range(self.env.S):
            self.obj += self.var[i]/self.env.S
    
        self.model.setObjective(self.obj,GRB.MINIMIZE)

        for i in range(self.env.S):
            for j in range(self.env.A):
                total = 0
                for k in range(self.env.S):
                    total = total + self.env.gamma*self.env.P[j][i,k]*self.var[k]
                self.model.addConstr( self.var[i] >= self.env.R[i,j] + total, "Contrainte%d" % i)

        self.building_time = thread_time()-start_time

        self.model.optimize()

        self.runtime = self.model.Runtime

def g_pl(env):
    solver = SolverPL(env)
    return solver.building_time, solver.runtime

class SolverPLDual:
    def __init__(self):
        self.env = None

def g_pl_dual(env):
    solver = SolverPL(env)
    return solver.building_time, solver.runtime