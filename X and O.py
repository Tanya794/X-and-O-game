lst = [["*" for i in range(4)] for j in range (4)]

def show(A):
    for j in lst:
        for i in j:
            print(i, end = " ")
        print()

lst[0][0] = " "
lst[1][0] = 1
lst[2][0] = 2
lst[3][0] = 3
lst[0][1] = "a"
lst[0][2] = "b"
lst[0][3] = "c"

show(lst)

step = 1

while step < 10:

    if step % 2 != 0:
        player = input("Player 1 (буква цифра): ")

        if player == "a1":
            if lst[1][1] == "*":
                lst[1][1] = "X"
                step += 1
                show(lst)
            else:
                continue
       
            
        elif player == "a2":
            if lst[2][1] == "*":
                lst[2][1] = "X"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "a3":
            if lst[3][1] == "*":
                lst[3][1] = "X"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b1":
            if lst[1][2] == "*":
                lst[1][2] = "X"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b2":
            if lst[2][2] == "*":
                lst[2][2] = "X"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b3":
            if lst[3][2] == "*":
                lst[3][2] = "X"
                step += 1
                show(lst)
            else:
                continue
        
        elif player == "c1":
            if lst[1][3] == "*":
                lst[1][3] = "X"
                step += 1
                show(lst)
            else:
                continue
        

        elif player == "c2":
            if lst[2][3] == "*":
                lst[2][3] = "X"
                step += 1
                show(lst)
            else:
                continue
        

        elif player == "c3":
            if lst[3][3] == "*":
                lst[3][3] = "X"
                step += 1
                show(lst)
            else:
                continue
    
    if step > 4:
        if (lst[1][1] == "X" and lst[1][2] == "X" and lst[1][3] == "X") or (lst [2][1] == "X" and lst[2][2] == "X" and lst[2][3] == "X") or (lst[3][1] == "X" and lst [3][2] == "X" and lst [3][3] == "X") or (lst[1][1] == "X" and lst [2][1] == "X" and lst [3][1] == "X") or (lst[1][2] == "X" and lst [2][2] == "X" and lst [3][2] == "X") or (lst[1][3] == "X" and lst [2][3] == "X" and lst [3][3] == "X") or (lst[1][1] == "X" and lst [2][2] == "X" and lst [3][3] == "X") or (lst[1][3] == "X" and lst [2][2] == "X" and lst [3][1] == "X"):
            print("Player 1 won!")
            raise SystemExit(0)

        elif (lst[1][1] == "O" and lst[1][2] == "O" and lst[1][3] == "O") or (lst [2][1] == "O" and lst[2][2] == "O" and lst[2][3] == "O") or (lst[3][1] == "O" and lst [3][2] == "O" and lst [3][3] == "O") or (lst[1][1] == "O" and lst [2][1] == "O" and lst [3][1] == "O") or (lst[1][2] == "O" and lst [2][2] == "O" and lst [3][2] == "O") or (lst[1][3] == "O" and lst [2][3] == "O" and lst [3][3] == "O") or (lst[1][1] == "O" and lst [2][2] == "O" and lst [3][3] == "O") or (lst[1][3] == "O" and lst [2][2] == "O" and lst [3][1] == "O"):
            print("Player 2 won!")
            raise SystemExit(0)
    

    if step % 2 == 0:
        player = input("Player 2 (буква цифра): ")

        if player == "a1":
            if lst[1][1] == "*":
                lst[1][1] = "O"
                step += 1
                show(lst)
            else:
                continue
       
            
        elif player == "a2":
            if lst[2][1] == "*":
                lst[2][1] = "O"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "a3":
            if lst[3][1] == "*":
                lst[3][1] = "O"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b1":
            if lst[1][2] == "*":
                lst[1][2] = "O"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b2":
            if lst[2][2] == "*":
                lst[2][2] = "O"
                step += 1
                show(lst)
            else:
                continue
       

        elif player == "b3":
            if lst[3][2] == "*":
                lst[3][2] = "O"
                step += 1
                show(lst)
            else:
                continue
        

        elif player == "c1":
            if lst[1][3] == "*":
                lst[1][3] = "O"
                step += 1
                show(lst)
            else:
                continue
        

        elif player == "c2":
            if lst[2][3] == "*":
                lst[2][3] = "O"
                step += 1
                show(lst)
            else:
                continue
        

        elif player == "c3":
            if lst[3][3] == "*":
                lst[3][3] = "O"
                step += 1
                show(lst)
            else:
                continue

    if step > 4:
        if (lst[1][1] == "X" and lst[1][2] == "X" and lst[1][3] == "X") or (lst [2][1] == "X" and lst[2][2] == "X" and lst[2][3] == "X") or (lst[3][1] == "X" and lst [3][2] == "X" and lst [3][3] == "X") or (lst[1][1] == "X" and lst [2][1] == "X" and lst [3][1] == "X") or (lst[1][2] == "X" and lst [2][2] == "X" and lst [3][2] == "X") or (lst[1][3] == "X" and lst [2][3] == "X" and lst [3][3] == "X") or (lst[1][1] == "X" and lst [2][2] == "X" and lst [3][3] == "X") or (lst[1][3] == "X" and lst [2][2] == "X" and lst [3][1] == "X"):
            print("Player 1 won!")
            raise SystemExit(0)

        elif (lst[1][1] == "O" and lst[1][2] == "O" and lst[1][3] == "O") or (lst [2][1] == "O" and lst[2][2] == "O" and lst[2][3] == "O") or (lst[3][1] == "O" and lst [3][2] == "O" and lst [3][3] == "O") or (lst[1][1] == "O" and lst [2][1] == "O" and lst [3][1] == "O") or (lst[1][2] == "O" and lst [2][2] == "O" and lst [3][2] == "O") or (lst[1][3] == "O" and lst [2][3] == "O" and lst [3][3] == "O") or (lst[1][1] == "O" and lst [2][2] == "O" and lst [3][3] == "O") or (lst[1][3] == "O" and lst [2][2] == "O" and lst [3][1] == "O"):
            print("Player 2 won!")
            raise SystemExit(0)        

print("The End!")
             
         