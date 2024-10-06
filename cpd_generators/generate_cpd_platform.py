

from random import randrange


HIGH = 'high'
MED = 'med'
LOW = 'low'

LG = 'lg'
SM = 'sm'

FAST = 'fast'
SLOW = 'slow'




def get_proba_dist(alt, size, speed):

    platforms = {
        'missile': {
            'alt': [HIGH, MED, LOW],
            'size': [MED, SM],
            'speed': [FAST, MED],
        },
        'fighter': {
            'alt': [HIGH, MED, LOW],
            'size': [MED, SM],
            'speed': [FAST, MED],
        },
        'bomber': {
            'alt': [HIGH, MED],
            'size': [LG, MED],
            'speed': [MED, SLOW],
        },
        'uav': {
            'alt': [HIGH, MED],
            'size': [MED, SM],
            'speed': [MED, SLOW],
        },
    }

    platform_names = [
        'missile',
        'fighter',
        'bomber',
        'uav',
    ]

    odds = []
    for platform in platform_names:
        # force ordered
        features = platforms[platform]

        p_mass = 0
        if alt in features['alt']:
            feature_mass = 1/(len(features['alt']))
            p_mass += feature_mass

        if size in features['size']:
            feature_mass = 1/(len(features['size']))
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

        

alts = [
    #HIGH,
    #MED,
    LOW
]
sizes = [
    #LG,
    #MED,
    SM
]


for alt in alts:
    for size in sizes:
        for speed in [FAST, MED, SLOW]:

            dist = get_proba_dist(alt, size, speed)

            corr = round(1.0 - sum(dist), 2)

            pad_index = randrange(len(dist))
            dist[pad_index] += corr

            print('-------------', sum(dist))
            for p in dist:
                print(p)
            
            # maually entered from here
