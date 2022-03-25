import numpy as np
from operator import itemgetter, attrgetter
import matplotlib.pyplot as plt
import random


def fit_fun(x):  # 适应函数
    fitness = -np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi)))
    return fitness


class Unit:
    # 初始化
    def __init__(self, x_min, x_max, dim):
        self.__pos = np.array([x_min + random.random() * (x_max - x_min) for i in range(dim)])
        self.__mutation = np.array([0.0 for i in range(dim)])   # 个体突变后的变量
        self.__crossover = np.array([0.0 for i in range(dim)])  # 个体交叉后的向量
        self.__px = 0  # 个体被选中的概率
        self.__qx = 0  # 累计概率
        self.__fitnessValue = fit_fun(self.__pos)  # 个体适应度

    def __repr__(self):
        return repr([self.__pos, self.__fitnessValue])

    def set_pos(self, i, value):
        self.__pos[i] = value

    def get_pos(self):
        return self.__pos

    def set_mutation(self, i, value):
        self.__mutation[i] = value

    def get_mutation(self):
        return self.__mutation

    def set_crossover(self, i, value):
        self.__crossover[i] = value

    def get_crossover(self):
        return self.__crossover

    def set_qx(self, value):
        self.__qx = value

    def get_qx(self):
        return self.__qx

    def set_fitness_value(self, value):
        self.__fitnessValue = value

    def get_fitness_value(self):
        return self.__fitnessValue


class GA:
    def __init__(self, dim, size, iter_mun, x_min, x_max, best_fitness_value=float('Inf'), F=0.5, CR=0.9):
        self.dim = dim
        self.size = size
        self.iter_num = iter_mun
        self.x_min = x_min
        self.x_max = x_max
        self.best_fitness_value = best_fitness_value
        self.best_pos = [0.0 for i in range(dim)]
        self.F = F
        self.CR = CR
        self.fitness_val_list = []  # 每次迭代最优适应值

        # 对种群初始化
        self.unit_list = [Unit(self.x_min, self.x_max, self.dim) for i in range(self.size)]

    def get_best_pos(self):
        return self.best_pos

    def set_best_pos(self, i, value):
        self.best_pos[i] = value

    def set_best_fitness_value(self, value):
        self.best_fitness_value = value

    def get_best_fitness_value(self):
        return self.best_fitness_value



    # 随机选择
    def selection_random(self):
        return np.random.choice(self.unit_list, 2)

    # 轮盘选择
    def selection(self):
        sum_fitness = sum(unit.get_fitness_value() for unit in self.unit_list)

        qx = 0
        for unit in self.unit_list:  # 计算累计概率
            if unit.get_qx() == 0:
                qx = qx + unit.get_fitness_value() / sum_fitness
                unit.set_qx(qx)

        chosen = []
        while(len(chosen) < 2):
            benchmark = [random.random() for i in range(self.size)]
            # print(benchmark)
            i = 0
            for unit in self.unit_list:
                if benchmark[i] < unit.get_qx():
                    chosen.append(unit)
                    break
                i += 1
        return chosen

    # 结合/交叉
    def crossover(self, parent1, parent2):
        corossover_dim1 = random.randrange(0, self.dim)
        corossover_dim2 = random.randrange(0, self.dim)

        for i in range(self.dim):
            if min(corossover_dim1, corossover_dim2) <= i <= max(corossover_dim1, corossover_dim2):
                parent1.set_crossover(i, parent1.get_pos()[i])
                parent2.set_crossover(i, parent2.get_pos()[i])
            else:
                parent1.set_crossover(i, parent2.get_pos()[i])
                parent2.set_crossover(i, parent1.get_pos()[i])
        # print(parent1, parent2)

        return parent1, parent2

    def mutation(self, mutation_individual):
        mutation_dim = random.randrange(0, self.dim)
        mutation_value = random.randrange(self.x_min, self.x_max + 1)
        mutation_individual.set_mutation(mutation_dim, mutation_value)

        return mutation_individual

    def update(self):
        for i in range(self.iter_num):
            # parent1, parent2 = self.selection_random()
            select_pop = self.selection()
            parent1 = select_pop.pop(0)
            parent2 = select_pop.pop(0)
            if np.random.random() <= self.CR:
                child1, child2 = self.crossover(parent1, parent2)

                fitness1 = fit_fun(child1.get_crossover())
                if fitness1 < child1.get_fitness_value():
                    child1.set_fitness_value(fitness1)
                    for i in range(self.dim):
                        child1.set_pos(i, child1.get_crossover()[i])

                fitness2 = fit_fun(child2.get_crossover())
                if fitness2 < child2.get_fitness_value():
                    child2.set_fitness_value(fitness2)
                    for i in range(self.dim):
                        child2.set_pos(i, child2.get_crossover()[i])

            if random.random() <= self.F:
                select_pop = self.selection()
                mutation_individual = select_pop.pop(0)
                fitness = fit_fun(mutation_individual.get_mutation())
                if fitness < mutation_individual.get_fitness_value():
                    mutation_individual.set_fitness_value(fitness)
                    for i in range(self.dim):
                        mutation_individual.set_pos(i, mutation_individual.get_mutation()[i])

            for unit in self.unit_list:
                if unit.get_fitness_value() < self.get_best_fitness_value():
                    self.set_best_fitness_value(unit.get_fitness_value())
                    for i in range(self.dim):
                        self.set_best_pos(i, unit.get_pos()[i])
            self.fitness_val_list.append(self.get_best_fitness_value())
        return self.fitness_val_list, self.get_best_pos()



if __name__ =='__main__':
    dim = 2
    size = 100
    iter_num = 100
    x_max = 10
    x_min = -10

    ga = GA(dim, size, iter_num, x_min, x_max)
    fit_var_list2, best_pos2 = ga.update()
    print("GA最优位置:" + str(best_pos2))
    print("GA最优解:" + str(fit_var_list2[-1]))
    plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list2, c="g", alpha=0.5, label="GA")

    plt.legend()  # 显示lebel
    plt.show()