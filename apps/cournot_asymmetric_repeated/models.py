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
    name_in_url = 'cournot_asymmetric_repeated'
    players_per_group = 2
    num_rounds = 4

    switching_round = num_rounds / 2 + 1  # Switch after half is done

    instructions_template = 'cournot_asymmetric_repeated/instructions.html'
    instructions_costs = 'cournot_asymmetric_repeated/cost_info.html'

    alpha = 91
    theta_H = 25
    theta_L = 13

    role_high_costs = 'high_costs'
    role_low_costs = 'low_costs'

    # Total production capacity of all players
    total_capacity = 90
    max_units_per_player = int(total_capacity / players_per_group)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number < Constants.switching_round:
            pass
        elif self.round_number == Constants.switching_round:
            matrix = self.get_group_matrix()
            for row in matrix:
                row.reverse()
            # Save it
            self.set_group_matrix(matrix)

        else:
            self.group_like_round(Constants.switching_round)    

class Group(BaseGroup):
    unit_price = models.CurrencyField()
    total_units = models.IntegerField(doc="""Total units produced by all players""")

    def set_payoffs(self):
        players = self.get_players()
        self.total_units = sum([p.units for p in players])
        self.unit_price = max(Constants.alpha - self.total_units, 0)  # Max operator non binding with paper parameters
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
        if self.role == Constants.role_low_costs:
            self.costs = Constants.theta_L * self.units
        else:
            self.costs = Constants.theta_H * self.units
