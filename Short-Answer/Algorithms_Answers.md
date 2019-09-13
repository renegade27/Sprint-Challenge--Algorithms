#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Time - O(n) Space - O(2)


b) Time - O(n^2) Space - O(3)


c) Time - O(n)

## Exercise II

# Function takes in n floors, eggs amount, and starts on floor f (bottom floor)

function eggDrop(n, eggs, f=0, cracked=0):
   # If we are on the top floor, we are obviously going to break an egg if we throw it
   # This will end the recursion and return the safest possible floor
   # So if we have 6 floors and you have this set of results
   # C = Cracked, N = Not Cracked
   # 0 - N, 1 - N, 2 - N, 3 - N, 4 - C, 5 - C, 6 - C
   # We have 3 cracked eggs, n = 6 & c = 3, n - c = 3. Thus 3rd Floor is deemed the safest top floor
   if f==n:
      return n - (cracked+1)
   // THROW EGG CODE //
   # After we throw our egg, check to see if it breaks, if so then decrement eggs and increment cracked
   if eggBroke:
      cracked -= 1 
      eggs -= 1
   # Recursively call function so we are moving up a floor each call
   eggDrop(n, eggs, f+1, cracked)

# eggDrop will run a total of n times, and isn't looped through each call/iteration
# which makes eggDrop have a run time of O(n)


