from flask import Flask, render_template
from flask_ask import Ask, statement, question

APP = Flask(__name__)
ASK = Ask(APP, '/')


@ASK.launch
def launch():
    return question(render_template('greeting'))


@ASK.intent('AMAZON.YesIntent')
def choose_product():
    return statement(render_template('choose_product'))


@ASK.intent('overviewIntent')
def overview():
    return statement(render_template('overview'))


@ASK.intent('smallCoffIntent')
def small_coffee():
    return statement(render_template('explanation_one_cup'))


@ASK.intent('coffeeIntent')
def normal_coffee():
    return statement(render_template('explanation_two_cups', product='kaffee'))


@ASK.intent('productionIntent', convert={'product' : str}, default={'product': None})
def explain_product(product):
    print(product)
    if product == None:
        return statement(render_template('no_such_product'))
    elif product == 'kaffee':
        return question(render_template('size_does_matter'))

    return statement(render_template('explanation_two_cups', product=product))


@ASK.intent('decalcifyIntent')
def decalcify():
    return statement(render_template('decalcify'))


# main function
if __name__ == '__main__':
    APP.run(debug=True)
