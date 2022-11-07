from gurobipy import Model, LinExpr, GRB

class GurobiSolver:
    def __init__(self, env):
        self.env = env
        self.model = Model("MDP")
        self.model.setParam('OutputFlag', 0)
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

        self.model.optimize()

        def show_solution(self):
            print("")                
            print('Solution optimale:')
            for i in range(self.env.S):
                    print('v%d'%(i+1), '=', self.var[i])
