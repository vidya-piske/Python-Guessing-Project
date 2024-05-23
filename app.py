from flask import Flask, render_template, request
from number_guessing_game import shuffle_list, check_guess, mylist

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    shuffle_output = shuffle_list(mylist)  
    result = ""
    user_guess_value = ""

    if request.method == 'POST':
        user_guess_value = int(request.form['guess'])
        result = check_guess(shuffle_output, user_guess_value)
    
    return render_template('index.html', result=result, shuffled_list=shuffle_output)

if __name__ == "__main__":
    app.run(debug=True)
