def user_input(message):
    
    answer = input(message)
    
    if answer=='':
        return None
    
    else:
        return answer
        

"""def format_input(input_a, input_b):
    
    if input_a!=None:
        output_a = input_a.lower()
    else:
        output_a = input_a
        
    if input_b!=None:
        output_b = input_b.lower()
    else:
        output_b = input_b
        
    return output_a, output_b"""