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


#* quiz functions *#

def fill_list(param=[' '], fill='#'):
    filledList = []

    for i in param:
        filledList.append(len(i) * fill)
    
    return filledList

def africa_map():
    algeria_on = True
    disputed_territories = True

    morocco = [
        ' ',
        ' ',
        '__' if disputed_territories else '  ',
        '  _',
        '  ',
        '__'
    ]

    algeria = [
        '       ',
        '         ',
        '             ',
        '            ',
        '           ',
        '          ',
        '        ',
        ',,_',
    ]
    tunisia = [
        ' ',
        '/',
    ]
    libya = [
        '    ',
        '  ',
        '                ',
        '               ',
        '             ',
        '-_',
    ]
    egypt = [
        '   ',
        '    ',
        '     ',
        '______',
    ]
    chad = [
        '        ',
        '        ',
        '        _',
        '         ',
        '          ',
        '      ',
        '_ ',
    ]
    lesotho = ['[]']

    if algeria_on and not disputed_territories: # morocco w/ western sahara
        morocco = fill_list(morocco)
    elif algeria_on and disputed_territories: # morocco w/o western sahara
        morocco[:3] = fill_list(morocco[:3])
    if algeria_on and disputed_territories: # western sahara
        morocco[3:6] = fill_list(morocco[3:6])
    if algeria_on: # algeria
        algeria = fill_list(algeria)
    if algeria_on: # tunisia
        tunisia = fill_list(tunisia)
    if algeria_on: # libya
        libya = fill_list(libya)
    if algeria_on: # egypt
        egypt = fill_list(egypt)
    if algeria_on: # chad
        chad = fill_list(chad)
    if algeria_on: # lesotho
        lesotho = fill_list(lesotho)

    print('            ___________')
    print(f'           /{morocco[0]}|{algeria[0]}|{tunisia[0]}|')
    print(f'        ,\'{morocco[1]},\'{algeria[1]}\\{tunisia[1]}\',_    __')
    print(f'     ,\'{morocco[2]}/{algeria[2]}|{libya[0]}\',|{libya[1]}"\'-,,,,,,,')
    print(f'   ,/{morocco[3]}|\',{algeria[3]}|{libya[2]}|{egypt[0]} \\')
    print(f'   |{morocco[4]}|   |\'{algeria[4]},\\{libya[3]}|{egypt[1]}\\')
    print(f'   |{morocco[5]}|   |  \',{algeria[5]}\',{libya[4]}|{egypt[2]}\\')
    print(f'  /       |     \',{algeria[6]},_"""""---\'{libya[5]},\'{egypt[3]}\\')
    print(f' /        |        \'{algeria[7]}-\'"    |{chad[0]}|        \',')
    print(f'|_________|         |         /{chad[1]}|        / \',,\'""""|')
    print(f'|__  |        ,____/         |{chad[2]}|       /    |___  /')
    print(f'\'\\___|      ,\'_,\'|_,-,_______|{chad[3]}|_______/      , \'/')
    print(f'  \\,\' _\', _/  ,, ,\',|        |{chad[4]}\\       |   \'" ,\'')
    print(f'   \\ / |_ ,  |  \\||||       ,\' |{chad[5]},\'|    _""    |,\'')
    print(f'    \' ,\'  \', |  ||||| __ ,\'   _|{chad[6]},\'    |    |""---/')
    print(f'       \' ,"""\',\'"""""" |     /           \\"""|    /')
    print(f'                      |_____|_      __\'\'"    \\   |')
    print(f'                     |  |  /  """"""   |      \\ /')
    print(f'                      \\ / |            |       /')
    print(f'                       \\--\'            |      /')
    print(f'                       |   \\__        _|__    |')
    print(f'                       |      |__     |   \',,,|')
    print(f'                       |         |____|   /   |')
    print(f'                       /         _|    ,,\'_   |')
    print(f'                      |__________|___,\'  ,,\' /')
    print(f'                       \\      ---\'    \\,/  ,\'')
    print(f'                        \\     |    ,,,\' \\_/')
    print(f'                         |    |_,\'\'      |/')
    print(f'                         |    |       {lesotho[0]}_|')
    print(f'                          \\___\'        /')
    print(f'                           \\       __,\'')
    print(f'                            \\_____/        FoulWing')

def quiz(param):
    """country quiz"""
    pass


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

    print(Fore.YELLOW)
    print('~ find a country')

    print(Fore.MAGENTA)
    print('~ options')

    print(Fore.RED)
    print('~ quit')

    print(Fore.YELLOW)
    userInput = input('~~> ').lower()

    match userInput:
        case 'countries of the world' | 'countries' | 'world':
            quiz('world')

            print('\033c', end='') # clear terminal
        case 'africa' | 'asia' | 'europe' | 'north america' | 'south america' | 'oceania':
            quiz(userInput)

            if userInput == 'africa':
                africa_map()
            
            input('~~> ')

            print('\033c', end='') # clear terminal
        case 'find':
            print(Fore.CYAN)
            print('please enter a country')
            userInput = input('~~> ')

            print('')
            if userInput in AFRICA or userInput in AFRICA_ALT:
                print(Fore.RED + 'this country is in africa')
            if userInput in ASIA or userInput in ASIA_ALT:
                print(Fore.CYAN + 'this country is in asia')
            if userInput in EUROPE or userInput in EUROPE_ALT:
                print(Fore.MAGENTA + 'this country is in europe')
            if userInput in NORTH_AMERICA or userInput in NORTH_AMERICA_ALT:
                print(Fore.YELLOW + 'this country is in north america')
            if userInput in SOUTH_AMERICA:
                print(Fore.GREEN + 'this country is in south america')
            if userInput in OCEANIA:
                print(Fore.BLUE + 'this country is in oceania')
            if userInput in OBSERVER_STATES or userInput in OBSERVER_STATES_ALT:
                print(Fore.BLUE + 'this is a U.N. observer state')
            if userInput in OTHER_DISPUTED_TERRITORIES:
                print(Fore.YELLOW + 'this is a disputed territory')
            if userInput in UNRECOGNISED_TERRITORIES or userInput in UNRECOGNISED_TERRITORIES_ALT:
                print(Fore.RED + 'this is an unrecognised territory')

            if userInput in WORLD or userInput in WORLD_ALT:
                print(Fore.GREEN + 'this is a U.N. recognised country')
            elif not (userInput in OBSERVER_STATES or userInput in OBSERVER_STATES_ALT or userInput in OTHER_DISPUTED_TERRITORIES or userInput in UNRECOGNISED_TERRITORIES or userInput in UNRECOGNISED_TERRITORIES_ALT):
                print(Fore.RED + 'this is not a country!')
            
            print(Fore.YELLOW)
            input(Fore.CYAN + '~~> ')            

            print('\033c', end='') # clear terminal
        case 'options' | 'settings':

            print('\033c', end='') # clear terminal
        case 'quit':
            sys.exit(0)
        case _: # invalid input
            call_error(userInput)
