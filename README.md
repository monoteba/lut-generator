# LUT Table Texture Generator

Python script for generating neutral LUT tables of different sizes. It supports both Unreal Engine style LUT (top down) and the Unity style LUT (bottom up).

Based on a [GitHub gist](https://gist.github.com/asus4/09b1f5403c63ceab5ae34710cbe2809e) by [Koki Ibukuro](https://gist.github.com/asus4).

## Prerequisites

The script uses *Python 2.7*, *cv2* and *numpy*, which can be installed using *pip*.

```bash
pip install numpy
pip install opencv-python
```

More information about OpenCV-Python can be found here: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

## Usage

The script can generate either a square layout or a long strip layout. Include `--flipy` for Unity style output.

`python lut-generator.py --strip 32 --flipy output.png`

`python lut-generator.py --square 64 output.png`

## Options

`-sq` `--square` use square format - accepted values `16`, `64`, `256`

`-st` `--strip` use strip format - accepted values `16`, `32`, `64`

`-fy` `--flipy` flip the image vertically

## Samples

| Size | Unreal Engine | Unity |
| :--- | --- | --- |
| 256x16 | ![strip 256x16](samples/unreal/lut_strip_16_256x16.png) | ![lut_strip_16_256x16](samples/unity/lut_strip_16_256x16.png) |
| 1024x32 | ![strip 1024x32](samples/unreal/lut_strip_32_1024x32.png) | ![strip 1024x32](samples/unity/lut_strip_32_1024x32.png) |

**Unity Style Layouts:**

- [Strip 256x16](samples/unity/lut_strip_16_256x16.png)
- [Strip 1024x32](samples/unity/lut_strip_32_1024x32.png)
- [Strip 4096x64](samples/unity/lut_strip_64_4096x64.png)
- [Square 64x64](samples/unity/lut_square_16_64x64.png)
- [Square 512x512](samples/unity/lut_square_64_512x512.png)
- [Square 4096x4096](samples/unity/lut_square_256_4096x4096.png)


**Unreal Engine Style Layouts:**

- [Strip 256x16](samples/unreal/lut_strip_16_256x16.png)
- [Strip 1024x32](samples/unreal/lut_strip_32_1024x32.png)
- [Strip 4096x64](samples/unreal/lut_strip_64_4096x64.png)
- [Square 64x64](samples/unreal/lut_square_16_64x64.png)
- [Square 512x512](samples/unreal/lut_square_64_512x512.png)
- [Square 4096x4096](samples/unreal/lut_square_256_4096x4096.png)

## License

This project is licensed under the [MIT License](LICENSE)