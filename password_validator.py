# Project Name: Password Strength Validator

print("\n" + "=" * 45)
print("--- Welcome to Password Strength Validator ---")
print("=" * 45)
print("\nA strong password needs: 8+ characters,\nuppercase, lowercase, numbers, and symbols.\n")


while True:
    password = input("\nEnter your password (or type 'quit' to exist): ")

    if password.lower() == 'quit':
        print("You are exist the password validator.\nThank you so much for using our services.")
        break

    # Make some variable to check password conditions
    has_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Now we check lenght using string functions
    if len(password) >= 8:
        has_digit = True

    # Now we check each character line by line
    for chr in password: # Chr means: Character
        if chr.isupper():
            has_upper = True
        elif chr.islower():
            has_lower = True
        elif chr.isdigit():
            has_digit = True
        elif not chr.isalnum():
            has_special = True

    score = 0
    if has_length: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    # Output the result
    print("\nResult:")
    print(f"Evaluatig: '{password}'")

    match score:
        case 5:
            print("Strong Passowrd: No Needs to improvement!")
        case 3 | 4:
            print("Moderate Password: little needs improvement!")
        case _:
            print("Weak Password: Your password is very simple!")