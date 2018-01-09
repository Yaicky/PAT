# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys
cur, count, all = 0, 0, 0
ranks = {}
groups = {}
lists = []
stu = {}

for line in sys.stdin:
    if count != 0:
        n = line.strip().split()
        stu[n[0]] = int(n[1])
        groups[n[0]] = cur+1
        count -= 1
        if count == 0:
            lists.append(stu)
            cur += 1
            stu = {}
    elif cur != all:
        count = int(line)
    elif cur == 0:
        all = int(line)


    if cur == all:
        # print(lists)
        rlt = {}
        for l in lists:
            l = sorted(l.items(), key=lambda x:(x[1]), reverse=True)
            inc, prerank, presocre = 1, 1, 0
            for i in l:
                if inc == 1:
                    presocre = i[1]
                    ranks[i[0]] = 1
                else:
                    if i[1] != presocre:
                        presocre = i[1]
                        prerank = inc
                        ranks[i[0]] = inc
                    else:
                        ranks[i[0]] = prerank
                inc += 1
            rlt.update(l)
        rlt = sorted(rlt.items(), key=lambda x:(-x[1], int(x[0])))
        all_rank, i, presocre, prerank = [], 1, 0, 1
        for r in rlt:
            if i == 1:
                presocre = r[1]
                all_rank.append(i)
            else:
                if r[1] != presocre:
                    presocre = r[1]
                    prerank = i
                    all_rank.append(i)
                else:
                    all_rank.append(prerank)
            i += 1
        print(len(rlt))
        # print(all_rank)
        i = 0
        for r in rlt:
            print("%s %d %d %d" % (r[0], all_rank[i], groups[r[0]], ranks[r[0]]))
            i += 1





'''
2
5
1234567890001 95
1234567890005 100
1234567890003 95
1234567890002 77
1234567890004 85
4
1234567890013 65
1234567890011 25
1234567890014 100
1234567890012 85

1
5
1234567890001 95
1234567890005 100
1234567890003 95
1234567890002 77
1234567890004 85
'''