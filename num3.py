class Tomato:
    states = {0: 'nothing',1: 'green',2: 'red'}


    def __init__(self, _index):
        self._index = _index
        self._state = 0

    def glow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(_index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all = ([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant_all()
        print('Gardener finished')

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Gardener is harvesting!')
        else:
            print('dont harvesting')

@staticmethod
    def knowlege_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')

    def __name__ == '__num3__':
        Gardener.knowledge_base()
        great_tomato_bush = TomatoBush(4)
        gardener = Gardener('Emilio', great_tomato_bush)
        gardener.work()
        gardener.work()
        gardener.harvest()
        gardener.work()
        gardener.harvest()












