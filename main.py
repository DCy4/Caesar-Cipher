alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(t, s):
  cipher_text = ""
  for letter in t:
    #variable to store index of letter
    position = alphabet.index(letter)
    #add shift to the index of the letter
    new_position = position + s   
    #similar to position, this finds the new index of letter 
    new_letter = alphabet[new_position]
    #append this new letter to string variable outside of loop
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(t = text,s = shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
encrypt(plain_text=text, shift_amount=shift)