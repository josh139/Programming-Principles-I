# Programming-Principles-I
This was my first project at university. Below is the task I was given:

## Part 1 - Student Version
- The program should allow students to predict their progression outcome at the end of each academic year.
- The program should prompt for the number of credits at pass, defer and fail and then display the appropriate progression outcome for an individual student.
- The program should let the user know if a credit input is the wrong data type. I.e., ‘Integers required’ is displayed.
- The program should let the user know if credits are not in the range 0, 20, 40, 60, 80, 100 and 120. I.e., ‘Range error’ is displayed.
- The program should let the user know if the total of the pass, defer and fail credits is not 120. I.e., ‘Total incorrect’ is displayed.

### Table 1: Progression outcomes as defined by the University regulations.
| Pass (including condoned pass) | Defer | Fail | Progression Outcome |
| :---: | :---: | :---: | :---: |
| 120 | 0 | 0 | Progress |
| 100 | 20 | 0 | Progress – module trailer |
| 100 | 0 | 20 | Progress – module trailer |
| 80 | 40 | 0 | Do not Progress – module retriever |
| 80 | 20 | 20 | Do not Progress – module retriever |
| 80 | 0 |40 | Do not Progress – module retriever |
| 60 | 60 | 0 | Do not progress – module retriever |
| 60 | 40 | 20 | Do not progress – module retriever |
| 60 | 20 | 40 | Do not progress – module retriever |
| 60 | 0 | 60 | Do not progress – module retriever |
| 40 | 80 | 0 | Do not progress – module retriever |
| 40 | 60 | 20 | Do not progress – module retriever |
| 40 | 40 | 40 | Do not progress – module retriever |
| 40 | 20 | 60 | Do not progress – module retriever |
| 40 | 0 | 80 | Exclude |
| 20 |100 | 0 | Do not progress – module retriever |
| 20 | 80 | 20 | Do not progress – module retriever |
| 20 | 60 | 40 | Do not progress – module retriever |
| 20 | 40 | 60 | Do not progress – module retriever |
| 20 | 20 | 80 | Exclude |
| 20 | 0 | 100 | Exclude |
| 0 | 120 | 0 | Do not progress – module retriever |
| 0 | 100 | 20 | Do not progress – module retriever |
| 0 | 80 | 40 | Do not progress – module retriever |
| 0 | 60 | 60 | Do not progress – module retriever |
| 0 | 40 | 80 | Exclude |
| 0 | 20 | 100 | Exclude |
| 0 | 0 | 120 | Exclude |

## Part 2 - Staff Version
- The program should prompt for credits at pass, defer and fail and display the appropriate progression for each individual student until the staff member user enters ‘q’ to quit.
- When ‘q’ is entered, the program should produce a ‘histogram’ where each star represents a student who achieved a progress outcome in the category range: progress, trailing, module retriever and exclude. See example below.
- The program should display the number of students for each progression category and the total number of outcomes processed.

This following horizontal histogram example shows the output distribution for 20 outcomes. However, your program should work with any number of outcomes generated.

Progress 10: ********** <br />
Trailing 5: ***** <br />
Retriever 3: *** <br />
Excluded 2: ** <br />
