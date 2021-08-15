exp = input("please type the postfix expression : ")

from part import stack

obj = stack(len(exp))

def evaluatePostfix(exp):
                
    for i in exp:
        if i.isdigit():
            obj.push(i)
          
                    
        else:
            val1 = obj.pop()
            val2 = obj.pop()
            obj.push(str(eval(val2 + i + val1)))
          
    return int(obj.pop())

print(evaluatePostfix(exp))
