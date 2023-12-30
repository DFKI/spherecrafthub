
import argparse
import cv2
import numpy as np
import os

from keypoint_utils import spherical_to_sphere_map_coords, build_image_name, get_scene_name, load_keypoint_coords

GREEN = (0, 255, 0)

#=======================================================================================================================

def draw_keypoints(keypoints:np.array, image:np.array, circle_rad:int) -> np.array:
    num_channels = image.shape[2]
    if num_channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    num_kpts = keypoints.shape[0]
    for i in range(0, num_kpts, 2):
        pixel_coords = spherical_to_sphere_map_coords(keypoints[i], keypoints[i + 1], image.shape[1], image.shape[0])
        cv2.circle(image, (int(pixel_coords[0]), int(pixel_coords[1])), circle_rad, GREEN, thickness=-1)

    return image

#-----------------------------------------------------------------------------------------------------------------------

def run(args) -> None:
    scene_dir = args.scene_dir
    keypoints_dir = os.path.join(scene_dir, args.keypoints_dir)
    images_dir = os.path.join(scene_dir, args.images_dir)
    output_dir = os.path.join(scene_dir, args.output_dir)
    view_id = args.view_id
    circle_radius = args.circle_radius
    assert os.path.exists(scene_dir), 'Directory {} does not exist.'.format(scene_dir)
    assert os.path.exists(keypoints_dir), 'Directory {} does not exist.'.format(keypoints_dir)
    assert os.path.exists(images_dir), 'Directory {} does not exist.'.format(images_dir)
    assert view_id >= 0, 'View id should be bigger than 0.'
    assert circle_radius > 0, 'Circle radius should be positive integer.'
    os.makedirs(output_dir, exist_ok=True)

    view_name = build_image_name(view_id)
    scene = get_scene_name(scene_dir)
    kpt_coords = load_keypoint_coords(os.path.join(keypoints_dir, scene + '_img_' + view_name + '.npz'))
    img = cv2.imread(os.path.join(images_dir, view_name + '.jpg'))
    img = draw_keypoints(kpt_coords, img, circle_radius)
    cv2.imwrite(os.path.join(output_dir, view_name + '.jpg'), img)

#=======================================================================================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draws keypoints on the equirectangular image.')
    parser.add_argument('-s', '--scene_dir',
                        required=True,
                        type=str,
                        help='The scene directory.')
    parser.add_argument('-k', '--keypoints_dir',
                        required=True,
                        type=str,
                        help='Directory relative to scene_dir containing the keypoints. Files are expected to be .npz')
    parser.add_argument('-i', '--images_dir',
                        required=False,
                        type=str,
                        default='images',
                        help='Directory relative to scene_dir containing the equirectangular images. Images are \
                              expected to be .jpg')
    parser.add_argument('-o', '--output_dir',
                        required=True,
                        type=str,
                        help='Output directory, relative to scene_dir, to store images after drawing the keypoints.')
    parser.add_argument('-v', '--view_id',
                        required=True,
                        type=int,
                        help='Identifier of the view.')
    parser.add_argument('-c', '--circle_radius',
                        required=False,
                        type=int,
                        default=2,
                        help=f'Circle radius to draw keypoints on the images. Default value is 2.')

    run(parser.parse_args())
