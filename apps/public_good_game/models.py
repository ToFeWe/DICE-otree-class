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


author = 'Adapted from oTree examples'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_good_game'
    players_per_group = 3
    num_rounds = 10

    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number <= 5:
            if self.round_number == 1:
                self.group_randomly()
            else:
                self.group_like_round(1)
        else:
            if self.round_number == 6:
                self.group_randomly()
            else:
                self.group_like_round(6)

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        self.individual_share = (
            self.total_contribution * Constants.multiplier / Constants.players_per_group
        )
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="How much will you contribute?"
    )
