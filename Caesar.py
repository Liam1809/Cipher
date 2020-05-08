# principle:
# if you want to decode, shift forwards
# if you want to encode, shift backwards

# function to encode message
def encoded(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    punctuation = "()~@#$%^&*-_+=/\"\<>.,?!:' "
    word_encoded = ""

    for letter in message:
        if not letter in punctuation:
             letter_index = alphabet.find(letter)
             word_encoded += alphabet[(letter_index - offset)% len(alphabet)]
        else:
             word_encoded += letter
    return word_encoded


# function to decode message
def decoded(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    punctuation = "()~@#$%^&*-_+=/\"\<>.,?!:' "
    word_decoded = ""
    for letter in message:
        if not letter in punctuation:
             letter_index = alphabet.find(letter)
             word_decoded += alphabet[(letter_index + offset) % len(alphabet)] 
        else:
             word_decoded += letter
    return word_decoded


# message and offset to encode
message1 = "Hello guys! My name is Liam. If you need me, call my phone number: 0755XXXXXXX"
offset = 10
print("Encoded message\n" + encoded(message1, offset))
# message to decode
message2 = encoded(message1, offset)
print("Decoded message\n" + decoded(message2, offset))



# # decode without knowing the shift value
# coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# # The easiest way to break this code is to simply brute force though all of the possible shifts.
# # We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can 
# # look through all of the outputs and look for the one that in english, and we've decoded our message!
# for i in range(26):
#     print("offset: " + str(i))
#     print("\t " + decoded(coded_message, i) + "\n")
