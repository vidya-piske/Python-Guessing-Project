from flask import Flask
from number_guessing_game.py import shuffle_list,get_user_guess,check_guess 

app = Flask(__name__)

@app.route('/')

def index():
    # Shuffled List
    shuffle_output = shuffle_list(mylist)

    # User Input
    user_guess_value = get_user_guess()

    # Guessing
    result = check_guess(shuffle_output, user_guess_value)
   
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()