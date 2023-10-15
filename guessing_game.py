#GUESSING_GaMe
def guess_number(lower,upper):
    if lower == upper:
        return lower

    mid = (lower+upper) // 2
    guess = input(f"Is the guessed number lesser, equal to, or higher than {mid}? (l/e/h): ")
    if guess in ['l','L']:
        return guess_number(lower,mid - 1)
    elif guess in ['e','E']:
        return mid
    elif guess in ['h','H']:
        return guess_number(mid + 1,upper)
    else:
        print("!...Invalid Guess...!")
        return None

#_main_
lower = int(input("Enter a Lower bound value : "))
upper = int(input("Enter a Upper bound value : "))
guessed_number = guess_number(lower,upper) #calling the function
if guessed_number is not None:
    print(f'The guessed number is {guessed_number} ')
else :
    print("The number couldn't be guessed")
