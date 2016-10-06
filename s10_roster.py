roster = ["Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf"]


import random

def call_three(roster):
    """
    print three names randomly
    roster: a list of strings
    """

# number_list = []
# for i in range(3):                      # run the loop three times
#   x = random.randint(len(roster)-1)     # include "-1"

number_list = random.sample(range(1, len(roster)),3)
for number in number_list:
  print(roster[number])

call_three(roster)