from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):

    # Welcome Page only shown in the first round
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'real_world_currency_per_point': self.session.config['real_world_currency_per_point'],
            'participation_fee': self.session.config['participation_fee']
        }

class Matrix(Page):
    form_model = 'player'
    form_fields = ['matrix_answer']

    def vars_for_template(self):
        # Compose the link to the files
        # oTree will look automatically in the *static* folder
        imgPath = './' + self.player.matrix_file

        return {
            'imgPath': imgPath
        }

    def before_next_page(self):
        self.player.check_answer()
        if self.round_number == Constants.num_rounds:
            self.player.set_payoff()

    # Note that the page is shown in every round
    

class Results(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            'money': self.player.payoff.to_real_world_currency(self.session)
        }

    def is_displayed(self):

        # Results page is only shown in the last round
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


page_sequence = [Welcome, Matrix, Results]
