from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Tobias Werner'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'raven_matrix'
    players_per_group = None
    num_rounds = 3 # Change if you have more matrices

    payment_per_matrix = c(10)

    all_matrices = {
        1: {
            'file': 'SPM-1.bmp',
            'number_of_answers': 6,
            'correct_answer': 6,
            'id': 'B8'
        },
        2: {
            'file': 'SPM-2.bmp',
            'number_of_answers': 8,
            'correct_answer': 3,
            'id': 'C3'
        },
        3: {
            'file': 'SPM-3.bmp',
            'number_of_answers': 8,
            'correct_answer': 2,
            'id': 'C12'
        }
    }
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    matrix_answer = models.IntegerField(label="Your answer:")
    answer_correct = models.BooleanField()
    total_correct = models.IntegerField()

    # Dynamic form field validation
    def matrix_answer_choices(self):
        # If you want to randomize the matrices you can do so by changing self.round_number
        # to some id that you draw ex ante
        # +1 bcs not inclusive
        choices = list(range(1, Constants.all_matrices[self.round_number]['number_of_answers'] + 1))
        return choices


    def check_answer(self):
        if self.matrix_answer == Constants.all_matrices[self.round_number]['correct_answer']:
            self.answer_correct = True 
        else:
            self.answer_correct = False

    def set_payoff(self):
        self.total_correct = sum([p.answer_correct for p in self.in_all_rounds()])
        self.payoff = self.total_correct * Constants.payment_per_matrix