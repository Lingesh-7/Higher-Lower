from flask import Flask
from random import randint
app=Flask(__name__)
ran_num=randint(0,9)
print(f"Roandom:  {ran_num}")
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1><br><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzMzbWV1cTlxdTFsdTl1MG9iYzdwanJmZGQwNW9wczF3aGFod2VzNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QmJ3e9So5M9NdNkOGo/giphy.gif' width=600>"
# @app.route(f'/{str(ran_num)}')
# def won():
#     return "<h1 style='color: green'>YOU FOUND ME!!!</h1><br><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmNjMTU5cGZoMjJzNnh5ZGw0YnB5bXk5dW9xczFwMGt5OXNjZ2oxdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT1R9GYCO1eRlwxW24/giphy.gif' width=900>"

@app.route('/<int:num>')
def high(num):
    if num>ran_num:
        return "<h1 style='color: red'>TOO HIGH,try again!!!</h1><br><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGwwZG13NWNxbHJ6YjkwMHVrOWljZ2h1Mmw2aWo2aHh5M2E1dnU4MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YKroe55zFMIwpmBCu6/giphy.gif' width=600>"
    elif num<ran_num:
        return "<h1 style='color: purple'>TOO LOW,try again!!!</h1><br><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYThhbmVhOWM0Zm0ybGFqbHg4ZDd0aXlzbnp6NmppMnc0OGU4a3BqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif' width=900>"
    else: 
        return "<h1 style='color: green'>YOU FOUND ME!!!</h1><br><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmNjMTU5cGZoMjJzNnh5ZGw0YnB5bXk5dW9xczFwMGt5OXNjZ2oxdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT1R9GYCO1eRlwxW24/giphy.gif' width=900>"

if __name__=='__main__':
    app.run(debug=True)