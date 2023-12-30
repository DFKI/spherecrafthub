
import math
import numpy as np
import os

Pi = math.pi
TwoPi = math.pi * 2
PiInverted = 1.0 / Pi
TwoPiInverted = 0.5 / Pi

#=======================================================================================================================

def constrain_spherical_boundaries(phi:float, theta:float) -> tuple:
    while phi < 0:
        phi += TwoPi
    while phi >= TwoPi:
        phi -= TwoPi

    if phi >= Pi:
        phi = TwoPi - phi
        theta += Pi

    while theta < 0:
        theta += TwoPi
    while theta >= TwoPi:
        theta -= TwoPi

    return phi, theta

#-----------------------------------------------------------------------------------------------------------------------

def spherical_to_sphere_map_coords(phi:float, theta:float, imgWidth:float, imgHeight:float) -> tuple:
    # Constrain (locally) phi to be in [0, Pi] and theta in [0, 2Pi)
    phi_bounds, theta_bounds = constrain_spherical_boundaries(phi, theta)

    # Compute image x position
    x = imgWidth * (1.0 - (theta_bounds * TwoPiInverted)) - 0.5
    # Now x is in (-0.5, w - 0.5]

    # Compute image y position
    y = (imgHeight * phi_bounds) * PiInverted - 0.5
    # Now y is in [-0.5, h - 0.5]

    return x, y

#-----------------------------------------------------------------------------------------------------------------------

def get_scene_name(base_dir:str) -> str:
    return os.path.basename(os.path.normpath(base_dir))     # normpath() to remove trailing '/' if present

#-----------------------------------------------------------------------------------------------------------------------

def load_keypoint_coords(keypoints_file:str) -> tuple:
    with np.load(keypoints_file, allow_pickle=True) as keypoint_data:
        kpt_coords = keypoint_data['keypointCoords']    # we only return the coords, so no need to load scores and
    return kpt_coords                                   # descriptors

#-----------------------------------------------------------------------------------------------------------------------

def build_image_name(view_id:int) -> str:
    return '{:08d}'.format(view_id)
