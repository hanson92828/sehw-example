from output import update_pie_chart

data = []

while True:
    thing = input().split(' ')
    price = int(thing[0])
    category = thing[1]
    data.append([price, category])
    update_pie_chart(data)