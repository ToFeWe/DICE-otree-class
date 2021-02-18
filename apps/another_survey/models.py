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
    name_in_url = 'another_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18, max=99, label="What is your age?")
    gender = models.StringField(choices=['Male', 'Female', 'Other', 'I don\'t want to say it'], label='What is your gender?')
    math_grade = models.FloatField(blank=True, min=1, max=6, label='What was your last math grade?')
    falk_time = models.IntegerField(choices=list(range(11)), widget=widgets.RadioSelectHorizontal,
                                    label="How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?")

    # Additional field to check if the participant wants to revise the answer
    revise_question = models.BooleanField(label="Do you want to change your answers?")