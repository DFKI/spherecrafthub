
import argparse
import cv2
import numpy as np
import os

from keypoint_utils import spherical_to_sphere_map_coords, build_image_name, get_scene_name, load_keypoint_coords

#=======================================================================================================================

def load_keypoints_matches(keypoint_matches_file:str) -> tuple:
    with np.load(keypoint_matches_file, allow_pickle=True) as keypoint_matches:
        kpts_corres = keypoint_matches['correspondences']
        scores = keypoint_matches['scores']
    return (kpts_corres, scores)

#-----------------------------------------------------------------------------------------------------------------------

def get_color(score:float) -> tuple:
    fake_input = np.zeros(shape=(1, 1, 1), dtype=np.uint8)
    if score < 0.:
        fake_input[0][0] = 0
    elif score > 1.:
        fake_input[0][0] = 255
    else:
        fake_input[0][0] = score * 255

    output = cv2.applyColorMap(fake_input, cv2.COLORMAP_JET)
    return (int(output[0][0][0]), int(output[0][0][1]), int(output[0][0][2]))

#-----------------------------------------------------------------------------------------------------------------------

def draw_keypoint_matches(keypoint_corres:list,
                          corres_scores:list,
                          ref_image:np.array,
                          tar_image:np.array,
                          ref_keypoints:np.array,
                          tar_keypoints:np.array,
                          min_score:float,
                          max_score:float,
                          line_thickness:int) -> np.array:
    corres_size = len(keypoint_corres)
    img_width = ref_image.shape[1]
    img_height = tar_image.shape[0]

    assert corres_size * 2 == len(ref_keypoints), 'Number of correspondences does not match number of reference \
                                                   keypoints.'
    assert img_width == tar_image.shape[1], 'Unable to draw keypoint correspondences: widths of reference and target \
                                             images do not match.'

    draw_image = cv2.vconcat([ref_image, tar_image])
    if min_score < 0.:
        min_score = 0.
    if max_score > 1.:
        max_score = 1.
    assert min_score < 1., "Invalid minimum score."
    assert max_score > 0., "Invalid maximum score."
    assert min_score < max_score, "Minimum score must be smaller than the maximum score."

    for i in range(corres_size):
        score = corres_scores[i]
        if (keypoint_corres[i] < 0) or (score < min_score) or (score > max_score):
            continue

        x_ref, y_ref = spherical_to_sphere_map_coords(ref_keypoints[i * 2],
                                                      ref_keypoints[i * 2 + 1],
                                                      img_width,
                                                      img_height)
        x_tar, y_tar = spherical_to_sphere_map_coords(tar_keypoints[keypoint_corres[i] * 2],
                                                      tar_keypoints[keypoint_corres[i] * 2 + 1],
                                                      img_width,
                                                      img_height)
        if x_ref < 0.:
            x_ref = 0.
        if y_ref < 0.:
            y_ref = 0.
        if x_tar < 0.:
            x_tar = 0.
        if y_tar < 0.:
            y_tar = img_height
        else:
            y_tar = y_tar + img_height

        draw_image = cv2.line(draw_image,
                              (int(x_ref), int(y_ref)),
                              (int(x_tar), int(y_tar)),
                              get_color(score),
                              line_thickness)
    return draw_image

#-----------------------------------------------------------------------------------------------------------------------

def run(args) -> None:
    scene_dir = args.scene_dir
    keypoints_dir = os.path.join(scene_dir, args.keypoints_dir)
    keypoint_matches_dir = os.path.join(scene_dir, args.keypoint_matches_dir)
    images_dir = os.path.join(scene_dir, args.images_dir)
    output_dir = os.path.join(scene_dir, args.output_dir)
    ref_id = args.reference_view_id
    tar_id = args.target_view_id
    line_thickness = args.line_thickness
    scene = get_scene_name(scene_dir)
    assert os.path.exists(scene_dir), 'Directory {} does not exist.'.format(scene_dir)
    assert os.path.exists(keypoints_dir), 'Directory {} does not exist.'.format(keypoints_dir)
    assert os.path.exists(keypoint_matches_dir), 'Directory {} does not exist.'.format(keypoint_matches_dir)
    assert os.path.exists(images_dir), 'Directory {} does not exist.'.format(images_dir)
    assert ref_id >= 0, 'Reference view id should be bigger than 0.'
    assert tar_id > ref_id, 'Target view id should be bigger than reference view id.'
    assert line_thickness > 0, 'Line thickness should be positive integer.'
    os.makedirs(output_dir, exist_ok=True)

    ref_base_name = build_image_name(ref_id)
    tar_base_name = build_image_name(tar_id)
    kpts_corres, scores = load_keypoints_matches(os.path.join(keypoint_matches_dir,
                                                              ref_base_name + '_' + tar_base_name + '.npz'))

    ref_image = cv2.imread(os.path.join(images_dir, ref_base_name + '.jpg'))
    tar_image = cv2.imread(os.path.join(images_dir, tar_base_name + '.jpg'))
    ref_kpt_coords = load_keypoint_coords(os.path.join(keypoints_dir, scene + '_img_' + ref_base_name + '.npz'))
    tar_kpt_coords = load_keypoint_coords(os.path.join(keypoints_dir, scene + '_img_' + tar_base_name + '.npz'))
    out_image = draw_keypoint_matches(kpts_corres,
                                      scores,
                                      ref_image,
                                      tar_image,
                                      ref_kpt_coords,
                                      tar_kpt_coords,
                                      args.min_score,
                                      args.max_score,
                                      line_thickness)
    cv2.imwrite(os.path.join(output_dir, ref_base_name + '_' + tar_base_name + '.jpg'), out_image)

#=======================================================================================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draws spherical keypoint matches.')
    parser.add_argument('-s', '--scene_dir',
                        required=True,
                        type=str,
                        help='The scene directory.')
    parser.add_argument('-k', '--keypoints_dir',
                        required=True,
                        type=str,
                        help='Directory relatvie to scene_dir containing the keypoints. Files are expected to be .npz')
    parser.add_argument('-m', '--keypoint_matches_dir',
                        required=True,
                        type=str,
                        help='Directory relative to scene_dir containing keypoint matches. Files are expected to be \
                              .npz')
    parser.add_argument('-i', '--images_dir',
                        required=False,
                        type=str,
                        default='images',
                        help='Directory relative to scene_dir containing the equirectangular images. Images are \
                              expected to be .jpg')
    parser.add_argument('-o', '--output_dir',
                        required=True,
                        type=str,
                        help='Output directory, relative to scene_dir, to store images after drawing keypoint matches.')
    parser.add_argument('-r', '--reference_view_id',
                        required=True,
                        type=int,
                        help='Identifier of the reference view.')
    parser.add_argument('-t', '--target_view_id',
                        required=True,
                        type=int,
                        help='Identifier of the target view.')
    parser.add_argument('--min_score',
                        required=False,
                        type=float,
                        default=0.,
                        help='Minimum score value to draw, in the range [0, 1). Must be smaller than the maximum \
                              score.')
    parser.add_argument('--max_score',
                        required=False,
                        type=float,
                        default=1.,
                        help='Maximum score value to draw, in the range (0, 1]. Must be larger than the minimum \
                              score.')
    parser.add_argument('-l', '--line_thickness',
                        required=False,
                        type=int,
                        default=2,
                        help='Line thickness to draw keypoint matches on the images. Default value is 2.')

    run(parser.parse_args())
