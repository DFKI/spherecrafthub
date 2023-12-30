# SphereCraft: A Dataset for Spherical Keypoint Detection, Matching and Camera Pose Estimation

![Eye candy](images/eyeCandy.jpg)

We introduce SphereCraft, a dataset specifically designed for spherical keypoint detection, matching, and camera pose estimation. It addresses the limitations of existing datasets by providing extracted keypoints from popular handcrafted and learn-based detectors, along with their ground-truth correspondences. Synthetic scenes with photo-realistic rendering and accurate depth maps and 3D meshes are included, as well as real-world scenes acquired from different spherical cameras. SphereCraft enables the development and evaluation of algorithms and models targeting multiple camera viewpoints, aiming to advance the state-of-the-art in computer vision tasks involving spherical images.

## Synthetic Scenes
<a name="SyntheticScenes"></a>

Our dataset comprises 21 synthetic scenes of different types, sizes, and complexity. We generate indoor and outdoor synthetic scenes with high-resolution RGB spherical images along with their depth maps and ground truth camera poses. A selection of popular handcrafted and learned keypoints (namely Sift, Akaze, [Superpoint](https://arxiv.org/abs/1712.07629), [KP2D](https://github.com/TRI-ML/KP2D)) is then extracted from each image and accurate ground truth keypoint correspondences are established. A highly accurate 3D mesh from each synthetic scene is also included. The resulting data (RGB images, depth maps, camera poses, 3D meshes, keypoints and their correspondences) allows future approaches to be trained and evaluated on exactly the same data. Images and depth maps were rendered with [Blender](https://www.blender.org/) at 2048x1024 pixels. To see a sample image from each scene, please visit SphereCraft's [webpage](https://dfki.github.io/spherecraftweb/).

Table [1](#T1) summarizes the scene type (I = indoor, O = outdoor, M = mixed), the number of images N, the number of image pairs, the size in GiB and our suggestion for train/test.

<span id="T1"></span>

|Scene|Type|N|Num. Pairs|Size (GiB)|Train/Test|
| :--- | :---: | ---: | ---: | ---: | :---: |
|bank|I|930|91,037|21.7|Train|
|barbershop|I|80|2652|2|Train|
|berlin|I|280|28,608|6.6|Train|
|classroom|I|370|57,073|10|Train|
|garage|M|1090|31,702|28|Train|
|harmony|I|380|54,577|8.9|Test|
|italianFlat|I|270|25,486|5.7|Train|
|kartu|I|640|65,687|18.2|Train|
|loneMonk|M|670|25,571|16.3|Train|
|medievalPort|O|2160|111,151|49.6|Train|
|middleEast|M|4300|211,750|89.2|Test|
|passion|I|600|56,545|14|Train|
|rainbow|I|930|47,755|20.4|Train|
|seoul|I|330|17,414|6.5|Train|
|shapespark|I|860|184,764|23.3|Test|
|showroom|I|1340|134,701|35|Test|
|simple|I|310|29,886|8.2|Train|
|tokyo|I|90|3976|2.2|Test|
|urbanCanyon|O|4090|870,718|294|Train|
|vitoria|I|550|54,292|15.3|Train|
|warehouse|I|900|48,595|30.6|Train|
|**TOTAL**|-|**21,170**|**2,153,940**|**705.7**|-|

Table 1: Synthetic scenes.  More details can be found in the paper.

## Real Scenes

Along with the synthetic scenes, we release a set of 9 real scenes: 4 indoors and 5 outdoors.
Images were acquired with [Civetta](https://weiss-ag.com/de/) and [Ricoh](https://www.ricoh360.com/theta/) Theta-S cameras and offer higher resolutions than the synthetic images. Images captured with Civetta are 7070x3535 pixels, whereas those acquired with Theta-S are 5376x2688 pixels. Unlike synthetic scenes, here ground truth depth maps, camera poses and keypoint correspondences are not available, but we provide the same keypoints extracted for synthetic images. Due to the lack of ground truth information, real scenes are reserved for testing. To see a sample image from each scene, please visit SphereCraft's [webpage](https://dfki.github.io/spherecraftweb/).

Table [2](#T2) summarizes the scene type, the number of cameras N, the size in GiB, and the camera used to capture the scene.

<span id="T2"></span>

|Scene|Type|N|Size (GiB)|Camera|
| :--- | :---: | ---: | ---: | :---: |
|berlinStreet|O|186|13|Civetta|
|church|I|54|2.4|Civetta|
|corridors|I|116|1.8|Theta-S|
|meetingRoom1|I|18|0.25|Theta-S|
|meetingRoom2|I|21|0.38|Theta-S|
|stadium|O|74|4.4|Civetta|
|townSquare|O|35|3.8|Civetta|
|trainStation|O|112|7.2|Civetta|
|uni|O|71|5.4|Civetta|
|**TOTAL**|-|**687**|**38.63**|-|

Table 2: Real scenes.  More details can be found in the paper.

## Download SphereCraft

Even though it is possible to donwload our dataset directly from the [Zenodo](https://zenodo.org/) web interface, this is generally not recommended due to the large size and number of files. Additionally, large scenes are spread over multiple Zenodo records, as shown in Table [3](#T3) below. Hence we provide a script to automate the download process.

<span id="T3"></span>

|Zenodo Record|Files|
| :---: |------|
|1|bank.tar.zst.aa, garage.tar.zst.aa, garage.tar.zst.ab, loneMonk.tar.zst.aa, medievalPort.tar.zst.aa|
|2|medievalPort.tar.zst.ab, medievalPort.tar.zst.ac, middleEast.tar.zst.aa, middleEast.tar.zst.ab, middleEast.tar.zst.ac|
|3|middleEast.tar.zst.ad, middleEast.tar.zst.ae, middleEast.tar.zst.af, rainbow.tar.zst.aa, shapespark.tar.zst.aa|
|4|showroom.tar.zst.aa, showroom.tar.zst.ab, urbanCanyon.tar.zst.aa, urbanCanyon.tar.zst.ab, urbanCanyon.tar.zst.ac|
|5|urbanCanyon.tar.zst.ad, urbanCanyon.tar.zst.ae, urbanCanyon.tar.zst.af, urbanCanyon.tar.zst.ag, urbanCanyon.tar.zst.ah|
|6|urbanCanyon.tar.zst.ai, warehouse.tar.zst.aa, warehouse.tar.zst.ab, berlinStreet.tar.zst.aa, kartu.tar.zst.aa|
|7|vitoria.tar.zst.aa, passion.tar.zst.aa, middleEast.tar.zst.ag, classroom.tar.zst.aa, trainStation.tar.zst.aa, simple.tar.zst.aa, harmony.tar.zst.aa|
|8|medievalPort.tar.zst.ad, bank.tar.zst.ab, uni.tar.zst.aa, seoul.tar.zst.aa, berlin.tar.zst.aa, italianFlat.tar.zst.aa, shapespark.tar.zst.ab, stadium.tar.zst.aa, townSquare.tar.zst.aa, loneMonk.tar.zst.ab, rainbow.tar.zst.ab, church.tar.zst.aa, tokyo.tar.zst.aa|
|9|garage.tar.zst.ac, barbershop.tar.zst.aa, showroom.tar.zst.ac, corridors.tar.zst.aa, warehouse.tar.zst.ac, berlinStreet.tar.zst.ab, meetingRoom2.tar.zst.aa, urbanCanyon.tar.zst.aj, meetingRoom1.tar.zst.aa|

Table 3: Distribution of scene files across Zenodo records.

The script works on Linux and has the following dependencies:
- Python3.7+
- [requests](https://pypi.org/project/requests/) package (```python -m pip install requests```)
- [tar](https://man7.org/linux/man-pages/man1/tar.1.html) and [zstd](https://sourceforge.net/projects/zstandard.mirror/) for decompression

**<ins>Option 1:</ins>** Download and decompress specific scenes.
This is the recommended option.
Beware that scenes have different sizes and thus different disk space requirements. Ideally, for each scene there should be twice as much free disk space as the scene sizes shown in Tables [1](#T1) and [2](#T2) above. This comfortably accommodates compressed and decompressed files.

To download a list of SphereCraft scenes to a directory of your choice, say ```/local/path/to/sphereCraft/```, run the following command (make sure you have write access to the destination directory):

```
python3 download_spherecraft.py --dest_dir=/local/path/to/sphereCraft/ --scenes <scene1> <scene2> ...
```

**Note:** The scenes have to be specified exactly like shown in Tables [1](#T1) and [2](#T2). For instance, the script expects ```italianFlat``` instead of ```Italian Flat```.

**<ins>Option 2:</ins>** Download specific scenes but do not decompress them.
This is the alternative to the option above if disk space is an issue.
To only download the scenes, run:
```
python3 download_spherecraft.py --dest_dir=/local/path/to/sphereCraft/ --scenes <scene1> <scene2> ... --download_only
```

Then, once enough free disk space is available, a scene can be manually decompressed with:

```
cat <scene_name>.tar.zst.* | tar -I zstd -xf -
```
**<ins>Option 3:</ins>** Download and decompress the entire dataset.
Warning! This requires significant amount of free disk space, see Tables [1](#T1) and [2](#T2).
This might be the best option for those with enough free disk space (at least 1.2TiB) and wish to download SphereCraft over the weekend (roughly 400GB of data to download).
```
python3 download_spherecraft.py --dest_dir=/local/path/to/sphereCraft/
```

Again, this will automatically decompress each scene after download is finished, so if you choose this option beware of the required free disk space.
Of course, you may also call it with the ```--download_only``` flag and decompress each scene manually later.

## Data Organization

Each synthetic scene is organized in directories and files as follows:
- ```blender```: directory containing the Blender project. [Anchor](#rendering) cameras are embedded. Generation of [satellite](#rendering) cameras is controlled by the configuration files.
- ```config```: directory containing one or more configuration files. Each file specifies the parameters used for rendering the scenes with [Blender](https://www.blender.org/), such as resolution, number of satellite cameras per anchor camera, whether to render depth maps, range of rotations around each axis, etc. See [Configuration Files](#configuration-files) for details.
- ```depthmaps```: directory containing the depth maps stored as 32-bit float, single-channel, ```exr``` files. We use lossless compression for maximum accuracy. Values represent the distance between the corresponding 3D point and the center of the spherical camera.
- ```extr```: directory containing the camera poses (or extrinsics) as ```dat``` files. Each file contains the rotation matrix **R** stored as a 3 x 3 matrix that, following convention, encodes the transformation from world to camera coordinate system. However, here the vector **t** *does not follow convention* and represents the camera position in world coordinate system. This is convenient to compute distances between cameras and determine neighborhood.
- ```images```: directory containing the images as ```jpg``` files.
- ```keypoints```: directory containing a sub-directory named after each keypoint detector used in our paper (```akaze```, ```kp2d``` and so on). Files are stored as ```npz``` and follow the same convention regardless of the keypoint detector used to produce it. Each ```npz``` is composed of three ```npy``` files: the first, ```keypointCoords.npy```, contains the location of each keypoint on the unit sphere using (&phi;, &theta;) coordinates, with &phi; the polar (or zenith) angle and &theta; the azimuthal angle. We follow [this](https://mathworld.wolfram.com/SphericalCoordinates.html) convention. This representation is simultaneously compact and independent of the resolution of the images. It also allows keypoints detected on images of different resolutions to be transparently integrated into training or testing of neural networks. The second file, ```keypointDescriptors.npy```, stores all keypoint descriptors. Finally, ```keypointScores.npy``` stores all keypoint scores, i.e. their strength or response.
- ```gt_correspondences```: like ```keypoints```, it is subdivided into directories containing ```npz``` files for each separate keypoint detector. Each file contains two embedded ```npy``` files: The first, ```correspondences.npy```, stores the index of the ground-truth keypoint correspondence in the second image for each keypoint in the first image, or -1 if no correspondence is found. The second file, ```scores.npy```, informs the confidence on the ground-truth correspondence as a number in the range [0, 1], computed based on the similarity between the descriptors of the matched keypoints. This confidence, or score, reflects how "important" a keypoint match is and can be used to train and evaluate learn-based keypoint matchers.
- ```mesh```: directory storing the ```obj``` file representing the 3D mesh.
- ```[keypoint detector]_train.txt```, ```[keypoint detector]_val.txt``` and ```[keypoint detector]_test.txt```: list of proposed training, validation, and test image pairs for each keypoint detector used in our paper, eg ```sift_train.txt```. Exclusive to synthetic scenes.
- ```[scene name]_black_list.txt```: a collection of images to be excluded from training, evaluation and testing. The reason is as follows. As satellite cameras are randomly generated, sometimes the resulting location is physically unrealistic, like under the floor or "inside" a piece of furniture (like a couch) nearby the anchor camera, yielding meaningless or defective images. To exclude these images from training, evaluation and testing, after rendering, all images are inspected by a human. When such an image is identified, it is added to this file which is later used to discard these images when creating the ```*_train.txt```, ```*_val.txt``` and ```*_test.txt``` files above.
- ```[scene name]_imperfect.txt```: similar to the black list above, but in contrast here the images are still useful for training, validation and testing even though they display some rendering imperfections.

Real scenes are reserved for testing and contain only a subset of the directories specified above, namely ```images``` and ```keypoints```. We intentionally omit the ```*_test.txt``` files to motivate the prediction of keypoint correspondences for all possible image pairs.

## Rendering

Rendering is based on the concept of **anchor** and **satellite** cameras.
Anchor cameras are those we manually distributed throughout a scene to homogeneously cover it. They are embedded in the Blender projects. Hence, to add or remove anchor cameras as well as to change their position in the scene it is required to edit the respective Blender project.
Satellite cameras are those we randomly generate in the vicinity of each anchor camera. Currently we render 9 satellites for each anchor, yielding clusters of 1 anchor + 9 satellites = 10 images. Satellites are responsible for the large variety of camera poses and strong image distortions. In contrast to anchor cameras, the rendering of satellite cameras is controlled by [configuration files](#configuration-files).

We release rendered images and depth maps at 2048 x 1024 pixels along with each camera's ground truth pose (rotation matrix **R** and translation vector **t**). However, it is possible to render a different version of each scene to satisfy specific requirements such as higher resolution images and/or depth maps, more satellite images, different satellite camera poses, images with more or less distortion, etc.

Scenes were rendered with [Blender](https://www.blender.org/) 3.0 using [NVidia's OptiX ray tracing](https://developer.nvidia.com/rtx/ray-tracing/optix) on RTX NVidia graphics cards (RTX3090, RTX6000 and RXTA600 are known to work). The provided rendering script requires the [bpy](https://pypi.org/project/bpy/) package.

### Configuration Files

The sole input to the rendering script is a configuration file controlling how the satellite images of the target scene will be rendered.
A typical configuration file looks like this:
```json
{
  "Models": [
    {
      "resolution_x": 2048,
      "resolution_y": 1024,
      "samples_per_pixel": 128,
      "file_format": "JPEG",
      "render_images": "yes",
      "render_depth_maps": "yes",
      "start_cam_index": 0,
      "num_anchor_cams": 10,
      "num_sat_cams": 9,
      "camera_type": "P",
      "angle_x_degrees": 45,
      "angle_y_degrees": 45,
      "angle_z_degrees": 180,
      "max_translation": 0.5,
      "random_seed": 19900115,
      "output_path": "/path/to/target/scene/"
    }
  ]
}
```

The relevant parts of each configuration file are as follows.
- ```resolution_x```: the desired width of the equirectangular image, in pixels.
- ```resolution_y```: the desired height of the equirectangular image, in pixels. Must be half of the width specified above. The redundancy is intentional. Moreover, this can be helpful in future versions to render images other than spherical using the same mechanism.
- ```render_images```: flag to enable/disable rendering of RGB images.
- ```render_depth_maps```: flag to enable/disable rendering of depth maps. Disabling the rendering of depth maps saves time and thus is convenient if depth maps are not required.
- ```start_cam_index```: index of the first **anchor** camera to render. Combined with ```num_anchor_cams```, it can be used to split the rendering into several GPUs.
- ```num_anchor_cams```: number of **anchor** cameras to render. For small scenes, this is normally the number of anchor cameras embedded in the Blender project. For large scenes, this can be combined with ```start_cam_index``` to split the rendering into several GPUs.
- ```num_sat_cams```: number of satellite cameras to generate for each anchor. In our paper, this number is 9 so that we form clusters of 10 images (1 anchor + 9 satellites).
- ```camera_type```: ```P``` for panorama. This is what tells Blender to render spherical images.
- ```angle_x_degrees```: a scalar determining the range of possible rotations around the x-axis of the camera, specified in degrees. For instance, 45 means rotations around the x-axis will be selected from [-45&deg;, 45&deg;]. This only affects the generation of satellite cameras. Combined with ```angle_y_degrees``` and ```angle_z_degrees``` it is used to render satellite images with a number of different orientations and produce images with severe distortions.
- ```angle_y_degrees```: like ```angle_x_degrees```, but for the y-axis.
- ```angle_z_degrees```: like ```angle_x_degrees```, but for the z-axis (vertical). While in our paper rotations around x- and y-axes are limited to [-45&deg;, 45&deg;], we allow full rotation around the z-axis, that is rotations are randomly selected from [-180&deg;, 180&deg;].
- ```max_translation```: a scalar, given in meters, specifying the radius of a sphere centered at an anchor camera within which the positions of the satellite cameras will be randomly sampled.
- ```random_seed```: seed used in the pseudo-random generator for the creation of the satellite cameras. Satellite cameras will be rendered at exactly the same poses as long as this seed remains unchanged. This ensures reproducibility but can also be used to create a different set of satellite cameras.

#### Easter Egg

Each configuration file has a different seed. However, the seeds in the files we released are not really random. The seeds in the configuration files (or only the first file when multiple files are present -- as for large scenes) are all related to the same source of inspiration. Glory to the first one who figures it out and explains what they mean! :wink:

## Draw keypoints

It is possible to draw all provided keypoints for any image in SphereCraft. That can be achieved with the ```draw_keypoints.py``` script.

### Examples

Running
```
python3 draw_keypoints.py -s /path/to/scene/vitoria -k keypoints/spherical_superpoint -o visualize_superpoint -v 490
```
will draw Superpoint keypoints stored in `/path/to/scene/vitoria/keypoints/spherical_superpoint` on image number 490 of the Vitoria scene and save the resulting image to `/path/to/scene/vitoria/visualize_superpoint`. The command above yields the following image. Small green dots indicate the keypoint locations.

![Example Superpoint](images/vitoria_00000490_superpoint.jpg)

Likewise, running
```
python3 draw_keypoints.py -s /path/to/scene/barbershop -k keypoints/spherical_sift -o visualize_sift -v 1
```
will draw Sift keypoints on image number 1 of the Barbershop scene and produce the image below.

![Example Sift](images/barbershop_00000001_sift.jpg)

## Draw keypoint correspondences

Similar to drawing keypoints, it is also possible to draw ground truth keypoint correspondences for all keypoints and any image pair, assuming the correspondences exist for the desired image pair (if the images are too far from each other or on opposite sides of a wall there might be no correspondence).

### Examples

Running
```
python3 draw_keypoint_matches.py -s /path/to/scene/italianFlat -k keypoints/spherical_kp2d -m gt_correspondences/kp2d_gt_matches -o visualize_kp2d_matches -r 40 -t 105
```
will draw **all** ground truth KP2D keypoint correspondences between *reference* image number 40 and *target* image number 105 of the Italian Flat scene. The resulting image will be saved to `/path/to/scene/italianFlat/visualize_kp2d_matches` and `keypoints/spherical_kp2d` and `gt_correspondences/kp2d_gt_matches` are the relative paths to KP2D keypoints and ground truth correspondences, respectively.
The command above produces the following image, where the colors indicate the score or confidence of each keypoint correspondence (red = high, blue = low). Scores are in the `[0, 1]` range.

![Example all KP2D correspondences](images/italianFlat_00000040_00000105_kp2d_all_scores.jpg)

To draw correspondences within a given range of scores, simply specify the minimum and maximum desired scores:
```
python3 draw_keypoint_matches.py -s /path/to/scene/italianFlat -k keypoints/spherical_kp2d -m gt_correspondences/kp2d_gt_matches -o visualize_kp2d_matches -r 40 -t 105 --min_score=0.25 --max_score=0.75
```
The command above yields the image below, where only keypoint correspondences with score between 0.25 and 0.75 are displayed.

![Example all KP2D correspondences](images/italianFlat_00000040_00000105_kp2d_min025_max075.jpg)

## Citation

If you use SphereCraft, please cite us:
```bibtex
@InProceedings{Gava_2024_WACV,
    author    = {Gava, Christiano and Cho, Yunmin and Raue, Federico and Palacio, Sebastian and Pagani, Alain and Dengel, Andreas},
    title     = {SphereCraft: A Dataset for Spherical Keypoint Detection, Matching and Camera Pose Estimation},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
    month     = {January},
    year      = {2024},
    pages     = {4408-4417}
}
```
