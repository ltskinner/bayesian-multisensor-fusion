
from random import randrange

import pandas as pd



FAR = 'far'
MED = 'med'
NEAR = 'near'

HIGH = 'high'
LOW = 'low'

FAST = 'fast'
SLOW = 'slow'




missile = {
    'cruise': {
        'range': [FAR, MED],
        'alt': [HIGH],
        'speed': [MED],
    },
    'attack': {
        'range': [MED, NEAR],
        'alt': [MED, LOW],
        'speed': [FAST],
    },
    'evade/neut': {
        'range': [NEAR],
        'alt': [LOW],
        'speed': [SLOW],
    }
}

fighter = {
    'cruise': {
        'range': [FAR, MED],
        'alt': [HIGH, MED],
        'speed': [FAST, MED],
    },
    'attack': {
        'range': [NEAR],
        'alt': [MED, LOW],
        'speed': [MED, SLOW],
    },
    'evade/neut': {
        'range': [NEAR],
        'alt': [LOW, MED, HIGH],
        'speed': [FAST],
    }
}

bomber = {
    'cruise': {
        'range': [FAR, MED],
        'alt': [HIGH, MED],
        'speed': [MED, SLOW],
    },
    'attack': {
        'range': [NEAR],
        'alt': [MED],
        'speed': [MED],
    },
    'evade/neut': {
        'range': [NEAR],
        'alt': [HIGH, LOW],
        'speed': [SLOW],
    }
}

uav = {
    'cruise': {
        'range': [FAR, MED, NEAR],
        'alt': [HIGH, MED],
        'speed': [MED, SLOW],
    },
    'attack': {
        'range': [NEAR],
        'alt': [MED],
        'speed': [SLOW],
    },
    'evade/neut': {
        'range': [NEAR],
        'alt': [LOW],
        'speed': [MED],
    }
}


intents = {
    'cruise': {
        'missile': {
            'range': [FAR, MED],
            'alt': [HIGH],
            'speed': [MED],
        },
        'fighter': {
            'range': [FAR, MED],
            'alt': [HIGH, MED],
            'speed': [FAST, MED],
        },
        'bomber': {
            'range': [FAR, MED],
            'alt': [HIGH, MED],
            'speed': [MED, SLOW],
        },
        'uav': {
            'range': [FAR, MED, NEAR],
            'alt': [HIGH, MED],
            'speed': [MED, SLOW],
        }
    },
    'attack': {
        'missile': {
            'range': [MED, NEAR],
            'alt': [MED, LOW],
            'speed': [FAST],
        },
        'fighter': {
            'range': [NEAR],
            'alt': [MED, LOW],
            'speed': [MED, SLOW],
        },
        'bomber': {
            'range': [NEAR],
            'alt': [MED],
            'speed': [MED],
        },
        'uav': {
            'range': [NEAR],
            'alt': [MED],
            'speed': [SLOW],
        }
    },
    'evade/neut': {
        'missile': {
            'range': [NEAR],
            'alt': [LOW],
            'speed': [SLOW],
        },
        'fighter': {
            'range': [NEAR],
            'alt': [LOW, MED, HIGH],
            'speed': [FAST],
        },
        'bomber': {
            'range': [NEAR],
            'alt': [HIGH, LOW],
            'speed': [SLOW],
        },
        'uav': {
            'range': [NEAR],
            'alt': [LOW],
            'speed': [MED],
        }
    },
}




intents_ordered = [
    'cruise',
    'attack',
    'evade/neut',
]

platforms = [
    'missile',
    'fighter',
    'bomber',
    'uav'
]

ranges = [
    FAR,
    MED,
    NEAR
]

alts = [
    HIGH,
    MED,
    LOW
]

speeds = [
    FAST,
    MED,
    SLOW
]



def get_proba_dist(platform, range, alt, speed):

    odds = []

    for intent in intents_ordered:
        features = intents[intent][platform]

        p_mass = 0
        if range in features['range']:
            feature_mass = 1/(len(features['range']))
            p_mass += feature_mass

        if alt in features['alt']:
            feature_mass = 1/(len(features['alt']))
            p_mass += feature_mass

        if speed in features['speed']:
            feature_mass = 1/(len(features['speed']))
            p_mass += feature_mass

        p_mass = round(p_mass, 2)
        odds.append(p_mass)

    new_odds = []
    for odd in odds:
        new_odd = odd/sum(odds)
        new_odd = round(new_odd, 2)
        new_odds.append(new_odd)

    return new_odds



'''
platform
range
alt
speed

cruise
attack
evade/neut
'''


cols = []

for platform in platforms:
    for range in ranges:
        for alt in alts:
            for speed in speeds:

                dist = get_proba_dist(platform, range, alt, speed)
                corr = round(1.0 - sum(dist), 2)

                pad_index = randrange(len(dist))
                dist[pad_index] += corr

                col = [
                    platform,
                    range,
                    alt,
                    speed,
                    dist[0],
                    dist[1],
                    dist[2],
                ]
                cols.append(col)

                #print('-------------', sum(dist))
                #for p in dist:
                #    print(p)



df = pd.DataFrame(cols)

df.columns = [
    'platform',
    'range',
    'alt',
    'speed',
    'cruise',
    'attack',
    'evade/neut',
]

df.to_csv('./intents.csv', index=False)

