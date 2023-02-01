#Python Program to add a record to nested dictionary
people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
          2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}

people[1]['team']='india'
people[2]['team']='india'
print(people)