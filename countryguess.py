import time, random, sys
from colorama import Fore, Back
from art import *

#* declares country lists *#

# african countries
AFRICA = [
    'algeria',
    'angola',
    'benin',
    'botswana',
    'burkina faso',
    'burundi',
    'cape verde',
    'cameroon',
    'central african republic',
    'chad',
    'comoros',
    'congo',
    'cote divoire',
    'djibouti',
    'democratic republic of congo',
    'egypt',
    'equatorial guinea',
    'eritrea',
    'eswatini',
    'ethiopia',
    'gabon',
    'gambia',
    'ghana',
    'guinea',
    'guinea-bissau',
    'kenya',
    'lesotho',
    'liberia',
    'libya',
    'madagascar',
    'malawi',
    'mali',
    'marutitania',
    'mauritius',
    'morocco',
    'mozambique',
    'namibia',
    'niger',
    'nigeria',
    'rwanda',
    'sao tome and principe',
    'senegal',
    'seychelles',
    'sierra leone',
    'somalia',
    'south africa',
    'south sudan',
    'sudan',
    'tanzania',
    'togo',
    'tunisia',
    'uganda',
    'zambia',
    'zimbabwe',
]
AFRICA_ALT = {
    'ivory coast': 'cote divoire',
    'cabo verde': 'cape verde',
    'coted ivoire': 'cote divoire',
    'cote d ivoire': 'cote divoire',
    'cotedivoire': 'cote divoire',
    'zaire': 'democratic republic of congo',
    'drc': 'democratic republic of congo',
    'democratic rep of congo': 'democratic republic of congo',
    'dem republic of congo': 'democratic republic of congo',
    'dem rep of congo': 'democratic republic of congo',
    'swaziland': 'eswatini',
}

# asian countries
ASIA = [
    'afghanistan',
    'armenia',
    'azerbaijan',
    'bahrain',
    'bangladesh',
    'bhutan',
    'brunei',
    'cambodia',
    'china',
    'cyprus',
    'georgia',
    'india',
    'indonesia',
    'iran',
    'iraq',
    'israel',
    'japan',
    'jordan',
    'kazakhstan',
    'kuwait',
    'kyrgyzstan',
    'laos',
    'lebanon',
    'malaysia',
    'maldives',
    'mongolia',
    'myanmar',
    'nepal',
    'north korea',
    'oman',
    'pakistan',
    'phillippines',
    'qatar',
    'saudi arabia',
    'singapore',
    'south korea',
    'sri lanka',
    'syria',
    'tajikistan',
    'thailand',
    'timor-leste',
    'turkey',
    'turkmenistan',
    'united arab emirates',
    'uzbekistan',
    'vietnam',
    'yemen',
]
ASIA_ALT = {
    'peoples republic of china': 'china',
    'democratic peoples republic of korea': 'north korea',
    'republic of korea': 'south korea',
    'east timor': 'timor-leste',
    'timor leste': 'timor-leste',
    'uae': 'united arab emirates',
}

# european countries
EUROPE = [
    'albania',
    'andorra',
    'austria',
    'belarus',
    'belgium',
    'bosnia and herzegovina',
    'bulgaria',
    'croatia',
    'czechia',
    'denmark',
    'estonia',
    'finland',
    'france',
    'germany',
    'greece',
    'hungary',
    'iceland',
    'ireland',
    'italy',
    'latvia',
    'liechtenstein',
    'lithuania',
    'luxeumbourg',
    'malta',
    'moldova',
    'monaco',
    'montenegro',
    'netherlands',
    'north macedonia',
    'norway',
    'poland',
    'portugal',
    'romania',
    'russia',
    'san marino',
    'serbia',
    'slovakia',
    'slovenia',
    'spain',
    'switzerland',
    'ukraine',
    'united kingdom',
]
EUROPE_ALT = {
    'czech republic': 'czechia',
    'macedonia': 'north macedonia',
    'uk': 'united kingdom',
}

# north american countries
NORTH_AMERICA = [
    'antigua and barbuda',
    'bahamas',
    'barbados',
    'belize',
    'canada',
    'costa rica',
    'cuba',
    'dominica',
    'dominican republic',
    'el salvador',
    'grenada',
    'guatemala',
    'haiti',
    'honduras',
    'jamaica',
    'mexico',
    'nicaragua',
    'panama',
    'saint kitts and nevis',
    'saint lucia',
    'saint vincent and the grenadines',
    'trinidad and tobago',
    'united states of america',
]
NORTH_AMERICA_ALT = {
    'saint vincent': 'saint vincent and the grenadines',
    'usa': 'united states of america',
}

# south american countries
SOUTH_AMERICA = [
    'Argentina',
    'Bolivia',
    'Brazil',
    'Chile',
    'Colombia',
    'Ecuador',
    'Guyana',
    'Paraguay',
    'Peru',
    'Suriname',
    'Uruguay',
    'Venezuela',
]

# oceania
OCEANIA = [
    'australia',
    'fiji',
    'kiribati',
    'marshall islands',
    'micronesia',
    'nauru',
    'new zealand',
    'palau',
    'papua new guinea',
    'samoa',
    'solomon islands',
    'tonga',
    'tuvalu',
    'vanuatu',
]

# list of all the (U.N. recognised) countries in the world
WORLD = AFRICA + ASIA + EUROPE + NORTH_AMERICA + SOUTH_AMERICA + OCEANIA
WORLD_ALT = AFRICA_ALT | ASIA_ALT | EUROPE_ALT | NORTH_AMERICA_ALT

