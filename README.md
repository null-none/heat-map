# heatmappy
Generate image heat maps in Python 

## Install

`pip install heat-map`

## Examples

#### Given some points (co-ordinates) and a base image

```python
from heat_map.heatmap import Heatmapper, _asset_file
from PIL import Image

example_points = [(120, 25), (200, 50), (60, 300), (60, 300), (60, 300), (60, 300), (60, 300), (170, 250)]
example_img = Image.open(_asset_file("area.png"))

heatmapper = Heatmapper(colours="default")
heatmapper.heatmap_on_img(example_points, example_img).save("out.png")

```
![area](examples/out.png?raw=true)

## Heatmap config

The following options are available (shown with their default values):

```python
heatmapper = Heatmapper(
    point_diameter=50,  # the size of each point to be drawn
    point_strength=0.2,  # the strength, between 0 and 1, of each point to be drawn
    opacity=0.65,  # the opacity of the heatmap layer
    colours='default',  # 'default' or 'reveal'
                        # OR a matplotlib LinearSegmentedColorMap object 
                        # OR the path to a horizontal scale image
    grey_heatmapper='PIL'  # The object responsible for drawing the points
                           # Pillow used by default, 'PySide' option available if installed
)
```

### Provided colour schemes

#### default

![default colour scheme](/heat_map/assets/default.png?raw=true)

#### reveal

![reveal colour scheme](/heat_map/assets/reveal.png?raw=true)


## License

MIT License.
