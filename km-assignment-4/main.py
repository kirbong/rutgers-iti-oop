## Test Code
from person import Person

people_list =  [Person('Robert', 'Johnson', 15), 
                Person('Bob', 'Robby', 18),
                Person('John', 'Smith', 25)]

for x in people_list:
    age_desc = 'Adult'
    if x.isMinor(): age_desc = 'Minor'
    print(f"{x.first_name} {x.last_name} is a(n) {age_desc}")
