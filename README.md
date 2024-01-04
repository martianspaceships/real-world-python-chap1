### Date Created

12/29/2023

### Project Title

Interactive Search and Rescue Game

### Description

This project is an interactive game to find a lost sailor. A map of Cape Python is used along with three search areas for the user to use in trying to locate the sailor. 

### Objective

Use Bayes' Rule as a guide to choosing search locations for the missing sailor.

### Files Used

bayes.py

cape_python.png

### Code Organization and Functionality

Begin with the **game objective**: Create a search and rescue game that uses Bayes' rule to inform player choices on how to conduct a search.

**Code strategy**: the program begins with initial target probabilities for the sailor's location and updates them based on the search results until the sailor is found or the user has used three unsuccessful attempts to find the sailor. (Code in book doesn't limit the user to three attempts)

- Import modules, python first and then 3rd party modules

- Define the 'Search' class

- Draw the search areas and legend on a 'map' which is a pulled in .png image

- Choose the sailor's final location using a random number method for the x and y coordinates within a search area

- Calculate search effectiveness of actually finding the sailor in a given search area

- Conduct the search in the chosen search areas (to be defined in two steps when getting user input)

- Revise target probabilities based on the results of a search

- Get input selection from user to determine which search area to search

- Create the main function to begin/continue the search and rescue game

### Credits

Book: Real World Python by Lee Vaughan

[Real World Python Book GitHub Repo](https://github.com/rlvaugh/Real_World_Python)
