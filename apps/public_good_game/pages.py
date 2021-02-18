from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Rematching(Page):
    def is_displayed(self):
        return self.round_number == 6

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    
    def vars_for_template(self):
        return {
            'total_payoff': self.participant.payoff
        }


page_sequence = [Rematching, Contribute, ResultsWaitPage, Results]
