import random


def create_table(odays, operiods, osubjects):
    subjects = []
    periods = []
    days = []
    for i, val in enumerate(odays):
        days.append(val)
    for i, val in enumerate(operiods):
        periods.append(val)
    for i, val in enumerate(osubjects):
        subjects.append(val)
    sub = subjects
    time_table = []
    period = ''
    subj = ''

    for i, val in enumerate(days):
        random.shuffle(sub)
        day = {'name': val['name']}
        for ppi, pval in enumerate(periods):
            if ppi == 5 and i % 2 == 0:
                period = pval['name']
                subj = 'Play'
            elif ppi == 4 and i % 2 == 1:
                period = pval['name']
                subj = 'Library'
            elif ppi == 5:
                period = pval['name']
                subj = sub[ppi - 1]['name']
            else:
                period = pval['name']
                subj = sub[ppi]['name']
            day[period] = subj
        time_table.append(day)
    return time_table