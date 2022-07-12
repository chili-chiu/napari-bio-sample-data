from __future__ import annotations
import numpy as np
from skimage.io import imread
from napari.utils import io
import fsspec
import zarr
import dask.array as da
import os

dir = os.path.dirname(__file__)
#to do: add metadata

#EM dataset (image + points + vectors)
def tomo_data() -> List[LayerData]:
    img = imread(os.path.join(dir,'./sample_images/tomo.tif'))
    point = np.load(os.path.join(dir,'./sample_images/tomo_point.npy'))
    vector = np.load(os.path.join(dir,'./sample_images/tomo_vector.npy'))
    return [(img, {"name": "tomo", "scale": (4,4,4)}),(point,{"name": "tomo point"}, "points"),(vector,{"name": "tomo vector", "length": 10}, "vectors")]

#2D skin RGB dataset (image + shape)
def skin_data() -> List[LayerData]:
    img = imread(os.path.join(dir,'./sample_images/skin.tif'))
    shapes, shape_type, shape = io.csv_to_layer_data(os.path.join(dir,'./sample_images/skin_shape.csv'))
    return [(img, {"name": "skin"}),(shapes, {"shape_type": shape_type['shape_type'], "name": "skin shape", "edge_width": 3, "edge_color": "green"}, "shapes")] 

#3D nuclei dataset (image + label + surface)
#surface layer saved by:
#np.savez('nuclei_surface.npz',*data)
def nuclei_data() -> List[LayerData]:
    img = imread(os.path.join(dir,'./sample_images/nuclei.tif'))
    label = imread(os.path.join(dir,'./sample_images/nuclei_label.tif'))
    surface_read = np.load(os.path.join(dir,'./sample_images/nuclei_surface.npz'))
    surface = tuple(surface_read.values())
    return [(img, {"name": "nuclei"}),(label, {"name": "nuclei label"}, "labels"),(surface, {"name": "nuclei surface"}, "surface")]

#2D timelapse dataset (image + points + tracks)
def timelapse_data() -> List[LayerData]:
    img = imread(os.path.join(dir,'./sample_images/2D_timelapse.tif'))
    point = np.load(os.path.join(dir,'./sample_images/timelapse_point.npy'))
    track = np.load(os.path.join(dir,'./sample_images/timelapse_track.npy'))
    return [(img, {"name": "2D timelapse"}),(point, {"name": "2D timelapse point"}, "points"),(track, {"name": "2D timelapse track"}, "tracks")]

#large multi-resolution EM dataset from janelia
#requires zarr 2.12.0 (2.6.1 doesn't work, missing N5FSStore) and s3fs
def large_data() -> List[LayerData]:
    group = zarr.open(zarr.N5FSStore('s3://janelia-cosem-datasets/jrc_hela-2/jrc_hela-2.n5', anon=True)) # access the root of the n5 container
    
    zdata = group['em/fibsem-uint16/s2'] # s0 is the the full-resolution data, use s2
    
    # create a 2-level resolution image using s2 and s3
    ddata = [
            da.from_zarr(group[f'em/fibsem-uint16/s{i}'], chunks=zdata.chunks)
            for i in range(2, 4)
    ]
    return [(ddata, {"name": "multi-res","multiscale": True, "contrast_limits": (25000, 35000)})]
