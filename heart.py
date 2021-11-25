from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

import folium

m = folium.Map(location=[5.398214,-3.9708682], zoom_start=16)

m.save("index.html")