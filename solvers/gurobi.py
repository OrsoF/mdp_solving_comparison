from gurobipy import Model, LinExpr, GRB

from time import thread_time_ns as thread_time

class SolverPL:
    def __init__(self, env):
        self.env = env

        assert len(self.env.P.shape)==3
        assert len(self.env.R.shape)==2
        assert self.env.P.shape[1]==self.env.P.shape[2] and self.env.P.shape[1]==self.env.R.shape[0]
        assert self.env.P.shape[0]==self.env.R.shape[1]

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
    def __init__(self, env):
        self.env = env

        start_time = thread_time()

        self.model = Model("MDP")
        self.model.setParam('OutputFlag', 0)
        self.model.setParam(GRB.Param.Threads, 1)
        self.model.setParam('LogToConsole', 0)
        self.var = {}
        for s in range(self.env.S):
            for a in range(self.env.A):
                self.var[(s, a)] = self.model.addVar(vtype=GRB.CONTINUOUS)
        
        self.model.update()

        self.obj = LinExpr()

        for s in range(self.env.S):
            for a in range(self.env.A):
                self.obj += self.env.R[s, a]*self.var[(s, a)]
    
        self.model.setObjective(self.obj,GRB.MINIMIZE)

        for s in range(self.env.S):
            sum_1 = 0
            for a in range(self.env.A):
                sum_1 += self.var[(s, a)]
            sum_2 = 0
            for a in range(A):
                for sp in range(S):
                    sum_2 += self.env.P[a, s, sp]*self.var[(sp, a)]
            mu = 1/self.env.S
            self.model.addConstr(sum_1 - self.env.gamma * sum_2 == mu, "Contrainte%d" % s)

        self.building_time = thread_time()-start_time

        self.model.optimize()

        self.runtime = self.model.Runtime


# class SolverPLDual:
#     def __init__(self):
#         self.env = None

def g_pl_dual(env):
    solver = SolverPL(env)
    return solver.building_time, solver.runtime