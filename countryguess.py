import time, random, sys
from colorama import Fore, Back
from art import *


#* declares variables *#

show_observer_states = True
show_disputed_territories = True
show_unrecognised_territories = True


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
    'mauritania',
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

def africa_map(finished_countries):
    morocco = [
        ' ',
        ' ',
        '__' if show_disputed_territories else '  ',
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
    mauritania = [
        '   ',
        '   ',
        '       ',
        '        ',
        '_________',
    ]
    senegal = [
        '__  ',
        '___'
    ]
    mali = [
        '  ',
        '     ',
        '        ',
        '         ',
        '        ',
        '____',
        '      ',
        ' _'
    ]
    niger = [
        '    ',
        '         ',
        '         ',
        '_,-,_______',
    ]
    nigeria = [
        '        ',
        '       ',
        ' __ ',
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
    sudan = [
        '        ',
        '        ',
        '       ',
        '_______',
    ]
    south_sudan = [
        '       ',
        '    _',
        '    ',
    ]
    ethiopia = [
        ' ',
        '    ',
        '       ',
        '   ',
        '    ',
        '---',
    ]
    somalia = [
        '\'""""',
        '___  ',
        ' ',
        ' ,',
        ',',
    ]
    sierra_leone = [' ']
    liberia = [
        ' ',
        ' ',
    ]
    cote_divoire = [
        '  ',
        ' ',
    ]
    guinea = [
        '  ',
        '  ',
        ' ',
    ]
    ghana = [
        '  ',
        '  ',
    ]
    togo = [
        '||',
        '||',
    ]
    benin = [
        '||',
        '||',
    ]
    cameroon = [
        ' ',
        '   _',
        '     ',
        '_____',
    ]
    central_african_rep = [
        '    ',
        '           ',
        '_      __',
    ]
    kenya = [
        '    ',
        '   ',
        ' ',
    ]
    gabon = [
        '  ',
        ' ',
    ]
    rep_of_congo = [
        '  ',
        ' ',
        '--',
    ]
    dem_rep_of_congo = [
        '  """"""   ',
        '            ',
        '            ',
        '__        _',
        '__     ',
        '____',
    ]
    tanzania = [
        '    ',
        '      ',
        '       ',
        '      ',
        '__    ',
        ',,,',
    ]
    angola = [
        '   ',
        '      ',
        '         ',
        '         _',
        '__________',
    ]
    zambia = [
        '   ',
        '   ',
        '    ,,',
        '___,',
    ]
    mozambique = [
        '   ',
        '_   ',
        ' ',
        '  ',
        '_',
    ]
    namibia = [
        '      ---',
        '     ',
        '    ',
        '    ',
        '___',
    ]
    botswana = [
        '    ',
        '    ,,,',
        '_,',
    ]
    zimbabwe = [
        '  ,,',
        ',',
    ]
    south_africa = [
        ' ',
        '\'      ',
        '       ',
        '_',
        '        ',
        '       __',
        '_____'
    ]
    lesotho = ['[]']

    if finished_countries[0] and not show_disputed_territories: # morocco w/ western sahara
        morocco = fill_list(morocco)
    elif finished_countries[0] and show_disputed_territories: # morocco w/o western sahara
        morocco[:3] = fill_list(morocco[:3])
    if finished_countries[1] and show_disputed_territories: # western sahara
        morocco[3:6] = fill_list(morocco[3:6], '%')
    if finished_countries[2]: # algeria
        algeria = fill_list(algeria)
    if finished_countries[3]: # tunisia
        tunisia = fill_list(tunisia)
    if finished_countries[4]: # libya
        libya = fill_list(libya)
    if finished_countries[5]: # egypt
        egypt = fill_list(egypt)
    if finished_countries[6]: # mauritania
        mauritania = fill_list(mauritania)
    if finished_countries[7]: # senegal
        senegal = fill_list(senegal)
    if finished_countries[8]: # mali
        mali = fill_list(mali)
    if finished_countries[9]: # niger
        niger = fill_list(niger)
    if finished_countries[10]: # nigeria
        nigeria = fill_list(nigeria)
    if finished_countries[11]: # chad
        chad = fill_list(chad)
    if finished_countries[12]: # sudan
        sudan = fill_list(sudan)
    if finished_countries[13]: # south sudan
        south_sudan = fill_list(south_sudan)
    if finished_countries[14]: # ethiopia
        ethiopia = fill_list(ethiopia)
    if finished_countries[15] and not show_unrecognised_territories: # somalia w/ somaliland
        somalia = fill_list(somalia)
    elif finished_countries[15] and show_unrecognised_territories: # somaliland w/o somaliland
        somalia[2:5] = fill_list(somalia[2:5])
    if finished_countries[16] and show_unrecognised_territories: # somaliland
        somalia[:2] = fill_list(somalia[:2], '%')
    if finished_countries[17]: # sierra leone
        sierra_leone = fill_list(sierra_leone)
    if finished_countries[18]: # liberia
        liberia = fill_list(liberia)
    if finished_countries[19]: # cote d' ivoire
        cote_divoire = fill_list(cote_divoire)
    if finished_countries[20]: # guinea
        guinea = fill_list(guinea)
    if finished_countries[21]: # togo
        togo = fill_list(togo)
    if finished_countries[22]: # benin
        benin = fill_list(benin)
    if finished_countries[23]: # ghana
        ghana = fill_list(ghana)
    if finished_countries[24]: # cameroon
        cameroon = fill_list(cameroon)
    if finished_countries[25]: # central african republic
        central_african_rep = fill_list(central_african_rep)
    if finished_countries[26]: # kenya
        kenya = fill_list(kenya)
    if finished_countries[27]: # gabon
        gabon = fill_list(gabon)
    if finished_countries[28]: # republic of congo
        rep_of_congo = fill_list(rep_of_congo)
    if finished_countries[29]: # democratic republic of congo
        dem_rep_of_congo = fill_list(dem_rep_of_congo)
    if finished_countries[30]: # tanzania
        tanzania = fill_list(tanzania)
    if finished_countries[31]: # angola
        angola = fill_list(angola)
    if finished_countries[32]: # tanzania
        zambia = fill_list(zambia)
    if finished_countries[33]: # mozambique
        mozambique = fill_list(mozambique)
    if finished_countries[34]: # namibia
        namibia = fill_list(namibia)
    if finished_countries[35]: # botswana
        botswana = fill_list(botswana)
    if finished_countries[36]: # zimbabwe
        zimbabwe = fill_list(zimbabwe)
    if finished_countries[37]: # lesotho
        lesotho = fill_list(lesotho)
    if finished_countries[38]: # south africa
        south_africa = fill_list(south_africa)

    print('            ___________')
    print(f'           /{morocco[0]}|{algeria[0]}|{tunisia[0]}|')
    print(f'        ,\'{morocco[1]},\'{algeria[1]}\\{tunisia[1]}\',_    __')
    print(f'     ,\'{morocco[2]}/{algeria[2]}|{libya[0]}\',|{libya[1]}"\'-,,,,,,,')
    print(f'   ,/{morocco[3]}|\',{algeria[3]}|{libya[2]}|{egypt[0]} \\')
    print(f'   |{morocco[4]}|{mauritania[0]}|\'{algeria[4]},\\{libya[3]}|{egypt[1]}\\')
    print(f'   |{morocco[5]}|{mauritania[1]}|{mali[0]}\',{algeria[5]}\',{libya[4]}|{egypt[2]}\\')
    print(f'  /{mauritania[2]}|{mali[1]}\',{algeria[6]},_"""""---\'{libya[5]},\'{egypt[3]}\\')
    print(f' /{mauritania[3]}|{mali[2]}\'{algeria[7]}-\'"{niger[0]}|{chad[0]}|{sudan[0]}\',')
    print(f'|{mauritania[4]}|{mali[3]}|{niger[1]}/{chad[1]}|{sudan[1]}/{ethiopia[0]}\',,{somalia[0]}|')
    print(f'|{senegal[0]}|{mali[4]},{mali[5]}/{niger[2]}|{chad[2]}|{sudan[2]}/{ethiopia[1]}|{somalia[1]}/')
    print(f'\'\\{senegal[1]}|{mali[6]},\'_,\'|{niger[3]}|{chad[3]}|{sudan[3]}/{ethiopia[2]}\'{somalia[2]}/')
    print(f'  \\,\' _\',{mali[7]}/{guinea[0]},, ,\',|{nigeria[0]}|{chad[4]}\\{south_sudan[0]}|{ethiopia[3]}\'"{somalia[3]}\'')
    print(f'   \\{sierra_leone[0]}/{liberia[0]}|_ ,{guinea[1]}|{ghana[0]}\\{togo[0]}{benin[0]}{nigeria[1]},\'{cameroon[0]}|{chad[5]},\'|{south_sudan[1]}""{ethiopia[4]}|{somalia[4]}\'')
    print(f'    \'{liberia[1]},\'{cote_divoire[0]}\',{guinea[2]}|{ghana[1]}|{togo[1]}{benin[1]}{nigeria[2]},\'{cameroon[1]}|{chad[6]},\'{central_african_rep[0]}|{south_sudan[2]}|""{ethiopia[5]}/')
    print(f'       \'{cote_divoire[1]},"""\',\'""""""|{cameroon[2]}/{central_african_rep[1]}\\"""|{kenya[0]}/')
    print(f'                      |{cameroon[3]}|{central_african_rep[2]}\'\'"{tanzania[0]}\\{kenya[1]}|')
    print(f'                     |{gabon[0]}|{rep_of_congo[0]}/{dem_rep_of_congo[0]}|{tanzania[1]}\\{kenya[2]}/')
    print(f'                      \\{gabon[1]}/{rep_of_congo[1]}|{dem_rep_of_congo[1]}|{tanzania[2]}/')
    print(f'                       \\{rep_of_congo[2]}\'{dem_rep_of_congo[2]}|{tanzania[3]}/')
    print(f'                       |{angola[0]}\\{dem_rep_of_congo[3]}|{tanzania[4]}|')
    print(f'                       |{angola[1]}|{dem_rep_of_congo[4]}|{zambia[0]}\'{tanzania[5]}|')
    print(f'                       |{angola[2]}|{dem_rep_of_congo[5]}|{zambia[1]}/{mozambique[0]}|')
    print(f'                       /{angola[3]}|{zambia[2]}\'{mozambique[1]}|')
    print(f'                      |{angola[4]}|{zambia[3]}\'{zimbabwe[0]}\'{mozambique[2]}/')
    print(f'                       \\{namibia[0]}\'{botswana[0]}\\{zimbabwe[1]}/{mozambique[3]},\'')
    print(f'                        \\{namibia[1]}|{botswana[1]}\'{south_africa[0]}\\{mozambique[4]}/')
    print(f'                         |{namibia[2]}|{botswana[2]}\'{south_africa[1]}|/')
    print(f'                         |{namibia[3]}|{south_africa[2]}{lesotho[0]}{south_africa[3]}|')
    print(f'                          \\{namibia[4]}\'{south_africa[4]}/')
    print(f'                           \\{south_africa[5]},\'')
    print(f'                            \\{south_africa[6]}/        FoulWing')

def quiz(param):
    """country quiz"""
    match param:
        case 'africa':
            country_set = AFRICA

            if show_disputed_territories: # adds western sahara if required
                country_set.append(OTHER_DISPUTED_TERRITORIES[1])
            if show_unrecognised_territories: # adds somaliland if required
                country_set.append(UNRECOGNISED_TERRITORIES[0])

            finished_countries = [0] * len(country_set)

            finished_countries[2] = 1
            finished_countries[13] = 1
            finished_countries[17] = 1
            finished_countries[21] = 1
            finished_countries[27] = 1
            finished_countries[30] = 1

            africa_map(finished_countries)
        case _:
            return
    
    input('~~> ')


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
