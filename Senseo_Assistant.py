from flask import Flask, render_template
from flask_ask import Ask, statement, question

# ====================================== FLASK DECLARATION AND INITIALIZATION ======================================== #

APP = Flask(__name__)
ASK = Ask(APP, '/')


# ===================================== IMPLEMENTATION FOR PREDEFINED INTENTS ======================================== #

@ASK.intent('AMAZON.CancelIntent')
def cancel():
    return statement(render_template('cancel'))


@ASK.intent('AMAZON.StopIntent')
def stop():
    return cancel()


@ASK.intent('AMAZON.HelpIntent')
def help():
    return overview()


@ASK.intent('AMAZON.YesIntent')
def choose_product():
    """
    user is asked which product he wants
    :return:
    """
    return statement(render_template('choose_product'))


# ==================================================================================================================== #
# ======================================== MAIN AREA WITH OWN IMPLEMENTATION ========================================= #


@ASK.launch
def launch():
    """
    the function that is triggered when skill is started
    :return: a greeting template
    """
    return question(render_template('greeting'))


@ASK.intent('overviewIntent')
def overview():
    """
    user is presented a broad overview over the skills functionality
    :return: template with overview content
    """
    return statement(render_template('overview'))


@ASK.intent('smallCoffIntent')
def small_coffee():
    """
    when the user decides to choose a small coffee
    :return: template that explains how to make small coffee
    """
    return statement(render_template('explanation_small_cup'))


@ASK.intent('coffeeIntent')
def normal_coffee():
    """
    when the user decides to pick a normal or large cup of coffee
    :return: template that explains how to make normal coffee
    """
    return statement(render_template('explanation_large_cup', product='kaffee'))


@ASK.intent('twoCupsIntent')
def two_cups_of_coffee():
    """
    in case the user wants to have two cups of coffee
    :return: template that explains how to make two single cups of coffee parallel.
    """
    return statement(render_template('explanation_two_cups', product='kaffee'))


@ASK.intent('productionIntent', convert={'product': str}, default={'product': None})
def explain_product(product):
    """
    the user wants to have an explanation on how he/she manages to make a hot drink using the senseo coffeepad machine
    :param product: the product the user says he/she wants
    :return: respective template for each situation depending on the implementation
    """
    if product == None:
        return statement(render_template('no_such_product'))
    elif product == 'kaffee':
        return question(render_template('size_does_matter'))

    return statement(render_template('explanation_two_cups', product=product))


@ASK.intent('decalcifyIntent')
def decalcify():
    """
    short explanation on how one could decalcify the machine.
    :return: the template that explains how to decalcify
    """
    return statement(render_template('decalcify'))


# main function
if __name__ == '__main__':
    APP.run(debug=True)
