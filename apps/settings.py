from os import environ


SESSION_CONFIGS = [
    dict(
       name='survey_second_session',
       display_name='My Survey (Second Session)',
       num_demo_participants=1,
       app_sequence=['my_survey']
    ),
    dict(
        name='surve_intro',
        display_name='Survey (Intro)',
        num_demo_participants=1,
        app_sequence=['survey'],
    ),
    dict(
        name='another_survey',
        display_name='Survey (Assignment)',
        num_demo_participants=1,
        app_sequence=['another_survey'],
    ),
    dict(
        name='raven',
        display_name='raven',
        num_demo_participants=2,
        app_sequence=['raven_matrix'],
    ),
    dict(
        name='raven_matrix_creating_session',
        display_name='raven_matrix_creating_session',
        num_demo_participants=2,
        app_sequence=['raven_matrix_creating_session'],
    ),
    dict(
        name='multiplication',
        display_name='multiplication',
        num_demo_participants=4,
        app_sequence=['multiplication'],
    ),
    dict(
        name='trust',
        display_name='trust',
        num_demo_participants=2,
        app_sequence=['trust'],
    ),
    dict(
        name='cournot',
        display_name='cournot',
        num_demo_participants=2,
        app_sequence=['cournot'],
    ),
    dict(
        name='cournot_asymmetric_repeated',
        display_name='cournot_asymmetric_repeated',
        num_demo_participants=4,
        app_sequence=['cournot_asymmetric_repeated'],
    ),
    dict(
        name='public_good_game',
        display_name='public_good_game',
        num_demo_participants=6,
        app_sequence=['public_good_game'],
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.40, participation_fee=4.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'smpg$(=6u4(dz0#60^m#^1(!$psqgrjw#f4s+$78ka$9-na-af'

INSTALLED_APPS = ['otree']
