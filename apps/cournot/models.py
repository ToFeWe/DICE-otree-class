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


doc = """
In Cournot competition, firms simultaneously decide the units of products to
manufacture. The unit selling price depends on the total units produced. In
this implementation, there are 2 firms competing for 1 period.
"""


class Constants(BaseConstants):
    name_in_url = 'cournot'
    players_per_group = 2
    num_rounds = 1


    # Parameters from the paper
    alpha = 91
    theta_H = 25

    # Total production capacity of all players
    total_capacity = 90
    max_units_per_player = int(total_capacity / players_per_group)


    instructions_template = 'cournot/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    unit_price = models.CurrencyField()

    total_units = models.IntegerField(doc="""Total units produced by all players""")

    def set_payoffs(self):
        players = self.get_players()
        self.total_units = sum([p.units for p in players])
        self.unit_price = max(Constants.alpha - self.total_units, 0) # Max operator non binding with paper parameters
        for p in players:
            p.calculate_costs()
            p.payoff = self.unit_price * p.units - p.costs


class Player(BasePlayer):

    units = models.IntegerField(
        min=0,
        max=Constants.max_units_per_player,
        doc="""Quantity of units to produce""",
        label=f"How many units will you produce (from 0 to {Constants.max_units_per_player})?"
    )

    costs = models.IntegerField()

    def get_others_units(self):
        others = self.get_others_in_group()
        return [o.units for o in others]

    def calculate_costs(self):
        self.costs = Constants.theta_H * self.units