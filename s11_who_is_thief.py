"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.
Among them, three were telling the truth while one was lying.
Could you find out who is the thief?
"""

for thief in ['John','Paul','George','Ringo']:          # assume theif is John (or the lement in the list)
  sum = (thief != 'John') + (thief == 'George') + (thief == 'Ringo') + (thief != 'Ringo')   # test each statement and add the sum of truths (truth = 1, False = 0)
  if sum == 3:
    print("The thief is {}." .format(thief))