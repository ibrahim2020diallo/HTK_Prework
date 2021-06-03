def seperate_list(names_list):
    
    even_list = []
    odd_list = []
    
    for i in names_list:
       
        if len(i) % 2 == 0:
            
            even_list.append(i)
      
        else:
            
            odd_list.append(i)
    
    for j in range(len(even_list)):
        
        even_list[j] = 'b' + even_list[j][1:]
    
    for k in range(len(odd_list)):
        
        odd_list[k] = odd_list[k][:-1] + 'a #c'
    
    print("Even list = ", even_list)
    print("Odd list = ", odd_list)
    
    return even_list

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
