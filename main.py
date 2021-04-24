###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
    rgb_colors.append(rgb)

print(rgb_colors)
