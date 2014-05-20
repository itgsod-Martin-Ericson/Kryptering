def encrypt(cleartext, offset):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    crypto_string = ""
    cleartextupper = cleartext.upper()
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')
    for character in cleartextupper:
        if character == " ":
            crypto_string = crypto_string + " "
        else:
            clear_index = alphabet.index(character)
            crypto_index = clear_index + offset
            while crypto_index >= 26:
                crypto_index = crypto_index - 26
            crypto_letter = alphabet[crypto_index]
            crypto_string = crypto_string + crypto_letter
    return(crypto_string)

def decrypt(cleartext, offset):
    return encrypt(cleartext, -offset).lower()