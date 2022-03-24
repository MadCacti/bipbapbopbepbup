phrase = ["racecar", "raCe caR!>#", "wrong"] # tests all different types: normal, abnormal, and example of incorrect
specialchars = "!@#$%^&*()~`<>,./?':;}{][\| "
inverse = ""
# all the special chars: need to filter them out + filter out spaces- !@#$%^&*()`~-_+=[{]}\|;:"',<.>/?'"]
for phrases in phrase:
  print("original phrase:", phrases)
  for chars in specialchars:
    phrases = phrases.replace(chars, "")
    inverse = phrases[::-1] # this reverses string
    phrases.lower()
  print("new phrase:", phrases)  
  if (phrases == inverse):
    print(phrases, "is a palindrome")
  else:
    print(phrases, "is not a palindrome")