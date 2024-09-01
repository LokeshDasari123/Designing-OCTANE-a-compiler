i = 0
top = 0
stack = []
ip = []

def push(c):
    global top
    
    if top >= 20:
        print("Stack Overflow")
    else:
        stack.append(c)
        top += 1

def pop():
    global top
    
    if top < 0:
        print("Stack underflow")
    else:
        stack.remove(stack[top-1])
        top -= 1

def error():
    print("\n\nSyntax Error!!!! String is invalid\n")
    

def match(expected_token):
    global i
    
    if expected_token == ip[i]:
        print("\nMatched:", expected_token)
        i += 1
    else:
        
        error()

def VarDec():
    Type()
    VarList()
    I()
    match("#")

def Type():
    if ip[i] in ["inum", "dnum", "tf", "dub", "char", "str"]:
        match(ip[i])
    else:
        error()

def VarList():
    match("id")
    V()

def V():
    if ip[i] == ",":
        match(",")
        VarList()
    else:
        # V -> ~ (epsilon)
        pass

def I():
    match("=")
    Init()

def Init():
    if ip[i] == "int":
        Integers()
    elif ip[i] == "num.num":
        Decimals()
    elif ip[i] == "tf":
        match("tf")
    elif ip[i] == "id":
        String()
    else:
        error()

def Integers():
    match("int")

def Decimals():
    match("num.num")

def String():
    match("id")

print("The given grammar is\n\n")
print("Var dec -> <Type><Var list><I>#\n")
print("Type -> inum|dnum|tf|dub|char|str\n")
print("Var list -> id<V>\n")
print("V -> ,<Var list>|~\n")
print("I -> =<Init>\n")
print("Init -> Integers|Decimals|tf|String\n")
print("Integers -> int\n")
print("Decimals -> num.num\n")
print("String -> id\n\n")

ip = input("Enter the string to be parsed:\n")
ip += ' $'
ip=ip.split(' ')
print(ip)
n=len(ip)

push('$')
push('Var dec')



while i < n:
    
    if ip[i] == '$' and stack[top-1] == '$':
        print("\n\n Successful parsing of string \n")
        i+=30
    elif ip[i] == stack[top-1]:
        print("\nMatched:", ip[i])
        i += 1
        pop()
    else:
        if stack[top-1] == 'Var dec' and ip[i] in ["inum", "dnum", "tf", "dub", "char", "str"]:
            print("\nS -> <Type><Var list><I>")
            pop()
            push("#")
            
            
            
            push('I')
            push('Var list')
            push('Type')
            
        elif stack[top-1] == 'Type' and ip[i] in ["inum", "dnum", "tf", "dub", "char", "str"]:
            pop()
            Type()
        elif stack[top-1] == 'Var list' and ip[i] == 'id':
            print("\nVar list -> id<V>")
            pop()
            push('V')
            push('id')
        elif stack[top-1] == 'V' and ip[i] == ',':
            print("\nV -> ,<Var list>")
            pop()
            push('Var list')
            push(',')
        elif stack[top-1] == 'V' and ip[i] == '=':
            pop()
        elif stack[top-1] == 'I' and ip[i] == '=':
            print("\nI -> =<Init>")
            pop()
            push('Init')
            push('=')
        elif stack[top-1] == 'Init' and ip[i] == 'int' or stack[top-1] == 'Init' and ip[i] == 'num.num'  or stack[top-1] == 'Init' and ip[i] == 'id' or stack[top-1] == 'Init' and ip[i] == 'tf':
            print("\nInit -> Integers")
            pop()
            push('Integers')
        
        elif stack[top-1] == 'Integers' and ip[i] == 'int':
            pop()
            Integers()
        elif stack[top-1] == 'Integers' and ip[i] == 'num.num':
            pop()
            Decimals()
        elif stack[top-1] == 'Integers' and ip[i] == 'tf':
            pop()
            match('tf')
        elif stack[top-1] == 'Integers' and ip[i] == 'id':
            pop()
            String()
        elif stack[top-1] == 'Var list' and ip[i] == 'id':
            print("\nV -> <Var list>")
            pop()
            push('V')
            push('Var list')
        else:
            print(stack[top-1])
            print(ip[i])
            error()
