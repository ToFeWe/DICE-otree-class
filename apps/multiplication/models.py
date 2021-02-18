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

import random
import itertools

author = 'Tobias Werner'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'multiplication'
    players_per_group = None
    num_rounds = 2

class Subsession(BaseSubsession):
    def creating_session(self):
        all_players = self.get_players()

        treatment = itertools.cycle([True, False])

        for p in all_players:
            p.first_number = random.randint(10,100)
            p.second_number = random.randint(10,100)
            p.correct_answer = p.first_number * p.second_number
            p.treatment_costly = next(treatment)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    correct_answer = models.IntegerField()
    user_answer = models.IntegerField(label="")
    correct = models.BooleanField()
    timeout_occured = models.BooleanField()
    treatment_costly = models.BooleanField()

    def check_answer(self):
        self.correct = self.correct_answer == self.user_answer
        self.calc_payoff()
        
    def calc_payoff(self):
        if self.correct:
            self.payoff = 1
        else:
            if self.treatment_costly:
                self.payoff = -1
            else:
                self.payoff = 0
        
        # Check at the end if the total payoff is negative
        # if so, reset it to zero.
        if (self.round_number == Constants.num_rounds) and (self.participant.payoff < 0):
            self.participant.payoff = 0