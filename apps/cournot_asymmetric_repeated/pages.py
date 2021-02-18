from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class SwitchingRound(Page):
    def is_displayed(self):
        return self.round_number == Constants.switching_round


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Decide(Page):
    form_model = 'player'
    form_fields = ['units']


class ResultsWaitPage(WaitPage):
    body_text = "Waiting for the other participant to decide."

    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def vars_for_template(self):
        return dict(other_player_units=self.player.get_others_units())


class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            # Note that we use participant class here as we
            # want the results for all subsessions.
            'all_round_payoffs': self.participant.payoff,
            'final_money': self.participant.payoff_plus_participation_fee()
        }

page_sequence = [SwitchingRound, Introduction, Decide, ResultsWaitPage, Results, FinalResults]
