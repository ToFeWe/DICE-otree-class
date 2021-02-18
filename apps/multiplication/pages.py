from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Multiplication(Page):
    timeout_seconds = 10
    form_fields = ['user_answer']
    form_model = 'player'

    def vars_for_template(self):
        return {
            'round_number': self.round_number
        }
    def before_next_page(self):
        if self.timeout_happened:
            self.player.user_answer = -1 # Some value to record missing values here, Note that this is not best practice
            self.player.timeout_occured = True
        self.player.check_answer()


class Results(Page):

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        total_correct = sum([p.correct for p in player_in_all_rounds])
        total_false = sum([not p.correct for p in player_in_all_rounds])

        return {
            'total_correct': total_correct,
            'total_false': total_false,
            'total_money': self.participant.payoff_plus_participation_fee()
        }
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    

page_sequence = [Multiplication, Results]
