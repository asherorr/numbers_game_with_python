Hello, world!

This is my first project in the Python techdegree at Treehouse. I'm so excited to share it with you!

guessing_game.py runs a fun game you can play.

First, a welcome message is displayed.

Then, the start_game() function begins.

A random integer >= 1 or <=10 is generated. Then the user is asked to enter any number from 1-10.

A try block then handles 2 errors:

Error 1: The user inputs a number outside the range 1-10.
Error 2: The user inputs a non-integer.

If no exceptions are raised, the program informs the user whether they entered the right number or not. If they guess the wrong number, the program informs the user whether the correct number is higher or lower, then to try again.

When they guess the right number, the length of the list "guesses" - which is, the number of guesses they made to get the right number - is added to the list "num_guesses_to_get_right."

If they guess the right number, the user is congratulated and told how many guesses it took within that session of the game. The list "guesses" is then cleared, so the user can get an updated number if they choose to play the game again.

The user is then asked if they'd like to play again. If yes, they are shown their high score - that is, the least amount of guesses they've made to get the right answer.

If the user chooses to plau again, the program prevents the same random number from generating upon starting a new game.

The random number generated at the start of the game is added to a list called "random_numbers_generated."

A while block creates a variable called new_random_num, which generates a random integer from 1 - 10. If the new_random_number is NOT in the list "random_numbers_generated," the while loop will break. Otherwise, it will continue to run.

After the loop breaks, the variable random_num is coerced to new_random_num. Then the list random_numbers_generated is cleared. This is because the entire function start_game is nested within a while loop. Upon playing the game again, the random number to guess will always be:

- A new random integer between 1-10
and:
- NOT the integer users had to guess in the previous game.

If the player chooses not to play again, the ending_message() function runs. It prints a thank-you message and closes the program.

Thank you for reading!

Copyright (c) [2022] [Stephen Asher Orr]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
