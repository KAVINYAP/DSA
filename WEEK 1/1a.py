def countdown(n):
    if n == 0:
       print("Rocket Launched");
    else:
         print(n)
         countdown(n - 1)
    
i=int(input("Enter the countdown time"))
countdown(i)
