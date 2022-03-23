phrase = input("Enter a phrase(can include special characters)")
specialchars = "!@#$%^&*()`~-_+=[{]}\|;:"',<.>/?'"] "
# all the special chars: need to filter them out + filter out spaces- !@#$%^&*()`~-_+=[{]}\|;:"',<.>/?'"]
for chars in specialchars:
  phrase = phrase.replace(chars, "")

print(phrase)
