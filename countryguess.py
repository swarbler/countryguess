import time, random, sys
from colorama import Fore, Back
from art import *


#* declares variables *#

show_observer_states = False
show_western_sahara = False
show_kosovo = False
show_somaliland = False


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
# list of indexes of all countries and territories on map
AFRICA_INDEXES_ON_MAP = [34, 54, 0, 50, 28, 15, 32, 41, 31, 37, 38, 9, 47, 46, 19, 44, 55, 43, 27, 12, 23, 49, 2, 22, 7, 8, 25, 20, 11, 14, 48, 1, 52, 35, 36, 3, 53, 26, 45]
ASIA_INDEXES_ON_MAP = []
EUROPE_INDEXES_ON_MAP = [16, 29, 39, 11, 9, 42, 17, 38, 31, 4, 27, 12, 13, 8, 40, 18, 30, 10, 19, 21, 3, 33]
NORTH_AMERICA_INDEXES_ON_MAP = [4, 22, 15]
SOUTH_AMERICA_INDEXES_ON_MAP = []
OCEANIA_INDEXES_ON_MAP = [8, 0, 6]

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
    'sweden',
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
    'argentina',
    'bolivia',
    'brazil',
    'chile',
    'colombia',
    'ecuador',
    'guyana',
    'paraguay',
    'peru',
    'suriname',
    'uruguay',
    'venezuela',
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

# U.N. observer states
VATICAN_CITY_ALT = {
    'holy see': 'vatican city',
    'vatican': 'vatican city',
}

# disputed territories
WESTERN_SAHARA_ALT = {
    'sahrawi republic': 'western sahara',
    'sahrawi arab democratic republic': 'western sahara',
}


#* declares functions *#

def warning_tag(param): return Back.RED + param + Back.RESET

def toggle_tag(param): return '/' if param else ' '

def toggle_option(param):
    global show_observer_states
    global show_western_sahara
    global show_kosovo
    global show_somaliland

    match param:
        case 'observer states':
            show_observer_states = not show_observer_states
        case 'western sahara':
            show_western_sahara = not show_western_sahara
        case 'kosovo':
            show_kosovo = not show_kosovo
        case 'somaliland':
            show_somaliland = not show_somaliland

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
        case 'does_not_exist':
            print(f'{err} does not exist yet. Please try again later.')
        case 'not_a_country':
            print(f'{err} is not a country. Did you misspell it?')
        case 'range':
            print(f'{err} is not a valid input. You must input a number between {minR} and {maxR}. Please try again')
        case _:
            print(f'{err} is not a valid input. Please try again.')
    print('')
    input('~~> ')

    print('\033c', end='') # clear terminal


#* quiz functions *#

def dotdotdot(length=1, interval=.5):
    """small loading screen"""

    for dot in range(2): # repeats twice
        print('.', end='', flush=True) # no new line after each dot
        time.sleep(interval) # small delay between each dot
    print('.')
    time.sleep(length) # longer delay after last dot

def fill_list(param=[' '], fill='#'):
    filledList = []

    # iterates over every element in the list to replace with fill
    for i in param:
        filledList.append(len(i) * fill)
    
    return filledList

