from unittest import result


def pairs_mult(numbers):
    results=[]
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

mylist = [2,3,5,6]
print(pairs_mult(mylist))