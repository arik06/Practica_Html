people = [
    {
        "name": "John",
        "age": 30
    },
    {
        "name": "Jane",
        "age": 20
    },
    {
        "name": "Mary",
        "age": 10
    }
]

def f (person):
    return person["age"]
people.sort(key=f)

print(people)