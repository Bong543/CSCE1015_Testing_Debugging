def validate_length(euid: str) -> bool:
    """
    Validate the length of the EUID.
    
    Args:
        euid: A string representing the EUID.

    Returns:
        bool: True if the length is valid, False otherwise.
        
    Rules:
    - Must be exactly 6 or 7 characters long.
    """
    if not isinstance(euid, str):
        return False
    return len(euid) in (6, 7)
    

def validate_contents(euid: str) -> bool:
    """
    Validate the structure and contents of the EUID.
    
    Args:
        euid: A string representing the EUID.

    Returns:
        bool: True if the contents are valid, False otherwise.
        
    Rules:
    - Starts with 2-3 lowercase letters.
    - Ends with exactly 4 digits.
    - Contains no special characters or uppercase letters.
    """
    if not isinstance(euid, str):
        return False
        
    length = len(euid)
    
    # Case 1: Length 6 (Must be 2 letters + 4 digits)
    if length == 6:
        letters = euid[:2]
        digits = euid[2:]
        return letters.isalpha() and letters.islower() and digits.isdigit()
        
    # Case 2: Length 7 (Must be 3 letters + 4 digits)
    elif length == 7:
        letters = euid[:3]
        digits = euid[3:]
        return letters.isalpha() and letters.islower() and digits.isdigit()
        
    return False
        
    
    return letters.islower() and letters.isalpha() and digits.isdigit()


def validate(euid: str) -> bool:
    return validate_length(euid) and validate_contents(euid)

if __name__ == "__main__":
    # Prompt the user for their EUID,
    euid = input("Please enter your EUID: ").strip()

    if validate(euid):
        print(f"'{euid}' is a valid EUID")
    else:
        print(f"'{euid}' is NOT a valid EUID")
