# The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
       
#        Consider the message
       
#            barry is the spy

#        If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
       
#            dog
           
#        Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth. Remember, we zero-index because this is Python we're talking about!

#                     message:       b  a  r  r  y    i  s   t  h  e   s  p  y
            
#              keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
             
#       resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
  
#         So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
        
#             eoxum ov hnh gvb


# function to encode message
def vigenere_encode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    punctuation = "()~@#$%^&*-_+=/\"\<>.,?!:' "
    # convert message into keyword phrase
    index_keyword = 0
    keyword_string = ""
    for letter in message:
        if not letter in punctuation:
            keyword_string += keyword[index_keyword]
            index_keyword = (index_keyword + 1) % len(keyword)
        else:
            keyword_string += letter 
    # start to decode based on the range between two characters in aplhabet
    message_encoded = ""
    for i in range(len(message)):
        if not message[i] in punctuation:
            index =  alphabet.find(message[i]) - alphabet.find(keyword_string[i])
            message_encoded += alphabet[index % len(alphabet)]
        else:
            message_encoded += message[i]
    
    return message_encoded

# function to decode message
def vigenere_decode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    punctuation = "()~@#$%^&*-_+=/\"\<>.,?!:' "
    index_keyword = 0
    keyword_string = ""
    for letter in message:
        if not letter in punctuation:
            keyword_string += keyword[index_keyword]
            index_keyword = (index_keyword + 1) % len(keyword)
        else:
            keyword_string += letter 
   
    message_decoded = ""
    for i in range(len(message)):
        if not message[i] in punctuation:
            index =  alphabet.find(message[i]) + alphabet.find(keyword_string[i])
            message_decoded += alphabet[index % len(alphabet)]
        else:
            message_decoded += message[i]
            
    return message_decoded


# message and keyword to encode
message1 = "Hello guys! My name is Liam. If you need me, call my phone number: 0755XXXXXXX"
keyword = "liam"
print("Encoded message\n" + vigenere_encode(message1, keyword))
# message to decode
message2 = vigenere_encode(message1, keyword)
print("Decoded message\n" + vigenere_decode(message2, keyword))

# principle:
# if you want to decode, shift forwards
# if you want to encode, shift backwards

