from Categories.Toolbox.Commands.morse import decrypt, encrypt

def test_encrypt_valid():
    message = "HELLO"
    expected = ".... . .-.. .-.. --- "
    result = encrypt(message)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_encrypt_invalid_character():
    message = "HELLO$"
    result = encrypt(message)
    assert not result, f"Expected False, but got {result}"

def test_decrypt_valid():
    message = ".... . .-.. .-.. --- "
    expected = "HELLO"
    result = decrypt(message)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_decrypt_invalid():
    message = ".... . .-.. .-.. --- ###"
    result = decrypt(message)
    assert result == 'invalid', f"Expected 'invalid', but got {result}"