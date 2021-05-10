def modify_sentence(sentence, character):
    new_sentence = ""
    for c in sentence:
        if c == character:
            new_sentence = new_sentence + "-"
        else:
            new_sentence = new_sentence + c
    return new_sentence


sentence = input("Frase:")
character = input("Carácter:")

print(modify_sentence(sentence, character))
