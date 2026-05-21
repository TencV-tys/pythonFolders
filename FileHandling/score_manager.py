import csv

def save_score(name,score):
    with open('scores.txt','w') as f:
        f.write(f'{name}, {score}\n')

def load_score():
    score = []
    with open('scores.txt','r') as f:
        for line in f:
            line = line.strip()
            if line:
                name, score = line.split('')
                scores.append((name,int(score)))
    return scores

def calculate_average():
    if not scores:
        return 0
    total = sum(score for name, score in scores)
    return total /len(scores)

def get_top_student():
    if not scores:
        return (None,0)
    return max(scores, key = lambda x: x[1])

def save_to_csv():
    scores = load_score()
    with open('scores.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name','Score'])
        writer.writerows(scores)