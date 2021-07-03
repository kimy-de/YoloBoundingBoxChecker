# YoloBoundingBoxChecker

To check given bounding boxes visually, this code creates the result images that mark bounding boxes stored by the Yolo format.

### 1. Annotation format
```
[class x_center y_center width height]
```
Box coordinates must be in normalized xywh format (from 0 - 1). 
[[Tutorial Link]](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)


- Example
```
0 0.651343 0.672414 0.259298 0.379310
0 0.500000 0.667385 0.165289 0.446839
0 0.479339 0.443966 0.163223 0.255747
0 0.380165 0.623563 0.212810 0.502874
0 0.260847 0.603448 0.186983 0.491379
1 0.193182 0.166667 0.055785 0.086207
1 0.351240 0.058908 0.045455 0.083333
```

### 2. Directory
Each label file should have the same file name as the image file corresponding to it.
```
- folder
  - classes.txt # list of classes
  - images # image folder containing images
    - 001.jpg ...
  - labels # label folder containing annotation corresponding to each image file
    - 001.txt ...
  - results # folder that stores result images
    - ...
```
### 3. classes.txt
```
person
bird
cat
dog
.
.
.
```

