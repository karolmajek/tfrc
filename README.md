# Tensorflow Research Cloud

Tensorflow Research Cloud granted me 100+5 TPUs for 30 days. I am using TPUs to train deep neural networks for Object Detection task.

[More about TFRC](https://www.tensorflow.org/tfrc/)

# TPU Models


| Model name  | Speed (ms, TITAN X) | [COCO mAP](http://cocodataset.org/#detection-eval) | FLIR ADAS | Open Images V4 | ERL2018 |
| ------------ | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| [ssd_mobilenet_v1_0.75_depth_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_0.75_depth_300x300_coco14_sync_2018_07_03.tar.gz) | 26 | 18 | | | |
| [ssd_mobilenet_v1_quantized_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_quantized_300x300_coco14_sync_2018_07_18.tar.gz) | 29 | 18 | | | |
| [ssd_mobilenet_v1_0.75_depth_quantized_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_0.75_depth_quantized_300x300_coco14_sync_2018_07_18.tar.gz) | 29 | 16 | | | |
| [ssd_mobilenet_v1_ppn_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_ppn_shared_box_predictor_300x300_coco14_sync_2018_07_03.tar.gz) | 26 | 20 | | | |
| [ssd_mobilenet_v1_fpn_coco](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03.tar.gz) | 56 | 32 | | | |
| [ssd_resnet_50_fpn_coco](http://download.tensorflow.org/models/object_detection/ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03.tar.gz) | 76 | 35 | | | |

## Download COCO checkpoints

With this script you can download all models from the table above and upload them into your storage bucket.
