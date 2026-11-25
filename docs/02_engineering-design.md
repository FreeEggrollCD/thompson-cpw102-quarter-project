# Engineering Design Document


## Overview

The application will be called from the command line.
If the required packages are not found, the user will be prompted to install them.
Once the program is running, the user will be prompted for which part(s) they would like to benchmark.
The user will then be prompted for how verbose the results should be and if they would like to save them to a file.
A series of flags can be called upon running the program to skip being prompted and go straight to the benchmarking.

## System Diagrams

If the program is ran without arguments then the options menu will look something like this:
```
Select the parts you wish to benchmark
GPU [ ]
CPU [ ]
Drive [ ]

Begin Benchmark
```
With the bracketed spaces being selectable check boxes and begin benchmark being a selectable option

That can be skipped by running the program with arguments like this:
`python benchmark.py -c -g -d "Drive Name/Letter" -vv`

## Technical Details


### Inputs

The user will be greeted with a set of options for how and what they would like to benchmark if the program is run without any arguments.
If arguments are passed when the program gets run then it will automatically execute the program functions associated with those arguments.

#### Handling bad inputs

Bad inputs will be handled by replying to the user that the previous input was invalid. The program will only continue its execution
if a valid input is given.

### Logic

Loops will be used for input validation and during the process of benchmarking. Multiple `if` statements will be used for checking passed arguments and running their associated functionality. Before running the main program a check will be ran to make sure dependancies are installed, if they are not the user will be prompted to install them. If the user chooses no, they can install the requirements by running the program with the `-irq` or `--install-requirements` argument

### Functions

Functions will be broken up into the respective parts to be benchmarked.

### Libraries

Most Libraries being used are in the Python Standard Library, such as `multiprocessing` and `sys`. I will be using `rich` and `tqdm` for more elegant looking outputs and progress bars. It will also use `wgpu` for GPU benchmarking.

### Output

A summary of the benchmark will be printed to the screen and the user will be prompted if they want it saved to a file
In the event the user ran the program with arguments to determine benchmarking options the same thing will occur.
The output will be formatted something like the following:
```
CPU:
Clock Speed: 8.4Ghz
Minimum Temp: 40*C
Max Temp: 88*C

GPU:
Clock Speed: 10.2Ghz
Minimum Temp: 60*C
Max Temp: 97*C

Drive 1:
Read Speed: 1.8 Gbps
Write Speed: 4.2 Gbps