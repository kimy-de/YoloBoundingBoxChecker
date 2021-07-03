import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from tqdm import tqdm

def boundingBoxImages():
    label_paths = glob.glob('./labels/*')
    count = 0
    cls = list(np.genfromtxt('./classes.txt', dtype='str'))
    cls_count = [0] * len(cls)

    for label_path in tqdm(label_paths):
        try:
            annotation = np.loadtxt(label_path, delimiter=' ')

            img_path = label_path.replace('txt', 'jpg').replace('labels', 'images')
            img = Image.open(img_path)
            plt.gca().set_axis_off()
            plt.imshow(img)
            img_size = np.array(img).shape

            if isinstance(annotation[0], np.ndarray) == False:
                x_center = img_size[1] * annotation[1]
                y_center = img_size[0] * annotation[2]
                width = img_size[1] * annotation[3]
                height = img_size[0] * annotation[4]
                x = x_center - width/2
                y = y_center - height/2
                plt.gca().add_patch(Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none'))
                plt.text(x, y, cls[int(annotation[0])], bbox={'facecolor': 'white', 'pad': 3})
                cls_count[int(annotation[0])] += 1

            else:
                for bbox in annotation:
                    x_center = img_size[1] * bbox[1]
                    y_center = img_size[0] * bbox[2]
                    width = img_size[1] * bbox[3]
                    height = img_size[0] * bbox[4]
                    x = x_center - width / 2
                    y = y_center - height / 2
                    plt.gca().add_patch(Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none'))
                    plt.text(x, y, cls[int(bbox[0])], bbox={'facecolor': 'white', 'pad': 3})
                    cls_count[int(bbox[0])] += 1
            plt.savefig(img_path.replace('images', 'results').replace('jpg', 'png'), bbox_inches='tight')
            plt.close()
            count += 1

        except:
            print("Error file:", label_path)

    print("Number of objects per class")
    for i in range(len(cls)):
        print(f"{cls[i]}: {cls_count[i]}")
    print(f"Saved {count} Images.")


if __name__ == "__main__":

    boundingBoxImages()
