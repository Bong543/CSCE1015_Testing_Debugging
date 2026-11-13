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
        
    if len(euid) == 6 or len(euid) == 7:
        return True
    else:
        return False
    

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
    if length == 6:
        letters = euid[:2]
        digits = euid[2:]
    elif length == 7:
        letters = euid[:3]
        digits = euid[3:]
    else:
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
