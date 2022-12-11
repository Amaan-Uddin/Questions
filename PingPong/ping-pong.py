# complexity of the program: O(n)

direction = True # right
count = 0
pp_value = 1
index = 1

def num_eight(num):
    global count
    k = num % 10
    if k == 8:
        count += 1
    if k == 0:
        return count
    return num_eight(num//10)

def ping_pong(num):
    global direction,pp_value,count,index

    count = 0
    check_eight = num_eight(index)
    print(f"Index: {index} , Ping-Pong Value: {pp_value}")

    if index == num:
        return pp_value
        
    if (index % 8 == 0) or (check_eight >= 1):
        if direction:
            direction = False # left
        else: 
            direction = True # right

    if direction:
        pp_value += 1
    else:
        pp_value -= 1

    index = index+1
    return ping_pong(num)

num = 73
print(ping_pong(num))