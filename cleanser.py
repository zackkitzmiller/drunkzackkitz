import csv
with open('/Users/zackkitzmiller/Downloads/tweets.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    good = []
    bad = 0
    for row in spamreader:
        text = row[5]
        if text.startswith('@'):
            bad = bad + 1
            continue
        good.append(text)

print bad
print len(good)

with open('zack_clean.txt', 'a') as tweets_clean:
    for g in good:
        tweets_clean.write('{0}\n'.format(g))
