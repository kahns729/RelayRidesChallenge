# RelayRidesChallenge

## Overview
-----------------

Python implementation of a simple database, according to the [Thumbtack coding challenge specifications](https://www.thumbtack.com/challenges/simple-database)


## Usage
-----------------

To run the database in interactive mode:
	`python db.py`

To run with an input file containing database commands:
	`python db.py < [myFile.txt]`


## Testing
-----------------

A simple testing framework has been set up for the simple database. To run it, use
	`python test.py [tests_directory]`,
where *tests_directory* is a folder containing an **inputs** folder and an **outputs** folder. The result of running *db.py* with each file in **inputs** is compared with a file of the same name in **outputs** to determine if the test was successful. Output test files should end with a newline in order for tests to pass. A test directory is already included.