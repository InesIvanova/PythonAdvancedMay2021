def fact(n):
   if n == 1:
      return 1
   return n * fact(n - 1)

def say(n):
    if n == 0:
        return
    print("Hey")
    say(n-1)

say(5)