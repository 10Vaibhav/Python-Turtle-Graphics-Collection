import colorgram

colors = colorgram.extract('damien-hirst-spot-painting-for-sale.jpg', 30)
length = len(colors)
rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tube = (r, g, b)
    rgb_list.append(tube)

print(rgb_list)
