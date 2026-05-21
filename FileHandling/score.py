
def save_scores(scores):
    with open('scores.csv','w') as f:
        f.write('Name,Score\n')
        for n,s in scores:
            f.write(f"{n}, {s} \n")

def load_score():
    load = []
    with open('scores.csv','r') as f:

        for line in f:
            load.append(line.strip().split(','))
    return load

my_scores = [
    ['Vincent', 95],
    ['Maria', 87],
    ['John', 92]
]

save_scores(my_scores)
print('saved')

loaded = load_score()
for load in loaded:
    print(f'{load}')