from . import *
import random
import yaml


class Bet:
    with open('var/stats.yaml') as f:
        stats_config = yaml.load(f)

    high_stats = stats_config['high_stats']
    low_stats = stats_config['low_stats']

    @property
    def win_conditions(self):
        wager_with_value = sum([x.value for x in self.wager_with])
        wager_for_value = sum([x.value for x in self.wager_for])
        value_diff = wager_for_value - wager_with_value
        used_stats = []
        print('value diff', value_diff)
        if wager_with_value > wager_for_value:
            win_conditions = [self._generate_win_condition_(easy=True)]
        else:
            win_conditions = []
            conditions_value = 0
            for i in range(20):
                condition = self._generate_win_condition_()
                condition_value = condition[-1]
                condition_stat = condition[1]
                if conditions_value + condition_value <= value_diff and condition_stat not in used_stats:
                    win_conditions.append(condition)
                    used_stats.append(condition_stat)
                    conditions_value += condition_value
        return win_conditions

    def __init__(self, better=None, betee=None, wager_with=None, wager_for=None):
        if not all([better, bettee, wager_for, wager_with]):
            error_message = f"""
            ALL PARAMETERS ARE REQUIRED
            +=============+=========+==============+
            |  Parameter  | Default |   You Set    |
            +=============+=========+==============+
            | better      | None    | {better}     |
            +-------------+---------+--------------+
            | bettee      | None    | {bettee}     |
            +-------------+---------+--------------+
            | wager_with  | None    | {wager_with} |
            +-------------+---------+--------------+
            | wager_for   | None    | {wager_for}  |
            +-------------+---------+--------------+
            """
            raise ValueError(error_message)

        self.better = better
        self.betee = betee
        self.wager_with = wager_with
        self.wager_for = wager_for

    def _generate_win_condition_(self, easy=False):
        highlow = random.choice(['high', 'low'])
        percentage = random.random()
        if easy:
            percentage = .01
        if highlow == 'high':
            stat_key = random.choice(list(self.high_stats.keys()))
            min_value, max_value = self. high_stats[stat_key]
            out_value = round(percentage*max_value+min_value)
            dollar_value = out_value / max_value * 1000
        else:
            stat_key = random.choice(list(self.low_stats.keys()))
            min_value, max_value = self.low_stats[stat_key]
            out_value = round((1-percentage)*max_value)
            dollar_value = ((max_value - out_value) / max_value) * 1000
            if dollar_value < 0:
                # Sometimes this produces negative dollar values
                # if this happens we want to spit out debugging
                # information
                print(stat_key, min_value, max_value)
                print('Out Value', out_value)
                print('Dollar Value', dollar_value)
            elif dollar_value == 0:
                # Even if the challenge is as easy as possible
                # it can't have a value of zero, since that
                # would mean that the program could produce
                # an unlimited number of win conditions, which
                # becomes infinitely difficult
                dollar_value = 100

        return highlow, stat_key, out_value, dollar_value

    def render_conditions(self):
        string_list = []
        for condition in self.win_conditions:
            highlow, stat_key, out_value, dollar_value = condition
            if highlow == 'high':
                rendered_string = f'Get at least {out_value} {stat_key}'
            else:
                rendered_string = f'Get no more than {out_value} {stat_key}'
            string_list.append(rendered_string)
        return '\n'.join(string_list)

    def win_bet(self):
        for tile in self.wager_for:
            tile.change_hands(self.better)

    def lose(self):
        for tile in self.wager_with:
            tile.change_hands(self.betee)
