age = 30
name = "Stephen"

def hello(name="STEPHEN", age=30):
    return "Hello {} you are {} years old!".format(name, age)

sentence = hello()

print(sentence)