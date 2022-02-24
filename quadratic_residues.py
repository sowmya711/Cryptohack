p = 29
ints = [14, 6, 11]
for i in range(1,29):
    val=(i*i)%29;
    for j in ints:
        if(val==j):
            print(i)