import random


def rollem(options):

    options_dict = {'quantity': 1, 'maximum': 10, 'minimum': 1, 'modifier': 0}

    for option in options:
        try:
            value = int(option['value'])
        except:
            raise Exception('You must enter an Integer.')

        options_dict[option['name']] = value

    message = '```'

    for die in range(options_dict['quantity']):

        number = random.randint(
            options_dict['minimum'], options_dict['maximum'])

        if options_dict['modifier'] > 0:
            message += f'Roll: {number} + {options_dict["modifier"]} = {number + options_dict["modifier"]}\n'

        else:
            message += f'Roll: {number}\n'

    message += '```'

    return message
