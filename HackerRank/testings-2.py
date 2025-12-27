if __name__ == '__main__':
    N = int(input())
    list = []
    com = []
    
    for i in range(0,N):
        com = [str(x) for x in input().split(" ")]
        
        if com[0] == "insert":
            list.insert(int(com[1]),int(com[2]))
        elif com[0] == "append":
            list.append(int(com[1]))
        elif com[0] == "remove":
            list.remove(int(com[1]))
        elif com[0] == "sort":
            list.sort()
        elif com[0] == "pop":
            list.pop()
        elif com[0] == "reverse":
            list.reverse()
        elif com[0] == "print":
            print(list)
        else:
            pass
        