if __name__ == '__main__':
    s = input()
    
    # 1. Alphanumeric?
    print(any(char.isalnum() for char in s))
    
    # 2. Alphabetical?
    print(any(char.isalpha() for char in s))
    
    # 3. Digits?
    print(any(char.isdigit() for char in s))
    
    # 4. Lowercase?
    print(any(char.islower() for char in s))
    
    # 5. Uppercase?
    print(any(char.isupper() for char in s))
