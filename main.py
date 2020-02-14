import collections
from pprint import pprint
from functools import reduce
import itertools

Model = collections.namedtuple(
    'Model', ['name', 'year', 'acc', 'sota'], verbose=False)

Equipment = collections.namedtuple(
    'Equipment', ['name', 'price', 'color', 'sold'], verbose=False)

data = (
    Model('AlexNet', 2010, '40%', True),
    Model('VGG', 2011, '52%', False),
    Model('LeNet', 2005, '36%', True),
    Model('ResNet', 2016, '67%', True),
    Model('InceptionV3', 2018, '64%', False),
    Model('EfficientNet', 2019, '72%', True),
)

household = (
    Equipment('Chair', 100, 'Brown', True),
    Equipment('Laptop', 2500, 'Gray', False),
    Equipment('Shoe', 1000, 'Blue', True),
    Equipment('Car', 20000, 'Black', True),
    Equipment('Pan', 50, 'Black', False),
)


def profit():
    return reduce(lambda val, ele: val+ele.price if ele.sold else val, household, 0)


def sort_color():
    return {x[0]: tuple(x[1]) for x in itertools.groupby(household, lambda x: x.color)}


def filter_sota():
    # Learn filter
    return filter(lambda x: x.sota, data)


def filter_year(year):
    # Python recommended way
    return (x for x in data if x.year <= year)


def map_data():
    # Learn map
    return map(lambda x: {'name': x.name, 'Accuracy': x.acc, 'Dataset': 'ImageNet' if x.year > 2010 else 'Mnist'}, data)


def map_data_recommended():
    # Python recommened way
    return ({'name': x.name, 'Accuracy': x.acc, 'Dataset': 'ImageNet' if x.year > 2010 else 'Mnist'} for x in data)


def main():
    print(type(data))
    print(type(data[0]))
    pprint(data)
    print('----------------------------------')
    print(filter_sota())
    pprint(tuple(filter_sota()))
    print('----------------------------------')
    print(filter_year(2016))
    pprint(tuple(filter_year(2017)))
    print('----------------------------------')
    print(map_data())
    pprint(tuple(map_data()))
    print('----------------------------------')
    print(profit())
    print('----------------------------------')
    print(sort_color())


if __name__ == "__main__":
    main()
