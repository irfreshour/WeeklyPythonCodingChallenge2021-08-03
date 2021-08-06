def fizz_buzz(num: int) -> str:
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(num)
    return output

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))