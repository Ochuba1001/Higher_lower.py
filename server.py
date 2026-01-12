from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route("/")
def home():
    return ("<h1> GUESS THE NUMBER BETWEEN 0 AND 9 </h1>"
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width = 250/>'
            )


@app.route("/<int:number>")
def guess(number):
    if number < random_number:
        return (
            "<h1 style='color:red'>YOUR GUESS IS TOO LOW, WHY NOT GO HIGHER!</h1>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExamVlY2RvbGV1eG84bmV0OGNleWlzMzN4eXZ3ejVkM3F0dHUwbXh6aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WXtccLGTLB1NS/giphy.gif' width='250'/>"
        )
    elif number > random_number:
        return (
            "<h1 style='color:blue'>YOUR GUESS IS TOO HIGH, TRY GOING LOWER!</h1>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGxheTNoaGdlcjFwNzZqamFpNjdqM2NiMmRmYmU5dW0yaW40NmhyNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GCO5WNzFmlc0vjK8cA/giphy.gif' width='250'/>"
        )
    else:
        return (
            "<h1 style='color:green'>YOU GUESSED CORRECT!!!!</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGowNnlud2o0Y3c5cWJtMjFqdGN4azI1Zzd6bDc5dWVrc2ZpYWVneSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTOQHQ9lim011gF80j/giphy.gif' width='250'/>"
        )



if __name__ == "__main__":
    app.run(debug=True)

