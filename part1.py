from itertools import *
import copy


def check_intersection(target,i):
    status = True
    for x in target:
        if not x.intersection(i):
            status = False
            break
        if len(x.intersection(i)) > 1:
            status = False
            break
    return status


def validate_quorums(processes):
    for key in processes.keys():
        status = check(key, processes)
        if status:
            print("Validation successful for {}".format(key))
            
        
def check(process_id, processes):
    status = True
    keys = processes.keys()
    quorum = set(processes.get(process_id))
    for key in keys:
        if key == process_id:
            continue
        q = set(processes.get(key))
        if not quorum.intersection(q):
            print("Validation failed for processes {} and {}".format(key, process_id))
            status = False
    return status


def generateCombinations(n,k):
    generated_combination = combinations([i for i in range(1,n+1)],k)
    combination_list = list(generated_combination)
    combination = [set(x) for x in combination_list]
    i = 1
    target = [combination.pop(0)]
    for x in combination:
        if i <= n and check_intersection(target, x):
            target.append(x)
            i=i+1
    return target


def MaekawasQuorums(n, k):
    target = generateCombinations(n,k)
    quorums = copy.copy(target)
    missing = []
    process_quorum = {}
    for i in range(1,n+1):
        status = False
        for q in quorums:
            if i in q:
                process_quorum[i] = q
                quorums.remove(q)
                status = True
                break
        if not status:
            missing.append(i)
    if len(missing) != 0:
        for miss in missing:
            for q in quorums:
                for p in q:
                    if miss in process_quorum.get(p):
                        process_quorum[miss] = process_quorum[p]
                        process_quorum[p] = q
                        quorums.remove(q)
                        missing.remove(miss)
                        break
    return process_quorum

process_quorum = MaekawasQuorums(21,5)
print(process_quorum, end="\n")
validate_quorums(process_quorum)
