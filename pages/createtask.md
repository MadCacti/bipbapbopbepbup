{% include base.html %}

  
# Create Task
##  Ideation
- A really dumb game

# Answers to Written Response

## Part A:

### I. Describe the overall purpose of the program 
- The purpose of the program is essentially a game to kill time with, though it also shows the real randomness of events,  
 
### II. Describe what part of the program is being shown in the video 
- In the video, the game itself is being played live.

### III. Describes the input and output of the program demonstrated in the video 
- The inputs would be the first number guessed and which math function to use, while the outputs are showing the end result of each math function or if they got it correct. 

## Part B:

### I. The first program code segment must show how data have been stored in the list. 
- We have an empty list of ```self.numList = []``` which will have values stored in it with ```self.numList.append(self.num)```
  
### II. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 
- Here we have a code snippet. It accesses the length of it to show score, as well as display the previous values to see how the number was manipulated. ![image](https://user-images.githubusercontent.com/45216311/163830841-8d9ab251-537d-4101-ae88-20f9eb8090d3.png)
and ![image](https://user-images.githubusercontent.com/45216311/165634528-0d7a5963-d58f-4879-b301-92d1ac35664c.png)

### III. Identifies the name of the list being used in this response 
- The list is named ```numList```, but because we put it in a class, it is ```self.numList```
  
### IV. Describes what the data contained in the list represent in your program 
- The data in our list is all about the numbers that have been guessed or manipulated
  
### V. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list 
- Although the usage is simply for outputting the list for callback and to use the length of the list, we could have potentially had reversible functions that are specific for turning it back to a previous number, like an undo/redo option but would be limited to one number undos by storing the value into a different variable each time.

## Part C:

### I. The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration 
![image](https://user-images.githubusercontent.com/45216311/165636746-8464f73a-6ebe-4523-9168-617c76101894.png)

### II. The second program code segment must show where your student-developed procedure is being called in your program
- ![image](https://user-images.githubusercontent.com/45216311/163846638-98190c20-f5f5-4a5c-9dbd-477c700bd210.png) 

### III. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
- The procedure `function` sets up a random number(based on difficulty) and provides the math functions still with full anonymity.

### IV. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
- The algorithm displays the 4 basic math functions: addition, subtraction, multiplication, and division as well as an option to go back to a previous number in the list. Due to the sake of guessing whole numbers, division is rounded to the nearest whole number. Based on the user input for whichever math function, a predecided random number based on a range of 1-9 or 1-20 depending on the difficulty is used alongside the original value, which becomes the new value. 

## Part D:

### I. Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
- Each call is similar, but provides a different argument value to change alongisde the difficulty. The variable `option` represents this, either being set a value of `1` or `2` to represent the two difficulties. This causes a different `if` statement to run in the `functions()` to ensure the right range of values is used for each respective difficulty.
  
### II. Describes what condition(s) is being tested by each call to the procedure 
- For each the call to the procedure, the condition is whether or not the difficulty had been set to easy or hard.
  
### III. Identifies the result of each call.
- The result is the range in which a random integer can be chosen from to make the game potentially easier or harder based on random chance. 