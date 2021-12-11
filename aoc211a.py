depth_list = open("aoc211a.txt","r").read().split('\n')
print (depth_list)

count = 0
count_two = 0
count_twofail = 0

list = len(depth_list)
listtwo = len(depth_list)
listthree = len(depth_list)

print (list)
for i in depth_list:
    if int(depth_list[list-1]) > int(depth_list[list-2]):
        count += 1
        list -= 1
    else:
        list -= 1
    
print (count)

list_two = list-1
for i in range (1 , listtwo):
    if int(depth_list[list_two]) > int(depth_list[list_two - 1]):
        count_two += 1
        list_two -= 1

    else:
        count_twofail +=1
        list_two -= 1

print(count_two)
print (count_twofail)

ind = 0
count_three = 0
for i in range (1, listthree-2):
    b = int(depth_list[ind+1]) + int(depth_list[ind+2]) + int(depth_list[ind+3])
    a = int(depth_list[ind]) + int(depth_list[ind +1]) + int(depth_list[ind+2])
    if int(b) > int(a):
        count_three += 1
        ind += 1
    else:
        ind +=1
        
print (count_three)
    
    