from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
    pass


class Ask(Page):
   form_model = 'player'
   form_fields = ['name', 'age', 'is_student']


class Results(Page):
    pass


page_sequence = [WelcomePage, Ask, Results]
