# give the table_min
import pandas as pd
from copy import deepcopy
pd.set_option('mode.chained_assignment', None)

table = pd.DataFrame([[13, 79, 23, 71, 60, 27, 2],
         [31, 13, 14, 94, 60, 61, 57],
         [17, 1, None, 23, 36, 8, 86],
         [19, 28, 10, 4, 58, 73, 40],
         [94, 75, None, 58, None, 68, 46],
         [8, 24, 3, 32, 4, 94, 89],
         [10, 57, 13, 1, 92, 75, 29],
         [80, 17, 38, 40, 66, 25, 88]])

table_min = deepcopy(table)
table_max = deepcopy(table)
table_suf = deepcopy(table)

#intialize machines with zeros
final_min = { "machine0":[], "machine1" : [], "machine2" : [], "machine3" : [], "machine4" : [], "machine5" : [], "machine6" : [] }
final_max = { "machine0":[], "machine1" : [], "machine2" : [], "machine3" : [], "machine4" : [], "machine5" : [], "machine6" : [] }
final_suff = { "machine0":[], "machine1" : [], "machine2" : [], "machine3" : [], "machine4" : [], "machine5" : [], "machine6" : [] }

# find the minimum of the table_min and its index
tasks_min = [0, 1, 2, 3, 4, 5, 6, 7]
machines = 7
loops_min = 8
print("Initial table_min")
print(table_min)
while loops_min>0:
    minimum = table_min[0][tasks_min[0]]
    for x in range (0,machines):
        for y in range(0, len(tasks_min)):
            if table_min[x][tasks_min[y]]<minimum:
                min_index_machine = x
                min_index_task = tasks_min[y]
                minimum = table_min[x][tasks_min[y]]
    print("")
    print("minimum-{},\t machine-{}\t, task-{}".format(minimum, min_index_machine, min_index_task))
    
    # update the table_min with task min
    temp = "machine"+str(min_index_machine)
    final_min[temp].append("Task"+str(min_index_task))
    print("final_min-", final_min)
    
    #delete the task
    for x in range(0,len(tasks_min)):
        table_min[min_index_machine][tasks_min[x]] = table_min[min_index_machine][tasks_min[x]] +minimum
    tasks_min.remove(min_index_task)
    table_min = table_min.drop(min_index_task, axis=0)
    print("")
    print("")
    print("After deleting")
    print(table_min)
    print("")
    loops_min = loops_min- 1
print(final_min)



print("")
print("")
print("Max-Min start here")
print("")
print("")
print("")

loops_max = 8
tasks_max = [0, 1, 2, 3, 4, 5, 6, 7]
maximum_table = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
print("intial table")
print(table_max)
while loops_max>0:
    for x in range(0, len(tasks_max)):
        maximum = table_max[0][tasks_max[x]]
        maximum_table[0][tasks_max[x]] = maximum
        maximum_table[1][tasks_max[x]] = tasks_max[x]
        maximum_table[2][tasks_max[x]] = 0
        for y in range(0, machines):
            if table_max[y][tasks_max[x]] < maximum:
                maximum = table_max[y][tasks_max[x]]
                maximum_table[0][tasks_max[x]] = maximum
                maximum_table[2][tasks_max[x]] = y
                
    print("")
    print("min for each task corresponding tasks and machines", maximum_table)
    maximum_of_table = max(maximum_table[0])
    max_index_task = maximum_table[0].index(maximum_of_table)
    max_index_machine = maximum_table[2][max_index_task]
    print("maximum-{},\t machine-{},\t task-{}".format(maximum_of_table, max_index_machine, max_index_task))
    
    # update the table_min with task max
    temp = "machine"+str(max_index_machine)
    final_max[temp].append("Task"+str(max_index_task))
    print("final max", final_max)

    #delete the task
    maximum_table[0][max_index_task] = 0
    for x in range(1,3):
        maximum_table[x][max_index_task] = None
    for x in range(0,len(tasks_max)):
        table_max[max_index_machine][tasks_max[x]] = table_max[max_index_machine][tasks_max[x]] + maximum_of_table
    tasks_max.remove(max_index_task)
    table_max = table_max.drop(max_index_task, axis=0)
    print("")
    print("")
    print("after dropping the task")
    print(table_max)
    print("")
    loops_max -=1
print(final_max)
print("")



print("")
print("")
print("")
print("sufferage start here")
print("")
print("")

loops_suf = 8
tasks_suf = [0, 1, 2, 3, 4, 5, 6, 7]
sufferage_table = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
print("intial table")
print(table_suf)
while loops_suf>0:
    for x in range(0, len(tasks_suf)):
        temp = []
        maximum = table_suf[0][tasks_suf[x]]
        sufferage_table[0][tasks_suf[x]] = maximum
        sufferage_table[1][tasks_suf[x]] = tasks_suf[x]
        sufferage_table[2][tasks_suf[x]] = 0
        for y in range(0, machines):
            try:
                temp.append(int(table_suf[y][tasks_suf[x]]))
            except:
                pass
            if table_suf[y][tasks_suf[x]] < maximum:
                maximum = table_suf[y][tasks_suf[x]]
                sufferage_table[0][tasks_suf[x]] = maximum
                sufferage_table[2][tasks_suf[x]] = y
        temp.sort()
        difference = temp[1]- temp[0]
        sufferage_table[3][tasks_suf[x]] = difference
                
    print("")
    print("min for each task corresponding tasks and machines", sufferage_table)
    maximum_of_suff = max(sufferage_table[3])
    max_index_task = sufferage_table[3].index(maximum_of_suff)
    minimum_of_table = sufferage_table[0][max_index_task]
    max_index_machine = sufferage_table[2][max_index_task]
    print("minimum - {},\t maximum-{},\t machine-{},\t task-{}".format(minimum_of_table, maximum_of_suff, max_index_machine, max_index_task))
    
    # update the table_min with task max
    temp1 = "machine"+str(max_index_machine)
    final_suff[temp1].append("Task"+str(max_index_task))
    print("final max", final_suff)

    #delete the task
    sufferage_table[0][max_index_task] = 0
    sufferage_table[3][max_index_task] = 0
    for x in range(1,3):
        sufferage_table[x][max_index_task] = None
    for x in range(0,len(tasks_suf)):
        table_suf[max_index_machine][tasks_suf[x]] = table_suf[max_index_machine][tasks_suf[x]] + minimum_of_table
    tasks_suf.remove(max_index_task)
    table_suf = table_suf.drop(max_index_task, axis=0)
    print("")
    print("")
    print("after dropping the task")
    print(table_suf)
    print("")
    loops_suf -=1
print(final_suff)
print("")
