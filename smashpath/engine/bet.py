from . import *
import random
class Bet:
    # Stats that are hard to keep low
    low_stats = { 
                'falls':(0,2), 
                'damage taken':(0,1000), 
                'launch distance':(0, 1000),
                'peak damage':(0,500), 
                'max launch speed':(25,350),
                'final smashes':(1,4),
                'grabs':(0,5),
                'throws':(0,5),
                'longest drought':(2,20),
                'air attacks':(0,20),
                'air time':(20,60),
                'ground attacks':(10, 50),
                'air attacks':(0, 20),
                'smash attacks':(0, 20),
                'items grabbed':(0, 20)
                }

    # Stats that are hard to get higher 
    high_stats = {
                'kos':(1,5),
                'damage given':(100,2000),
                'ground time':(60,300), 
                'max launcher speed':(25,350),
                'hit percentage':(0,90),
                'high stakes games':(1,10),
                'grabs':(5,30),
                'throws':(5,30),
                'longest drought':(5,120),
                'air attacks':(5,50),
                'air time':(20,90),
                'ground attacks':(20, 120),
                'air attacks':(10, 80),
                'smash attacks':(10, 80),
                'items grabbed':(10, 80)
                }
    
    @property
    def win_conditions(self):
        bet1_value = sum([x.value for x in self.bet1])
        bet2_value = sum([x.value for x in self.bet2])
        value_diff = bet2_value - bet1_value
        used_stats = []
        print('value diff', value_diff)
        if bet1_value > bet2_value:
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
    
    def __init__(self, better, betee, bet1, bet2):
        self.better = better
        self.betee = betee
        self.bet1 = bet1
        self.bet2 = bet2
    
    def _generate_win_condition_(self, easy=False):
        highlow = random.choice(['high', 'low'])
        percentage = random.random()
        if easy:
            percentage = .01
        if highlow == 'high':
            stat_key = random.choice(list(self.high_stats.keys()))
            min_value, max_value =self. high_stats[stat_key]
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
    
    def _win_bet_(self):
        for tile in self.bet2:
            tile.change_hands(self.better)
    
    def _lose_bet_(self):
        for tile in self.bet1:
            tile.change_hands(self.betee)
    
    def run(self):
        print(self.render_conditions())
        win_or_lose = input('Did they win?: Y/N')
        if 'y' in win_or_lose.lower():
            self._win_bet_()
        else:
            self._lose_bet_()