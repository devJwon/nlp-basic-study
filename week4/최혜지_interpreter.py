def main() :
    expression = input("Enter an arithmetic expression 'x y z' (x and z is number, y is mathematical symbols) : ")
    x_str, operator, z_str = expression.split() 
    
    x = int(x_str)
    z = int(z_str)
    
    if operator == "+" :
        result = x + z
    elif operator == "-" :
        result = x - z
    elif operator == "*" :
        result = x * z
    elif operator == "/" :
        result = x / z
    else :
        raise ValueError("Unsupported operator")
        # result = ValueError("unsupported")
        # print(result)
    
    print(f"{result: .1f}")

main()