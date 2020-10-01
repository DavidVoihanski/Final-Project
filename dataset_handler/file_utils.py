import os
import glob
import random

USE_CAR = 0
USE_BACKGROUND = 1


def get_train_test_validation_lists(num_of_images: int, validation_size: int, test_size: int) -> (list, list, list):
    """
    generate random unique indices for train test validation split
    :param num_of_images: the total number of images
    :param validation_size: number of images for validation
    :param test_size: number of images for test
    :return: (train_list, test_list, validation_list)- indices lists
    """
    indices = [i for i in range(num_of_images)]
    validation_list = random.sample(indices, validation_size)

    for x in validation_list:
        indices.remove(x)

    test_list = random.sample(indices, test_size)

    for x in test_list:
        indices.remove(x)

    return indices, test_list, validation_list


def normalize_names(path: str, image_index_list: list, prefix: int):
    """
    changes the images names such that every image name length is 5
    :param prefix:
    :param image_index_list:
    :param path: directory path
    """

    for index in image_index_list:
        image_path_list = glob.glob('{}*_{}_*'.format(path, index))
        for image_path in image_path_list:
            image_name = image_path.split('/')[-1]
            print(image_name)
            obj_type, img_id, _, exp_num = image_name.split('_')
            img_id_len = len(img_id)
            to_append = str(prefix)
            flag_append = False
            for x in range(5 - img_id_len - 1):
                flag_append = True
                to_append += '0'

            obj_type = obj_type + "_"
            if flag_append:
                new_img_id = obj_type + to_append + img_id
                os.rename(path + image_name, path + new_img_id + "_Exp_" + exp_num)


def split_long_short(path: str):
    """
    split the images:
        all the images that their exposure less than 5 goes to short folder.
        all the images that their exposure is 5 goes to not_used folder.
        all the images that their exposure is 10 goes to long folder.
    :param path: the path for the directory
    """
    long_images = glob.glob("{}/*Exp_10.*".format(path))
    not_used_images = glob.glob("{}/*Exp_5.*".format(path))
    long_path = path + "long"
    short_path = path + 'short'
    not_used_path = path + 'not_used'

    if not os.path.exists(long_path):
        os.makedirs(long_path)

    if not os.path.exists(short_path):
        os.makedirs(short_path)

    if not os.path.exists(not_used_path):
        os.makedirs(not_used_path)

    for long_image in long_images:
        file = long_image.split("/")[-1]
        os.rename(long_image, "{}/{}".format(long_path, file))

    for not_used_image in not_used_images:
        file = not_used_image.split("/")[-1]
        os.rename(not_used_image, "{}/{}".format(not_used_path, file))

    for short_image in os.listdir(path):
        if short_image != 'short' and short_image != 'long' and short_image != 'not_used':
            os.rename(path + short_image, '{}/{}'.format(short_path, short_image))


def create_txt_file(path: str, file_name: str, prefix: int):
    """
    for every short exposure unique image pair the corresponding ground truth image (exposure=10)
    :param prefix: validation_prefix=2 / test_prefix=1 / train_prefix=0
    :param path: path to short exposure directory
    :param file_name: the file name that we create
    """
    prefix_short = './Sony/short/'
    prefix_long = './Sony/long/'
    ISO = 'ISO2000'
    F = 'F5.6'

    files = sorted(glob.glob('{}/*_{}*_Exp_*'.format(path, prefix)))
    with open(file_name, 'w') as f:
        for file in files:
            file = file.split('/')[-1]
            obj_type, index, _, exp_num = file.split('_')
            file_long = obj_type + '_' + index + '_Exp_' + '10.ARW'
            f.write('{}{} {}{} {} {}\n'.format(prefix_short, file, prefix_long, file_long, ISO, F))


def rename_label_files(path: str):
    """
    rename files name that contain the label according to the image index.
    :param path: directory path
    """
    files = os.listdir(path)
    for file in files:
        index = file.split('_')[0]
        os.rename('{}{}'.format(path, file), '{}{}.txt'.format(path, index))


def rename_label_paths_file(file_name: str):
    """
    rename the images path in the file.
    :param file_name: path to the file that contain all the image paths.
    """
    images_path_list = []
    with open(file_name) as f:
        content = f.readlines()
        for line in content:
            img_name = line.split('/')[-1]
            img_index = img_name.split('_')[0]
            images_path_list.append('data/obj_train_data/{}.JPG\n'.format(img_index))

    os.remove(file_name)

    with open(file_name, 'x') as f:
        f.writelines(images_path_list)


def merge_background_and_cars_folders(path: str):
    """
    splits all of the raw and jpg images to separate folders in a folder named "Sony" with.
    :param path: the path to the dataset
    """
    path_to_cars_raw = path + 'cars_raw/'
    path_to_cars_jpg = path + 'cars_jpg/'
    path_to_background_raw = path + 'background_raw/'
    path_to_background_jpg = path + 'background_jpg/'
    dst_path_raw = path + 'raw_images/Sony/'
    dst_path_jpg = path + 'jpg_images/Sony/'

    if not os.path.exists(dst_path_raw):
        os.makedirs(dst_path_raw)

    if not os.path.exists(dst_path_jpg):
        os.makedirs(dst_path_jpg)

    for file in os.listdir(path_to_cars_raw):
        os.rename(path_to_cars_raw + file, dst_path_raw + file)

    for file in os.listdir(path_to_background_raw):
        os.rename(path_to_background_raw + file, dst_path_raw + file)

    for file in os.listdir(path_to_cars_jpg):
        os.rename(path_to_cars_jpg + file, dst_path_jpg + file)

    for file in os.listdir(path_to_background_jpg):
        os.rename(path_to_background_jpg + file, dst_path_jpg + file)