# U.N. observer states
OBSERVER_STATES = [
    'palestine',
    'vatican city',
]
OBSERVER_STATES_ALT = {
    'holy see': 'vatican city',
    'vatican': 'vatican city',
}

# disputed territories
OTHER_DISPUTED_TERRITORIES = [
    'kosovo',
    'western sahara'
]

# unrecognised territories
UNRECOGNISED_TERRITORIES = [
    'somaliland',
    'northern cyprus',
    'abkhazia',
    'south ossetia',
    'nagorno-karabakh',
    'transnistria',
]
UNRECOGNISED_TERRITORIES_ALT = {
    'republic of artsakh': 'nagorno-karabakh',
}

#* declares functions *#

def warning_tag(param): return Back.RED + param + Back.RESET

def call_error(param, errorType='none', minR=0, maxR=0):
    """error message"""

    # something went wrong (Fire Font-k)
    print(Fore.RED)     
    tprint('something went wrong', 'fire-font-s')                                                                                                        
    # print('                           )    )                                           )                                   ')
    # print('             )      (   ( /( ( /( (          (  (    (  (      (         ( /(   (  (    (                (  (   ')
    # print(' (    (     (      ))\\  )\\()))\\()))\\   (     )\\))(   )\\))(    ))\\  (     )\\())  )\\))(   )(    (    (     )\\))(  ')
    # print(' )\\   )\\    )\\  \' /((_)(_))/((_)\\((_)  )\\ ) ((_))\\  ((_)()\\  /((_) )\\ ) (_))/  ((_)()\\ (()\\   )\\   )\\ ) ((_))\\  ')
    # print('((_) ((_) _((_)) (_))  | |_ | |(_)(_) _(_/(  (()(_) _(()((_)(_))  _(_/( | |_   _(()((_) ((_) ((_) _(_/(  (()(_) ')
    # print('(_-</ _ \\| \'  \\()/ -_) |  _|| \' \\ | || \' \\))/ _` |  \\ V  V // -_)| \' \\))|  _|  \\ V  V /| \'_|/ _ \\| \' \\))/ _` |  ')
    # print('/__/\\___/|_|_|_| \\___|  \\__||_||_||_||_||_| \\__, |   \\_/\\_/ \\___||_||_|  \\__|   \\_/\\_/ |_|  \\___/|_||_| \\__, |  ')
    # print('                                            |___/                                                       |___/   ')
    # print('')

    err = warning_tag(param)

    match errorType:
        case 'subject':
            print(f'{err} is not a valid subject. Please try again.')
        case 'topic':
            print(f'{err} is not a valid topic. Please try again.')
        case 'does_not_exist':
            print(f'{err} does not exist yet. Please try again later.')
        case 'range':
            print(f'{err} is not a valid input. You must input a number between {minR} and {maxR}. Please try again')
        case _:
            print(f'{err} is not a valid input. Please try again.')
    print('')
    input('~~> ')

    print('\033c', end='') # clear terminal

#* program *#

while True:
    print(Fore.GREEN, end='')
    tprint('countryguess', 'soft')

    print(Fore.BLUE)
    print('Choose an option:')

    print(Fore.GREEN)
    print('~ countries of the world')
    print('~ continents')
    print(Fore.RED +    '   ~ africa')
    print(Fore.CYAN +   '   ~ asia')
    print(Fore.MAGENTA +   '   ~ europe')
    print(Fore.YELLOW + '   ~ north america')
    print(Fore.GREEN +   '   ~ south america')
    print(Fore.BLUE +   '   ~ oceania')

    print(Fore.MAGENTA)
    print('~ options')

    print(Fore.RED)
    print('~ quit')

    userInput = input('~~> ').lower()

    match userInput:
        case 'countries of the world' | 'countries' | 'world':

            print('\033c', end='') # clear terminal
        case 'africa':

            print('\033c', end='') # clear terminal
        case 'asia':

            print('\033c', end='') # clear terminal
        case 'europe':

            print('\033c', end='') # clear terminal
        case 'north america':

            print('\033c', end='') # clear terminal
        case 'south america':

            print('\033c', end='') # clear terminal
        case 'oceania':

            print('\033c', end='') # clear terminal
        case 'options' | 'settings':

            print('\033c', end='') # clear terminal
        case 'quit':
            sys.exit(0)
        case _: # invalid input
            call_error(userInput)

# userInput = input('type a country: ')
# if userInput in AFRICA or userInput in AFRICA_ALT:
#     print('this country is in AFRICA')
# if userInput in ASIA or userInput in ASIA_ALT:
#     print('this country is in ASIA')
# if userInput in EUROPE or userInput in EUROPE_ALT:
#     print('this country is in EUROPE')
# if userInput in NORTH_AMERICA or userInput in NORTH_AMERICA_ALT:
#     print('this country is in NORTH AMERICA')
# if userInput in SOUTH_AMERICA:
#     print('this country is in SOUTH AMERICA')
# if userInput in OCEANIA:
#     print('this country is in OCEANIA')
# if userInput in OBSERVER_STATES or userInput in OBSERVER_STATES_ALT:
#     print('this is a U.N. observer state')
# if userInput in OTHER_DISPUTED_TERRITORIES:
#     print('this is a disputed territory')
# if userInput in UNRECOGNISED_TERRITORIES or userInput in UNRECOGNISED_TERRITORIES_ALT:
#     print('this is an unrecognised territory')
# if userInput in WORLD or userInput in WORLD_ALT:
#     print('this is a U.N. recognised country')
# else:
#     print('it is not a U.N. recognised country')
