from heat_map.heatmap import Heatmapper, _asset_file
from PIL import Image

example_points = [(120, 25), (200, 50), (60, 300), (60, 300), (60, 300), (60, 300), (60, 300), (170, 250)]
example_img = Image.open(_asset_file("area.png"))

heatmapper = Heatmapper(colours="default")
heatmapper.heatmap_on_img(example_points, example_img).save("out.png")
