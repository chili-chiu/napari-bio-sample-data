from __future__ import annotations
import numpy as np
from skimage.io import imread
from napari.utils import io
import fsspec
import zarr
import dask.array as da

#to do: add metadata

#EM dataset (image + points + vectors)
def tomo_data() -> List[LayerData]:
    img = imread('./sample_images/tomo.tif')
    point = np.load('./sample_images/tomo_point.npy')
    vector = np.load('./sample_images/tomo_vector.npy')
    return [(img, {"name": "tomo", "scale": (4,4,4)}),(point,{"name": "tomo point"}, "points"),(vector,{"name": "tomo vector", "length": 10}, "vectors")]

#2D skin RGB dataset (image + shape)
def skin_data() -> List[LayerData]:
    img = imread('./sample_images/skin.tif')
    shapes, shape_type, shape = io.csv_to_layer_data('./sample_images/skin_shape.csv')
    return [(img, {"name": "skin"}),(shapes, {"shape_type": shape_type['shape_type'], "name": "skin shape", "edge_width": 3, "edge_color": "green"}, "shapes")] 

#3D nuclei dataset (image + label + surface)
#surface layer saved by:
#np.savez('nuclei_surface.npz',*data)

def nuclei_data() -> List[LayerData]:
    img = imread('./sample_images/nuclei.tif')
    label = imread('./sample_images/nuclei_label.tif')
    surface_read = np.load('./sample_images/nuclei_surface.npz')
    surface = tuple(surface_read.values())
    return [(img, {"name": "nuclei"}),(label, {"name": "nuclei label"}, "labels"),(surface, {"name": "nuclei surface"}, "surface")]

#2D timelapse dataset (image + points + tracks)
def timelapse_data() -> List[LayerData]:
    img = imread('./sample_images/2D_timelapse.tif')
    point = np.load('./sample_images/timelapse_point.npy')
    track = np.load('./sample_images/timelapse_track.npy')
    return [(img, {"name": "2D timelapse"}),(point, {"name": "2D timelapse point"}, "points"),(track, {"name": "2D timelapse track"}, "tracks")]

#large multi-resolution EM dataset from janelia

def large_data() -> List[LayerData]:
    group = zarr.open(zarr.N5FSStore('s3://janelia-cosem-datasets/jrc_hela-2/jrc_hela-2.n5')) # access the root of the n5 container
    zdata = group['em/fibsem-uint16/s4'] # s0 is the the full-resolution data, use s4
    ddata = da.from_array(zdata, chunks=zdata.chunks)
    result = ddata[0].compute()
 
    # ddata = [
    #         da.from_zarr(group[f'em/fibsem-uint16/s{i}'], chunks=zdata.chunks)
    #         for i in range(3, 5)
    # ]
    return [(result, {"name": "multi-res"})]