def africa_map(finished_countries):
    """map of africa"""

    morocco = [
        ' ',
        ' ',
        '__' if show_western_sahara else '  ',
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

    if finished_countries[34] and not show_western_sahara: # morocco w/ western sahara
        morocco = fill_list(morocco)
    elif finished_countries[34] and show_western_sahara: # morocco w/o western sahara
        morocco[:3] = fill_list(morocco[:3])
    if finished_countries[54] and show_western_sahara: # western sahara
        morocco[3:6] = fill_list(morocco[3:6], '%')
    if finished_countries[0]: # algeria
        algeria = fill_list(algeria)
    if finished_countries[50]: # tunisia
        tunisia = fill_list(tunisia)
    if finished_countries[28]: # libya
        libya = fill_list(libya)
    if finished_countries[15]: # egypt
        egypt = fill_list(egypt)
    if finished_countries[32]: # mauritania
        mauritania = fill_list(mauritania)
    if finished_countries[41]: # senegal
        senegal = fill_list(senegal)
    if finished_countries[31]: # mali
        mali = fill_list(mali)
    if finished_countries[37]: # niger
        niger = fill_list(niger)
    if finished_countries[38]: # nigeria
        nigeria = fill_list(nigeria)
    if finished_countries[9]: # chad
        chad = fill_list(chad)
    if finished_countries[47]: # sudan
        sudan = fill_list(sudan)
    if finished_countries[46]: # south sudan
        south_sudan = fill_list(south_sudan)
    if finished_countries[19]: # ethiopia
        ethiopia = fill_list(ethiopia)
    if finished_countries[44] and not show_somaliland: # somalia w/ somaliland
        somalia = fill_list(somalia)
    elif finished_countries[44] and show_somaliland: # somaliland w/o somaliland
        somalia[2:5] = fill_list(somalia[2:5])
    if finished_countries[55] and show_somaliland: # somaliland
        somalia[:2] = fill_list(somalia[:2], '%')
    if finished_countries[43]: # sierra leone
        sierra_leone = fill_list(sierra_leone)
    if finished_countries[27]: # liberia
        liberia = fill_list(liberia)
    if finished_countries[12]: # cote d' ivoire
        cote_divoire = fill_list(cote_divoire)
    if finished_countries[23]: # guinea
        guinea = fill_list(guinea)
    if finished_countries[49]: # togo
        togo = fill_list(togo)
    if finished_countries[2]: # benin
        benin = fill_list(benin)
    if finished_countries[22]: # ghana
        ghana = fill_list(ghana)
    if finished_countries[7]: # cameroon
        cameroon = fill_list(cameroon)
    if finished_countries[8]: # central african republic
        central_african_rep = fill_list(central_african_rep)
    if finished_countries[25]: # kenya
        kenya = fill_list(kenya)
    if finished_countries[20]: # gabon
        gabon = fill_list(gabon)
    if finished_countries[11]: # republic of congo
        rep_of_congo = fill_list(rep_of_congo)
    if finished_countries[14]: # democratic republic of congo
        dem_rep_of_congo = fill_list(dem_rep_of_congo)
    if finished_countries[48]: # tanzania
        tanzania = fill_list(tanzania)
    if finished_countries[1]: # angola
        angola = fill_list(angola)
    if finished_countries[52]: # zambia
        zambia = fill_list(zambia)
    if finished_countries[35]: # mozambique
        mozambique = fill_list(mozambique)
    if finished_countries[36]: # namibia
        namibia = fill_list(namibia)
    if finished_countries[3]: # botswana
        botswana = fill_list(botswana)
    if finished_countries[53]: # zimbabwe
        zimbabwe = fill_list(zimbabwe)
    if finished_countries[26]: # lesotho
        lesotho = fill_list(lesotho)
    if finished_countries[45]: # south africa
        south_africa = fill_list(south_africa)

    print(Fore.RED, end='')
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

def europe_map(finished_countries):
    """map of europe"""

    iceland = [
        '   ',
        ' ',
        '   ',
        '  ',
        '        ',
        '       ',
    ]
    norway = [
        '   ',
        '    ',
        '   ',
        '  ',
        '  ',
        ' ',
        '   ',
        '   ',
        '   ',
        '   ',
        '      ',
        '       ',
        '       ',
        '        ',
        '     ',
        '   ',
    ]
    sweden = [
        '    ',
        '     ',
        '       ',
        '       ',
        '      ',
        '       ',
        '        ',
        '      ',
        '     ',
        '      ',
        '      ',
        '       ',
        '    ',
        '       ',
        '     ',
        '    ',
        '   ',
    ]
    finland = [
        '      ',
        '     ',
        '      ',
        '      ',
        '       ',
        '        ',
        '       ',
        '    ',
        '  ',
        '     ',
        '     ',
        '       ',
        '  ',
    ]
    denmark = [
        ' ',
        ' ',
        '   ',
        ' ',
    ]
    uk = [
        ' ',
        '   ',
        '   ',
        '    ',
        '  ',
        '    ',
        '    ',
        '    ',
        '   ',
        '    ',
        '      ',
        '          ',
        '       ',
    ]
    ireland = [
        '  ',
        '    ',
        '     ',
    ]
    spain = [
        '      ',
        '                    ',
        '                ',
        '                 ',
        '              ',
        '             ',
        '            ',
        '            ',
        '           ',
    ]
    portugal = [
        '    ',
        '    ',
        '     ',
        '     ',
        '     ',
        '    ',
        '  ',
    ]
    netherlands = ['   ', '   ']
    belgium = ['    ', '  ']
    france = [
        '    ',
        '       ',
        '   ',
        '           ',
        '                  ',
        '              ',
        '             ',
        '             ',
        '               ',
        '                ',
        '        ',
        '  ', # corsica
    ]
    germany = [
        '   ',
        '          ',
        '           ',
        '            ',
        '            ',
        '         ',
        '          ',
        '        ',
        '          ',
    ]
    austria = [
        '     ',
        '     ',
    ]
    czechia = [
        '       ',
        '        ',
    ]
    slovakia = []
    switzerland = ['       ', '    ']
    italy = [
        '       ',
        '      ',
        '     ',
        '     ',
        '      ',
        '      ',
        '  ',
        '   ',
        '  ',
        '  ',
        ' ',
        '     ',
        '  ',
    ]
    poland = [
        '            ',
        '             ',
        '             ',
        '             ',
        '            ',
        '        ',
    ]
    estonia = ['   %    ', '         ']
    latvia = ['           ', '             ']
    lithuania = ['       ', '      ']
    belarus = [
        '   ',
        '             ',
        '               ',
        '           ',
        '             ',
    ]
    ukraine = [
        '     ',
        '                      ',
        '                =    *',
        '                         ',
        '                        ',
        '                        ',
        '                     ',
        '               ',
        '          ',
        '  ',
        '        ',
        '    ',
    ]
    russia = [
        '                               ',
        '                                ',
        '        ',
        '                                ',
        '          ',
        '                                 ',
        '        ',
        '                                   ',
        '  ',
        '                                    ',
        '   ',
        '                                   ',
        '   ',
        '                                    ',
        '                                         ',
        '                                           ',
        '    ',
        '                                    ',
        '      ',
        '                                   ',
        '                                      ',
        '   ',
        '                                       ',
        '     ',
        '                                      ',
        '                                      ',
        '                                  *   ',
        '                                   ',
        '                                 ',
        '                             ',
        '                           ',
        '                 @         ',
        '           .@     ',
        '                ',
        '              ',
        '             ',
        '             ',
        '                 ',
        '                  ',
        '                     ',
        '               ',
        '           ',
        '    ',
        '     ', # kaliningrad
    ]

    if finished_countries[16]: # iceland
        iceland = fill_list(iceland)
    if finished_countries[29]: # norway
        norway = fill_list(norway)
    if finished_countries[39]: # sweden
        sweden = fill_list(sweden)
    if finished_countries[11]: # finland
        finland = fill_list(finland)
    if finished_countries[9]: # denmark
        denmark = fill_list(denmark)
    if finished_countries[42]: # united kingdom
        uk = fill_list(uk)
    if finished_countries[17]: # ireland
        ireland = fill_list(ireland)
    if finished_countries[38]: # spain
        spain = fill_list(spain)
    if finished_countries[31]: # portugal
        portugal = fill_list(portugal)
    if finished_countries[27]: # netherlands
        netherlands = fill_list(netherlands)
    if finished_countries[4]: # belgium
        belgium = fill_list(belgium)
    if finished_countries[12]: # france
        france = fill_list(france)
    if finished_countries[13]: # germany
        germany = fill_list(germany)
    if finished_countries[2]: # austria
        austria = fill_list(austria)
    if finished_countries[8]: # czechia
        czechia = fill_list(czechia)
    if finished_countries[36]: # slovakia
        slovakia = fill_list(slovakia)
    if finished_countries[40]: # switzerland
        switzerland = fill_list(switzerland)
    if finished_countries[18]: # italy
        italy = fill_list(italy)
    if finished_countries[30]: # poland
        poland = fill_list(poland)
    if finished_countries[10]: # estonia
        estonia = fill_list(estonia)
    if finished_countries[19]: # latvia
        latvia = fill_list(latvia)
    if finished_countries[21]: # lithuania
        lithuania = fill_list(lithuania)
    if finished_countries[3]: # belarus
        belarus = fill_list(belarus)
    if finished_countries[41]: # ukraine
        ukraine = fill_list(ukraine)
    if finished_countries[33]: # russia
        russia = fill_list(russia)

    print(Fore.MAGENTA, end='')
    print(f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{russia[0]}')
    print(f':::::::::::::::::::::::::::::::::::::::::::::::@:+@ *:::::::::::  @:{russia[1]}')
    print(f':::::::::::::::::::::::::::::::::::::::::::::@:{norway[0]}@.{russia[2]}:::::  :{russia[3]}')
    print(f':::::::::::::::::::::::::::::::::::::::::::@{norway[1]}{finland[0]}{russia[4]}:::{russia[5]}')
    print(f':::::{iceland[0]}::::::::::::::::::::::::::::::::+::{norway[2]}{sweden[0]}{finland[1]}{russia[6]}::{russia[7]}')
    print(f':::::{iceland[1]}@{iceland[2]}:{iceland[3]}::::::::::::::::::::::::::@::{norway[3]}{sweden[1]}{finland[2]}{russia[8]}:::::::{russia[9]}')
    print(f':::::@{iceland[4]}:::::::::::::::::::::::::::{norway[4]}{sweden[2]}{finland[3]}{russia[10]}%:: ::{russia[11]}')
    print(f'::::::{iceland[5]}:::::::::::::::::::::::::::{norway[5]}%{sweden[3]}+{finland[4]}{russia[12]}+:::{russia[13]}')
    print(f':::::::::::::::::::::::::::::::::::::::{norway[6]}{sweden[4]}::@{finland[5]}{russia[14]}')
    print(f'::::::::::::::::::::::::::::::::::::::{norway[7]}{sweden[5]}::{finland[6]}{russia[15]}')
    print(f'::::::::::::::::::::::::::::::::::::{norway[8]}{sweden[6]}::{finland[7]}:%{finland[8]}@{russia[16]}::{russia[17]}')
    print(f'::::::::::::::::::-::::::::::::::::{norway[9]}%{sweden[7]}:::{finland[9]}::@@@{russia[18]}:{russia[19]}')
    print(f':::::::::::::::::::::::::::::::::{norway[10]}{sweden[8]}@:::%{finland[10]}*@: =:::{russia[20]}')
    print(f':::::::::::::::::::::::::::::::{norway[11]}{sweden[9]}:::::{finland[11]}:{russia[21]}:{russia[22]}')
    print(f':::::::::::::::::::::::@:::::::@{norway[12]}{sweden[10]}::::::{finland[12]}::::{russia[23]}{russia[24]}')
    print(f'::::::::::::::::::::::::::::::::{norway[13]}{sweden[11]}::::::{estonia[0]}@{russia[25]}')
    print(f'::::::::::::::::{uk[0]}:{uk[1]}:::::::::::{norway[14]}@@ :{sweden[12]}::::::+:{estonia[1]}{russia[26]}')
    print(f'::::::::::::::::{uk[2]}:::::::::::::{norway[15]}:::{sweden[13]}:::::::::{latvia[0]}{russia[27]}')
    print(f'::::::::::::::::@{uk[3]}:::::::::::::::{denmark[0]}::{sweden[14]}@: :::%{latvia[1]}{belarus[0]}{russia[28]}')
    print(f':::::::::::::::@@{uk[4]}@::::::::::::::@@{denmark[1]}:::{sweden[15]}@:::::{lithuania[0]}@{belarus[1]}{russia[29]}')
    print(f'::::::::::::{uk[5]}={uk[6]}:::::::::::::{denmark[2]}:={sweden[16]}:::::::::{lithuania[1]}@{belarus[2]}{russia[30]}')
    print(f':::::::::{uk[7]}{ireland[0]}:::@{uk[8]}:::::::::::::{denmark[3]}:::::::::::@:={russia[43]}{belarus[3]}@{ukraine[0]}{russia[31]}:')
    print(f':::::::::@{ireland[1]}=::::{uk[9]}:::::::::::={germany[0]}:@ :::{poland[0]}{ukraine[1]}{russia[32]}::::')
    print(f'::::::::@{ireland[2]}:::{uk[10]}:::::::{netherlands[0]}{germany[1]}{poland[1]}{ukraine[2]}@{russia[33]}:::::')
    print(f':::::::::::::::{uk[11]}::::{netherlands[1]}{germany[2]}{poland[2]}{ukraine[3]}{russia[34]}:::::')
    print(f':::::::::::::::@{uk[12]}::::{belgium[0]}@{germany[3]}{poland[3]}{ukraine[4]}{russia[35]}::::::')
    print(f'::::::::::::::::@:::::::{france[0]}{belgium[1]}@{germany[4]}@{poland[4]}{ukraine[5]}:{russia[36]}::::::')
    print(f'::::::::::::::::::::::@{france[1]}{germany[5]}@{czechia[0]}{poland[5]}  {ukraine[6]}:{russia[37]}::::')
    print(f'::::::::::::::{france[2]}::{france[3]}{germany[6]}{czechia[1]}=        {ukraine[7]}::::{russia[38]}::')
    print(f':::::::::::::::@{france[4]}{germany[7]}{austria[0]}           {ukraine[8]}:::@{ukraine[9]}::@:{russia[39]}')
    print(f':::::::::::::::::@{france[5]}@{germany[8]}:{austria[1]}           {ukraine[10]}::::{ukraine[11]}@:::::::@{russia[40]}')
    print(f'::::::::::::::::::{france[6]}{switzerland[0]}                           @  :::::::::::::::::::::{russia[41]}')
    print(f':::::::::::::::::::{france[7]}{switzerland[1]}@        @  :                  ::::::::::::::::::::::       {russia[42]}')
    print(f'::::::::::::::::::{france[8]}{italy[0]}:: :            %          :::::::::::::::::::              ')
    print(f'::::+{spain[0]}:::::::{france[9]}{italy[1]}::::@                     :::::::::                   =   @ ')
    print(f'::::{spain[1]}{france[10]}:::::{italy[2]}::::     @  =            ::::::                        @ @')
    print(f'::::{portugal[0]}@{spain[2]}::::::::::@:%{italy[3]}:::::::@     =@                                          ')
    print(f'::::{portugal[1]}{spain[3]}:::::::::{france[11]}:::{italy[4]}:@:::::: *   @   :*@ : @                               ')
    print(f'::{portugal[2]}{spain[4]}::::::::::::::::::::::@{italy[5]}::::  @  * *=:::                                   ')
    print(f'::{portugal[3]}{spain[5]}::::::::::::::={italy[6]}:::::::::{italy[7]}::=:::     ::::::                  @ @              ')
    print(f'::{portugal[4]}{spain[6]}:::::@::::::::::{italy[8]}:::::::::::{italy[9]}::::::@   :  ::::@              :::                ')
    print(f':::{portugal[5]}{spain[7]}::::::::::::::::::::::::::::::{italy[10]}::::::: :   : :::@::@     :::@@::=::@               ')
    print(f'::::::{portugal[6]}{spain[8]}::::::::::::::::::::::::::{italy[11]}::::::::::::  ::::@:@:  :::::::::  ::::               ')
    print(f':::::::::::::::::::::::::::::::::::  ::::::@{italy[12]}:::::::::::::: :::::::@::::::::::::::::               ')
    print(f'::::::   :::::::+*                   %::::::::::::::::::::::::    ::::::::::::::::::                ')
    print(f'::::                                  ::::::::::::::::::::::::::::::::::::::::::::::                ')

def north_america_map(finished_countries):
    """map of north america"""

    canada = [
        '         ',
        '            ',
        '                      ',
        '                   ',
        '                    ',
        '                  ',
        '                       ',
        '            ',
        '                                      ',
        '                          ',
        '      ',
        '                                ',
        '      ',
    ]
    usa = [
        '    ',
        '      ',
        '          ',
        '         ',
        '    ',
        '   ',
        '                        ',
        '   ',
        '                          ',
        '       ',
        '                           ',
        '     ',
        '                                ',
        '                                ',
        '                                ',
        '                              ',
        '                          ',
        '           ',
        '     '
    ]
    mexico = [
        '       ',
        '  ',
        '  ',
        '        ',
        '         ',
        '         ',
        '      ',
        '       ',
    ]

    if finished_countries[4]: # canada
        canada = fill_list(canada)
    if finished_countries[22]: # united states of america
        usa = fill_list(usa)
    if finished_countries[15]: # mexico
        mexico = fill_list(mexico)

    print(Fore.YELLOW, end='')
    print('                                        @@@ @                    ')
    print('                                             @ @@@               ')
    print('                                   @  @          @ @             ')
    print('                                  @ @ @            @@@           ')
    print('             @@@          @@          @ @@                       ')
    print(f'         @@@{usa[0]}@           @    @@@                 @           ')
    print(f'      @@ @{usa[1]}@      @ @    @ @ @@         @@     @            ')
    print(f'     @{usa[2]}@    @@  @  @ @@@@@     @                        ')
    print(f'    @{usa[3]}@{canada[0]}@    @@@ @  @ @          @    @          ')
    print(f'    @{usa[4]}@{usa[5]}@{canada[1]}@  @@     @      @                     ')
    print(f'    @     @@ @{canada[2]}@ @  @ @                     ')
    print(f'           @@{canada[3]}@  @     @@                      ')
    print(f'          @{canada[4]}@           @@                    ')
    print(f'           @@{canada[5]}@                  @@@            ')
    print(f'          @{canada[6]}@     @{canada[7]}@           ')
    print(f'          @{canada[8]}@@    @@        ')
    print(f'            @{canada[9]}@@{canada[10]}@@@               ')
    print(f'             @{canada[11]}@@   @@            ')
    print(f'             @@@@@@@@@@@@@@@@@@@@@@@ @{canada[12]}@@@                  ')
    print(f'             @{usa[6]}@ @@@@{usa[7]}@                 ')
    print(f'            @{usa[8]}@{usa[9]}@                 ')
    print(f'           @{usa[10]}@{usa[11]}@                   ')
    print(f'           @{usa[12]}@                    ')
    print(f'           @{usa[13]}@                    ')
    print(f'           @{usa[14]}@                    ')
    print(f'            @{usa[15]}@                     ')
    print(f'              @{usa[16]}@                       ')
    print(f'                @@@@@@@@{usa[17]}@@  @   @                     ')
    print(f'               @@{mexico[0]}@@{usa[18]}@          @ @ @                  ')
    print(f'                @{mexico[1]}@{mexico[3]}@                 @                  ')
    print(f'                  {mexico[2]}@{mexico[4]}            @@ @@                  ')
    print(f'                   @  @{mexico[5]}               @@             @  ')
    print(f'                       @{mexico[6]}@     @          @@               @')
    print(f'                        @{mexico[7]}@@@   @@                         ')
    print(f'                            @        @@@@ @@                     ')
    print(f'                                    @ @                          ')
    print(f'                                         @@@                     ')
    print(f'                                            @  @ @@              ')

def south_america_map(finished_countries):
    """map of south america"""
    print(Fore.GREEN, end='')
    print(':::::::::::::::::: :::::::::::::::::::::::::::::::')
    print(':::::::::::::::   :        :::::::::::::::::::::::')
    print('::::::::::::::              @:::::::::::::::::::::')
    print('::::::::::::::             @@     ::::::::::::::::')
    print('::::::::::::::              @@@     ::::::::::::::')
    print('::::::::::::          =             @:::::::::::::')
    print(':::::::::::     =                       ::::::::::')
    print(':::::::::::+                %                 ::::')
    print(':::::::::::                                      :')
    print('::::::::::::                                      ')
    print(':::::::::::::                              :     :')
    print('::::::::::::::                                 :::')
    print(':::::::::::::::                               ::::')
    print(':::::::::::::::::   :                         ::::')
    print(':::::::::::::::::::                           ::::')
    print('::::::::::::::::::::                         :::::')
    print('::::::::::::::::::::              :         ::::::')
    print(':::::::::::::::::::  @                 :::::::::::')
    print(':::::::::::::::::::                   ::::::::::::')
    print(':::::::::::::::::::                   ::::::::::::')
    print(':::::::::::::::::::       :          :::::::::::::')
    print(':::::::::::::::::::              % :::::::::::::::')
    print('::::::::::::::::::                ::::::::::::::::')
    print(':::::::::::::::::: :           :::::::::::::::::::')
    print(':::::::::::::::::              :::::::::::::::::::')
    print(':::::::::::::::::         ::::::::::::::::::::::::')
    print('::::::::::::::::: %       ::::::::::::::::::::::::')
    print(':::::::::::::::: :       :::::::::::::::::::::::::')
    print(':::::::::::::::::       ::::::::::::::::::::::::::')
    print('::::::::::::::::      ::::::::::::::::::::::::::::')
    print('::::::::::::::::       :::::::::::::::::::::::::::')
    print(':::::::::::::::  @    +:::::::::::::::::::::::::::')
    print('::::::::::::::::@     ::::::::::::::::::::::::::::')
    print(':::::::::::::::@:    :::::::-@::::::::::::::::::::')
    print(':::::::::::::::::@=: :::::::::::::::::::::::::::::')
    print('::::::::::::::::: ::  ::::::::::::::::::::::::::::')
    print('::::::::::::::::::::-:::::::::::::::::::::::::::::')

def oceania_map(finished_countries):
    """map of oceania"""

    papua_new_guinea = [
        '    ',
        '      ',
        '        ',
        '  ',
        '  ',
        ' ',
    ]
    australia = [
        '   ',
        '       ',
        '  ',
        '   ',
        '       ',
        '                ',
        '     ',
        '                    ',
        '     ',
        '                                ',
        '                                  ',
        '                                         ',
        '                                              ',
        '                                                 ',
        '                                                   ',
        '                                                    ',
        '                                                     ',
        '                                                     ',
        '                                                    ',
        '                                                   ',
        '                                                   ',
        '             ',
        '                         ',
        '          ',
        '    ',
        '                  ',
        '    ',
        '                ',
        '             ',
        '             ',
        '         ',
        '    ',
        '  ',
    ]
    new_zealand = [
        '  ',
        '  ',
        ' @',
        '   @',
    ]

    if finished_countries[8]: # papua new guinea
        papua_new_guinea = fill_list(papua_new_guinea)
    if finished_countries[0]: # australia
        australia = fill_list(australia)
    if finished_countries[6]: # new zealand
        new_zealand = fill_list(new_zealand)

    print(Fore.BLUE, end='')
    print('                                                                                                    ')
    print('                                                                                                    ')
    print('                                                                                 %% %@              ')
    print(f'                                                                      %%%         @%                ')
    print(f'                                                                      %@%                           ')
    print('                                                                                                    ')
    print('                                                                                                    ')
    print('                                                                                                    ')
    print('                                                                                                    ')
    print(f'                                                                               %                    ')
    print(f'                                                     %%%  %%                                        ')
    print(f'                                              %%%%          %@%                                     ')
    print(f'                                             @%{papua_new_guinea[0]}%%       %%%%                                    ')
    print(f'                                             %{papua_new_guinea[1]}%@% %%%%@%   %%                                 ')
    print(f'                                             %{papua_new_guinea[2]}%%          @%%                               ')
    print(f'                                             %{papua_new_guinea[3]}@%%%%{papua_new_guinea[4]}@            %@%@%%                          ')
    print(f'                                             %%%%    % %%%           @{papua_new_guinea[5]}%%@%                         ')
    print(f'                                                      %@%@%%            @%@%         %%             ')
    print(f'                             %%@%%%           %%                                                    ')
    print(f'                             @%%%{australia[0]}%%%%     %%%%                                                   ')
    print(f'                       %%%  %%{australia[1]}%       %{australia[2]}@                                                   ')
    print(f'                     @%{australia[3]}%%%       %{australia[4]}%%  %%%                             %                   ')
    print(f'                   %%{australia[5]}%@%    %{australia[6]}@                             %%                %%')
    print(f'                %%%@{australia[7]}%% %%{australia[8]}%                                   %%       %%@% ')
    print(f'                @%{australia[9]}%                                           %@%   ')
    print(f'              %%{australia[10]}%%%                             %                 ')
    print(f'       %%%%%{australia[11]}%                    %%% %%                    ')
    print(f'    %%%{australia[12]}%%                    %%@%@%          %%       ')
    print(f'   %%{australia[13]}%@                                            ')
    print(f'  %%{australia[14]}%%                                           ')
    print(f'  %%{australia[15]}%%                                          ')
    print(f'  @%{australia[16]}%                                          ')
    print(f'  %{australia[17]}%                                           ')
    print(f'  @%{australia[18]}@                                           ')
    print(f'  @%{australia[19]}%%                                           ')
    print(f'  %{australia[20]}%%                                            ')
    print(f'  %@{australia[21]}@ %%%%%%@%%{australia[22]}%                                              ')
    print(f'  %{australia[23]}%%@           %{australia[24]}%{australia[25]}%%                                               ')
    print(f'%%{australia[26]}%@%%%%@               %%%%%{australia[27]}%%                           %                     ')
    print(f'  %%%                       %@%@%%{australia[28]}%%                             %%%                   ')
    print(f'                             %  %{australia[29]}%                               @@%                   ')
    print(f'                                %{australia[30]}%%%@                                %%%@%%                ')
    print(f'                                  %@%%%@%                                  %%%{new_zealand[0]}%%%                 ')
    print(f'                                   %{australia[31]}%@                                 %{new_zealand[1]}%%                    ')
    print(f'                                   %%%@%%                             %%@%@%%%                      ')
    print(f'                                  %%{australia[32]}%@                            %% @%%                          ')
    print(f'                                  %%%@                          %%%% %%                             ')
    print(f'                                                            %%%%{new_zealand[2]}%%              %                 ')
    print(f'                                                          %%{new_zealand[3]}%                                   ')
    print(f'                                                          %%%%                                      ')

def quiz(param):
    """country quiz"""
    # declares variables
    end_game = False

    # declares lists
    indexes_on_map = []
    country_set = []
    country_alt_set = []

    # constants
    GIVEUP_COMMANDS = ['give up', 'giveup', 'forfeit', 'surrender', 'quit', 'i quit']

    match param:
        case 'africa':
            country_set = AFRICA
            country_alt_set = AFRICA_ALT

            if show_western_sahara: # adds western sahara if required
                country_set.append('western sahara')
                country_alt_set = country_alt_set | WESTERN_SAHARA_ALT # sahrawi arab democratic republic
            else:
                country_set.append(0) # blank entry

            if show_somaliland: # adds somaliland if required
                country_set.append('somaliland')
            else:
                country_set.append(0) # blank entry

            finished_countries = [0] * len(country_set)
            indexes_on_map = AFRICA_INDEXES_ON_MAP
        case 'asia':
            call_error(param, 'does_not_exist')

            return
        case 'europe':
            country_set = EUROPE
            country_alt_set = EUROPE_ALT

            if show_observer_states: # adds vatican city if required
                country_set.append('vatican city')
                country_alt_set = country_alt_set | VATICAN_CITY_ALT # holy see / vatican
            else:
                country_set.append(0) # blank entry

            if show_kosovo: # adds kosovo if required
                country_set.append('kosovo')
            else:
                country_set.append(0) # blank entry

            finished_countries = [0] * len(country_set)
            indexes_on_map = EUROPE_INDEXES_ON_MAP
        case 'north america':
            country_set = NORTH_AMERICA
            country_alt_set = NORTH_AMERICA_ALT

            finished_countries = [0] * len(country_set)
            indexes_on_map = NORTH_AMERICA_INDEXES_ON_MAP
        case 'south america':
            country_set = SOUTH_AMERICA
            country_alt_set = {}

            finished_countries = [0] * len(country_set)
            indexes_on_map = SOUTH_AMERICA_INDEXES_ON_MAP
        case 'oceania':
            country_set = OCEANIA
            country_alt_set = {}

            finished_countries = [0] * len(country_set)
            indexes_on_map = OCEANIA_INDEXES_ON_MAP
        case _:
            return
    
    while not end_game:
        # lists are used to record all guessed countries
        listed_indexes = [] # the indexes of the countries in country_set
        listed_countries = [] # the names of the countries

        # iterates over every country to find the indexes and names of guessed countries
        for i in range(len(country_set)):
            if finished_countries[i]:
                listed_indexes.append(i)
                listed_countries.append(country_set[i])
        
        # checks whether user has won
        if len(listed_countries) == len(country_set):
            end_game = True
            print(Fore.MAGENTA)
            print('>> you got all the countries!')
            break # break out of loop if all countries have been guessed

        print('\033c', end='') # clear terminal

        # prints map with guessed countries
        match userInput:
            case 'africa':
                africa_map(finished_countries)
            case 'europe':
                europe_map(finished_countries)
            case 'north america':
                north_america_map(finished_countries)
            case 'south america':
                south_america_map(finished_countries)
            case 'oceania':
                oceania_map(finished_countries)

        # prints pairs of countries 
        print(Fore.GREEN)
        for i in range(1, len(listed_countries), 2): # iterates every two countries
            # countries not shown on the map are labelled
            if listed_indexes[i-1] in indexes_on_map:
                print(f'~ {listed_countries[i-1]}   \t\t\t\t', end='')
            else:
                print(f'~ {listed_countries[i-1]} (not shown on map)  \t', end='')
            
            # countries not shown on the map are labelled
            if listed_indexes[i] in indexes_on_map:
                print(f'~ {listed_countries[i]}')
            else:
                print(f'~ {listed_countries[i]} (not shown on map)')
        
        # prints remainder if odd number of guessed countries
        if len(listed_countries) % 2 == 1:
            # countries not shown on the map are labelled
            if listed_indexes[-1] in indexes_on_map:
                print(f'~ {listed_countries[-1]}')
            else:
                print(f'~ {listed_countries[-1]} (not shown on map)')
        
        print(Fore.MAGENTA)
        print(f'{len(listed_countries)}/{len(country_set)}') # shows how many countries you have guessed correctly
        
        print(Fore.YELLOW)
        userAction = input('~~> ')

        if userAction in listed_countries: # tells user country has already been guessed
            print(Fore.YELLOW)
            print('>> silly goose! you already have that country!')

            input('~~> ')
        elif userAction in country_set: # adds country
            finished_countries[country_set.index(userAction)] = 1
            print(Fore.GREEN)
            print(f'>> country added: {userAction}')

            input('~~> ')
        elif userAction in country_alt_set: # checks if user inputted alternative name for country
            if country_alt_set[userAction] in listed_countries: # tells user country has already been guessed
                print(Fore.YELLOW)
                print('>> silly goose! you already have that country!')
            else: # adds country
                finished_countries[country_set.index(country_alt_set[userAction])] = 1
                print(Fore.GREEN)
                print(f'>> country added: {country_alt_set[userAction]}')

            input('~~> ')
        elif userAction in GIVEUP_COMMANDS: # user gives up
            end_game = True
            print(Fore.RED)
            print('>> You have given up')

            input('~~> ')
        else: # tells user that is not a valid country
            print(Fore.RED)
            print('>> silly goose, that\'s not a valid country!')

            input('~~> ')

    dotdotdot()

    # tells user final score
    print(Fore.MAGENTA)
    print(f'you got {len(listed_countries)}/{len(country_set)} of the countries of {param}!') # shows how many countries you have guessed correctly

    # waits for user to exit
    input('~~> ')

def world_quiz():
    """countries of the world quiz"""
    pass


#* program *#

while True:
    print(Fore.GREEN, end='')
    tprint('countryguess', 'soft')

    print(Fore.BLUE)
    print('Choose an option:')

    print(Fore.GREEN)
    print('~ countries of the world (not completed)')
    print('~ continents')
    print(Fore.RED +     '   ~ africa')
    print(Fore.CYAN +    '   ~ asia (not completed)')
    print(Fore.MAGENTA + '   ~ europe (partially completed)')
    print(Fore.YELLOW +  '   ~ north america')
    print(Fore.GREEN +   '   ~ south america (partially completed)')
    print(Fore.BLUE +    '   ~ oceania')

    print(Fore.YELLOW)
    print('~ find a country')

    print(Fore.MAGENTA)
    print('~ options')
    print(Fore.CYAN +  f'   ~ [{toggle_tag(show_observer_states)}] show U.N. observer states')
    print(Fore.CYAN + '        (Vatican City and Palestine)')
    print(Fore.GREEN + f'   ~ [{toggle_tag(show_western_sahara)}] show western sahara')
    print(Fore.GREEN + f'   ~ [{toggle_tag(show_kosovo)}] show kosovo')
    print(Fore.BLUE +  f'   ~ [{toggle_tag(show_somaliland)}] show somaliland')

    print(Fore.RED)
    print('~ quit')

    print(Fore.YELLOW)
    userInput = input('~~> ').lower()

    match userInput:
        case 'countries of the world' | 'countries' | 'world':
            call_error(userInput, 'does_not_exist')
        case 'africa' | 'asia' | 'europe' | 'north america' | 'south america' | 'oceania':
            quiz(userInput)

            print('\033c', end='') # clear terminal
        case 'find' | 'find a country' | 'find country':
            print(Fore.CYAN)
            print('please enter a country')
            userInput = input('~~> ')

            print('')
            if userInput in AFRICA or userInput in AFRICA_ALT:
                print(Fore.RED + 'this country is in africa')
            elif userInput in ASIA or userInput in ASIA_ALT:
                print(Fore.CYAN + 'this country is in asia')
            elif userInput in EUROPE or userInput in EUROPE_ALT:
                print(Fore.MAGENTA + 'this country is in europe')
            elif userInput in NORTH_AMERICA or userInput in NORTH_AMERICA_ALT:
                print(Fore.YELLOW + 'this country is in north america')
            elif userInput in SOUTH_AMERICA:
                print(Fore.GREEN + 'this country is in south america')
            elif userInput in OCEANIA:
                print(Fore.BLUE + 'this country is in oceania')
            elif userInput == 'vatican city' or userInput == 'vatican' or userInput == 'holy see' or userInput == 'palestine' or userInput in VATICAN_CITY_ALT:
                print(Fore.BLUE + 'this is a U.N. observer state')
            elif userInput == 'western sahara' or userInput == 'kosovo' or userInput in WESTERN_SAHARA_ALT:
                print(Fore.YELLOW + 'this is a disputed territory')
            elif userInput == 'somaliland':
                print(Fore.RED + 'this is somaliland, a "country" that is unrecognised by any U.N. member state')
            else:
                print(Fore.RED + 'this is not a country or territory')
            
            print(Fore.YELLOW)
            input(Fore.CYAN + '~~> ')            

            print('\033c', end='') # clear terminal
        case 'show observer states' | 'observer states' | 'show un observer states' | 'un observer states' | 'show u.n. observer states' | 'u.n. observer states' | 'un observers' | 'u.n. observers' | 'observers' | 'show un observers' | 'show u.n. observers' | 'show observers':
            # toggles whether U.N. observer states (Vatican City and Palestine) are enabled
            toggle_option('observer states')
        case 'show western sahara' | 'western sahara' | 'show sahrawi republic' | 'sahrawi republic' | 'show sahrawi arab democratic republic' | 'sahrawi arab democratic republic':
            # toggles whether Western Sahara (a disputed territory) is enabled
            toggle_option('western sahara')
        case 'show kosovo' | 'kosovo':
            # toggles whether Kosovo (a disputed territory) is enabled
            toggle_option('kosovo')
        case 'show somaliland' | 'somaliland':
            # toggles whether Somaliland (a territory unrecognised by any U.N. member state) is enabled
            toggle_option('somaliland')
        case 'quit':
            sys.exit(0)
        case _: # invalid input
            call_error(userInput)










