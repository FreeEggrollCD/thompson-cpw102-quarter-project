# Engineering Design Document


## Overview

The application will be called from the command line.
If the required packages are not found, the user will be prompted to install them.
Once the program is running, the user will be prompted for which part(s) they would like to benchmark.
The user will then be prompted for how verbose the results should be and if they would like to save them to a file.
A series of flags can be called upon running the program to skip being prompted and go straight to the benchmarking.

## System Diagrams

[This document must include one or more of the following:

- block diagram of your proposed functions and modules, including external libraries
- flowchart of logic for critical flows
- mockups of any program-driven user interfaces, if applicable]

## Technical Details


### Inputs

The user will be greeted with a series of options for what they would like to benchmark.

#### Handling bad inputs

[How will your app handle bad user inputs?] 

### Logic

[At a high level, describe the logic you will need to apply. What Python tools will you use to capture that logic? For loops, while loops, exceptions?] 

### Functions

[How will you break your flow of logic up into functions? Write some psuedo code for your `main()` function to show how your app will coordinate its duties.]

``` python
def main():
    """
    function calls go below here
    """
    pass

main()
```

### Libraries

[How can you leverage external libraries to:

- take advantage of functionality already written and tested by others?
- improve the performance, user experience, or features in your application?

All apps should leverage libraries. ]

### Output

[What exactly will you output to the user? Options could be:

- printing a report to the terminal at the end of a program
- repeatedly giving users updates on an iterative process
- creating a file based on user-entered data

If applicable, show an example output below:]

```

```