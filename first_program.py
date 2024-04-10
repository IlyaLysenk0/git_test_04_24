from flask import send_file, request, Flask

from flask import url_for, redirect, abort

from flask import  render_template  , session



app = Flask(__name__)


@app.route('/')
def f_1():
    return render_template('first_program_pg1.html')


@app.route('/pg1')
def f_2():
    return render_template('first_program_pg2.html')

@app.route('/pg2')
def f_3():
    return render_template('first_program_pg3.html')

@app.route('/pg3', methods = ['GET'])
def f_4():
    us_name = request.args.get('us_name')
    us_age = request.args.get('us_age')
    return f'Вітаю, вас звати {us_name}, і вам {us_age} років'





if __name__ == '__main__':
    app.run(debug=True, port=8000)



