# [Project name]

## Project description

This project is an AIO computer hardware benchmarking CLI software written in python.

## Author

Jonathon Thompson

## Environment setup

Python >= 3.14
Doowload libraries in `dependencies.txt` or optionally run the program with the `-d` flag

## Dependencies
TP = Third party
PS = Python standard

The main project will use these libraries:
(TP)rich - for displaying information in a more "aesthetically pleasing" way
(PS)threading - for use in bencharking the cpu

## Running the project

The program can be run using this command: `python3 main.py`.
If dependency errors are present run with the `-d` flag: `python3 main.py -d`.

## Running the tests

The command for testing is : `python3 main.py -T`