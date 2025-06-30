from die import Die
import plotly.express as px


d = Die(1_000_000, 2, 6)
d.toss()
frequancies = []


poss_results = range(1, d.number_of_size * d.dies + 1)


for x in poss_results:
    frequancies.append(d.outcomes.count(x))
    
print(frequancies)

title = "Result form die on d6 1,000,000 times"
labels = {'x':'result', 'y':'frequancy'}
fig = px.bar(x=poss_results, y=frequancies, title=title, labels=labels)
fig.show()
