def find_first_sum(nums, goal):
    seen = {} #Diccionario para guardar el numero y su indice

    for idx, value in enumerate(nums):
        missing = goal - value
        if missing in seen:return [seen[missing],idx]
        seen[value] = idx 
    
        print(f"index {idx} value: {value}")


nums = [0,1,2,3,4,5,6,7,8,9]
goal = 7
result = find_first_sum(nums,goal)
print(result)