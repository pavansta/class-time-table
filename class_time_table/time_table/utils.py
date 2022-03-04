import random


def create_table(odays, operiods, osubjects):
    subjects = []
    periods = []
    days = []
    play = {}
    library = {}
    for i, val in enumerate(odays):
        days.append(val)
    for i, val in enumerate(operiods):
        periods.append(val)
    for i, val in enumerate(osubjects):
        if val['name'] == 'Play':
            play = val
        elif val['name'] == 'Library':
            library = val
        else:
            subjects.append(val)
    sub = subjects
    time_table = []
    table_db = []
    period = ''
    subj = ''

    for i, val in enumerate(days):
        random.shuffle(sub)
        day = {'name': val['name']}
        for ppi, pval in enumerate(periods):
            if ppi == 5 and i % 2 == 0:
                subj = play
            elif ppi == 4 and i % 2 == 1:
                subj = library
            elif ppi == 5 and i % 2 == 1:
                subj = sub[ppi - 1]
            else:
                subj = sub[ppi]
            period = pval['name']
            day[period] = subj['name']
            row = {'department': val['id'], 'day': val['id'], 'period': pval['id'], 'subject': subj['id']}
            table_db.append(row)
        time_table.append(day)
    return { 'display_table': time_table, 'db_table': table_db }