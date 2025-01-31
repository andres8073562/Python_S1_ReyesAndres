import random
import string

def contraseña_random(length=12, exclude_chars="", min_upper=1, min_lower=1, min_digits=1, min_symbols=1):
    upper = [random.choice(string.ascii_uppercase) for _ in range(min_upper)]
    lower = [random.choice(string.ascii_lowercase) for _ in range(min_lower)]
    digits = [random.choice(string.digits) for _ in range(min_digits)]
    symbols = [random.choice(string.punctuation) for _ in range(min_symbols)]
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    all_chars = ''.join(c for c in all_chars if c not in exclude_chars)
    
    if len(all_chars) == 0:
        raise ValueError("All characters are excluded. Cannot generate password")
    
    remaining_length = length - (min_upper + min_lower + min_digits + min_symbols)
    
    if remaining_length < 0:
        raise ValueError("Length is too short to meet minimum character requirements.")
    
    remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]
    
    password_list = upper + lower + digits + symbols + remaining_chars
    random.shuffle(password_list)
    
    return ''.join(password_list)

password = contraseña_random(length=16, exclude_chars="lIO0", min_upper=2, min_lower=2, min_digits=2, min_symbols=2)
print(password)
