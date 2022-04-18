{% include base.html %}

# Create Task
##  Ideation
- A really dumb game

## Answers to Written Response

Part A:
Part of Part | Question | Answer | 
--- | -------- | --------- |
I | Describe the overall purpose of the program | It's basically a fun game to kill time with for people that are incredibly bored. |
II | Describe what part of the program is being shown in the video | In the video, the game itself is being played live. |
III | Describes the input and output of the program demonstrated in the video | The inputs would be the first number guessed and which math function to use, while the outputs are showing the end result of each math function or if they got it correct. |

Part B:
Part of Part | Question | Answer | 
--- | -------- | --------- |
I | The first program code segment must show how data have been stored in the list. | We have an empty list of ```self.numList = []``` which will have values appended to it with ```self.numList.append(self.num)``` |
II | The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. |Here we have a code snippet. It accesses the length of it to show score, as well as display the previous values to see how the number was manipulated. ![image](https://user-images.githubusercontent.com/45216311/163830841-8d9ab251-537d-4101-ae88-20f9eb8090d3.png)
 |
III | Identifies the name of the list being used in this response | The list is named ```numList```, but because we put it in a class, it is ```self.numList``` |
IV | Describes what the data contained in the list represent in your program | The data in our list is all about the numbers that have been guessed or manipulated |
V | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list | Although the usage is simply for outputting the list for callback and to use the length of the list, we could have potentially had reversible functions that are specific for turning it back to a previous number, like an undo/redo option. |

Part C:
Part of Part | Question | Answer | 
--- | -------- | --------- |
I | The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration | ![image](https://user-images.githubusercontent.com/45216311/163832052-c1ddb790-1813-4f1e-975f-de74b14c6f80.png) |
II | The second program code segment must show where your student-developed procedure is being called in your program | ![image](https://user-images.githubusercontent.com/45216311/154349757-b2351e78-7305-4bf2-9e67-4a081eae81d0.png) |
III |  Describes in general what the identified procedure does and how it contributes to the overall functionality of the program| The procedure `handleguess` essentially makes sure that a guessed letter(by button) is correctly processed as either correct or incorrect, and updates the picture, # of wrong guesses or the blanks. Without it, the game wouldn't actually work. |
IV | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. | Essentially, the parameter 'choosenLetter' is required, and based on what button is pressed in the HTML part, the choosenLetter will be used respectively and updated so that it cannot be changed later. In another function, the guessed word is indexed and each letter in it is specifically set to >= 0 to identify it as a correct letter. All alphabet characters are initially set to -1, so that can be left alone while we update the correct letters to other values. This is done before the iteration to ensure that it is set up correctly, thus showing the requirement of sequencing this part of the code. The two options of iteration are evidently either a correct guess or incorrect one. The correct one runs two procedures that check if the game was won and update the word, while the incorrect one runs different procedures that update the drawing of the hangman as well as updating the amount of mistakes and checking if the game was lost on the mistake. The selection actually occurs at the very beginning with the user input of the buttons to select from, as that is the parameter of the function.  |

Part D:
Part of Part | Question | Answer | 
--- | -------- | --------- |
I | Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. | This is a bit hard with how we formatted this part. Unfortunately we set it so that the procedure is only set once, but gets repetitively recreated for all the letters in the alphabet and the space(-). However, if we were to break this up into parts, we can use the example of `stephen-king` as our guessed word, and have the `choosenLetter` options be `e` and `a`  |
II |  Describes what condition(s) is being tested by each call to the procedure | For each the call to the procedure, the condition is whether or not the letter is within the guessedword. For e, it would see that it is in the guessedword of `stephen-king`, but would not count it for `a` |
III | Identifies the result of each call | The result of `e` would be that it would update wherever `e` exists in the guessedWord and would check if the game was won, while `a` would increase the count of the mistakes as well as check if the amount of mistakes has reached the max, in which the game would end. |