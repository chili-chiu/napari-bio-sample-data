# napari-bio-sample-data

[![License](https://img.shields.io/pypi/l/napari-bio-sample-data.svg?color=green)](https://github.com/chili-chiu/napari-bio-sample-data/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-bio-sample-data.svg?color=green)](https://pypi.org/project/napari-bio-sample-data)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-bio-sample-data.svg?color=green)](https://python.org)
[![tests](https://github.com/chili-chiu/napari-bio-sample-data/workflows/tests/badge.svg)](https://github.com/chili-chiu/napari-bio-sample-data/actions)
[![codecov](https://codecov.io/gh/chili-chiu/napari-bio-sample-data/branch/main/graph/badge.svg)](https://codecov.io/gh/chili-chiu/napari-bio-sample-data)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-bio-sample-data)](https://napari-hub.org/plugins/napari-bio-sample-data)

a sample data plugin for bio-related demos

----------------------------------
This plugin contains 5 sample datasets with additional napari layer types:

(1) 3D EM dataset (image + points + vectors)
Image credit: Alister Burt
The [original data](https://github.com/alisterburt/napari-cryo-et-demo) is down-sampled to have smaller file size.

(2) 2D skin RGB dataset (image + shape)
Image credit: skimage.data.skin

(3) 3D nuclei dataset (image + label + surface)
Image credit: skimage.data.cells3d

(4) 2D timelapse dataset (image + points + tracks)
Image credit: [Cell Tracking Challenge](http://celltrackingchallenge.net/2d-datasets/)
The original data is cropped to have smaller file size.

(5) large multi-resolution 3D EM dataset
Image credit: [Janelia Open Organelle](https://openorganelle.janelia.org/datasets/jrc_hela-1) 
This plugin only accesses 2 lower resolution levels.

Datasets (1)-(4) are stored locally. 
Dataset (5) is downloaded and temporarily stored on RAM when accessed.  

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `napari-bio-sample-data` via [pip]:

    pip install napari-bio-sample-data



To install latest development version :

    pip install git+https://github.com/chili-chiu/napari-bio-sample-data.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-bio-sample-data" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/chili-chiu/napari-bio-sample-data/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
