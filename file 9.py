people = [
   {"name": "Tom", "age" : 39, "company": "SuperCorp", "languages": ["Python","JavaScript"]},
   {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
   {"name": "Sam", "age" : 28, "company": "LittleCorp", "languages": ["Python", "Java"] }
]
a = 0
while a != len(people):
   for key,values in people[a].items():
      bing = people[a].get('name')
      ghoul = people[a].get('languages')
      re = people[a].get('age')
   a += 1
   print( f'NAME: {bing} \nAGE: {re}  \nLAST LANGUAGE: {ghoul[-1]} \n')