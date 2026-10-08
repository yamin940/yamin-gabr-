def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
print (seconds_to_hms(3661))

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)
print(celsius_to_fahrenheit(25))

def split_evenly(total, people):
    return total // people, total % people

print(split_evenly(17, 5))

def is_palindrome_word(word):
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]

print(is_palindrome_word("Radar"))
print(is_palindrome_word("Hello"))

def mask_email(email):
    at_index = email.index("@")
    return email[:2] + "*" * (at_index - 2) + email[at_index:]
print(mask_email("mohamed@gmail.com"))
print(mask_email("ahmed.ali@yahoo.com"))

def middle(values):
    return values[len(values) // 2]

print(middle([1, 2, 3, 4, 5]))

def rotate_left(values, k):
    shift = k % len(values)
    return values[shift:] + values[:shift]

print(rotate_left([1, 2, 3, 4, 5], 2))


def fib_list(n): 
    if n <= 0: 
        return [] 
    if n == 1: 
        return [0]

fibs = [0, 1]
while len(fibs) < n:
    fibs.append(fibs[-1] + fibs[-2])

    return fibs

print(fib_list(6))

def collatz_steps(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

print(collatz_steps(6))