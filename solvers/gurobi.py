from gurobipy import Model, LinExpr, GRB
from time import thread_time_ns as thread_time

class Solver:
    def __init__(self, env, solve_method):
        self.available_methods = ['Pl', 'DualPl']
        self.solve_method = solve_method

        if self.solve_method=='Pl':
            self.solver = GurobiSolverPL(env)
        else:
            self.solver = GurobiSolverPLDual(env)

    def build(self):
        self.solver.build()

    def run(self):
        self.solver.run()
        self.total_time = self.solver.total_time        

class GurobiSolverPL:
    def __init__(self, env) -> None:
        self.env = env
        self.model = Model("MDP")
        self.model.setParam('OutputFlag', 0)
        self.model.setParam(GRB.Param.Threads, 1)
        self.model.setParam('LogToConsole', 0)
        self.__name__ = 'GurobiSolverPL'
    
    def build(self):
        start_time = thread_time()
        self.var = []
        for _ in range(self.env.S):
            self.var.append(self.model.addVar(vtype=GRB.CONTINUOUS, lb=0))
        self.model.update()
        self.obj = LinExpr()
        for i in range(self.env.S):
            self.obj += self.var[i]/self.env.S
        self.model.setObjective(self.obj,GRB.MINIMIZE)
        for i in range(self.env.S):
            for j in range(self.env.A):
                total = 0
                for k in range(self.env.S):
                    total = total + self.env.gamma*self.env.P[j,i,k]*self.var[k]
                self.model.addConstr( self.var[i] >= self.env.R[i,j] + total, "Contrainte%d" % i)

        self.building_time = thread_time()-start_time

    def run(self):
        self.model.optimize()
        self.total_time = self.model.Runtime + self.building_time
        assert GRB.OPTIMAL == 2

class GurobiSolverPLDual:
    def __init__(self, env) -> None:
        self.env = env
        self.model = Model("MDP")
        self.model.setParam('OutputFlag', 0)
        self.model.setParam(GRB.Param.Threads, 1)
        self.model.setParam('LogToConsole', 0)
        self.__name__ = 'GurobiSolverPLDual'
    
    def build(self):
        start_time = thread_time()

        self.var = {}
        for s in range(self.env.S):
            for a in range(self.env.A):
                self.var[(s, a)] = self.model.addVar(vtype=GRB.CONTINUOUS, lb=0.0)
        
        self.model.update()

        self.obj = LinExpr()

        for s in range(self.env.S):
            for a in range(self.env.A):
                self.obj += self.env.R[s, a]*self.var[(s, a)]
    
        self.model.setObjective(self.obj,GRB.MAXIMIZE)

        for s in range(self.env.S):
            sum_1 = 0
            for a in range(self.env.A):
                sum_1 += self.var[(s, a)]
            sum_2 = 0
            for a in range(self.env.A):
                for sp in range(self.env.S):
                    sum_2 += self.env.P[a, s, sp]*self.var[(sp, a)]
            mu = 1/self.env.S
            self.model.addConstr(sum_1 - self.env.gamma * sum_2 == mu, "Contrainte%d" % s)

        self.building_time = thread_time()-start_time

    def run(self):
        self.model.optimize()
        self.runtime = self.model.Runtime
        self.total_time = self.runtime + self.building_time
        assert GRB.OPTIMAL == 2
