need_to_sort=[5,9,8,6,7,4,3]

for a in range(len(need_to_sort)):
    for b in range(len(need_to_sort)):
        if need_to_sort[a] < need_to_sort[b]:
            temp=need_to_sort[a]
            need_to_sort[a]=need_to_sort[b]
            need_to_sort[b]=temp
            print(need_to_sort)



    