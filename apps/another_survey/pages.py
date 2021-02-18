from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questions(Page):
    form_model = 'player'
    form_fields = ['age','gender', 'math_grade', 'falk_time']

class Revise(Page):
    form_model = 'player'
    form_fields = ['revise_question']

class Resubmit(Page):
    form_model = 'player'
    form_fields = ['age','gender', 'math_grade', 'falk_time']

    def is_displayed(self):
        return self.player.revise_question

class Results(Page):
    pass


page_sequence = [Questions, Revise, Resubmit, Results]
