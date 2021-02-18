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
    name_in_url = 'raven_matrix_creating_session'
    players_per_group = None
    num_rounds = 3  # Change if you have more matrices

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
    def creating_session(self):
        all_players = self.get_players()

        # Python 3.7+:
        # Dictionary iteration order is guaranteed to be in order of insertion.
        for p in all_players:
            p.matrix_file = Constants.all_matrices[self.round_number]['file']
            p.matrix_id = Constants.all_matrices[self.round_number]['id']
            p.matrix_correct_answer = Constants.all_matrices[self.round_number]['correct_answer']
            p.matrix_number_of_answers = Constants.all_matrices[self.round_number]['number_of_answers']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Save the input also in the database
    matrix_file = models.StringField()
    matrix_id = models.StringField()
    matrix_correct_answer = models.IntegerField()
    matrix_number_of_answers = models.IntegerField()

    # Fields for response related data
    matrix_answer = models.IntegerField(label="Your answer:")
    answer_correct = models.BooleanField()
    total_correct = models.IntegerField()

    # Dynamic form field validation
    def matrix_answer_choices(self):
        choices = list(range(1, self.matrix_number_of_answers + 1))
        return choices

    def check_answer(self):
        if self.matrix_answer == self.matrix_correct_answer:
            self.answer_correct = True
        else:
            self.answer_correct = False

    def set_payoff(self):
        self.total_correct = sum([p.answer_correct for p in self.in_all_rounds()])
        self.payoff = self.total_correct * Constants.payment_per_matrix
