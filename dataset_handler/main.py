from file_utils import *


def main():
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/'
    merge_background_and_cars_folders(path)
    # now there are 2 folders holding all of the raw and jpg images separately each in a folder named "Sony" with

    # generating  random indices for train test and validation
    num_of_images = 300
    test_size = 60
    validation_size = 30
    train_list_cars, test_list_cars, validation_list_cars = get_train_test_validation_lists(num_of_images,
                                                                                            validation_size, test_size)
    train_list_back, test_list_back, validation_list_back = get_train_test_validation_lists(num_of_images,
                                                                                            validation_size, test_size)

    # changes the images names such that every image name length is 5
    validation_prefix = 2
    test_prefix = 1
    train_prefix = 0

    # raw
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony/'
    normalize_names(path, train_list_back, train_prefix)
    normalize_names(path, test_list_back, test_prefix)
    normalize_names(path, validation_list_back, validation_prefix)
    normalize_names(path, train_list_cars, train_prefix)
    normalize_names(path, test_list_cars, test_prefix)
    normalize_names(path, validation_list_cars, validation_prefix)

    # jpg
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony/'
    normalize_names(path, train_list_back, train_prefix)
    normalize_names(path, test_list_back, test_prefix)
    normalize_names(path, validation_list_back, validation_prefix)
    normalize_names(path, train_list_cars, train_prefix)
    normalize_names(path, test_list_cars, test_prefix)
    normalize_names(path, validation_list_cars, validation_prefix)
    # now all the images names are normalized to length of 5



    # splitting the images to short/long/not_used folders
    # raw
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony/'
    split_long_short(path)
    # jpg
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony/'
    split_long_short(path)



    # creates a text file that contains the short exposure images and their corresponding long exposure image
    # raw
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony/short'
    # validation
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony_val_list.txt'
    create_txt_file(path, file_name, validation_prefix)
    # train
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony_train_list.txt'
    create_txt_file(path, file_name, train_prefix)
    # test
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/raw_images/Sony_test_list.txt'
    create_txt_file(path, file_name, test_prefix)

    # jpg
    path = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony/short'
    # validation
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony_val_list.txt'
    create_txt_file(path, file_name, validation_prefix)
    # train
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony_train_list.txt'
    create_txt_file(path, file_name, train_prefix)
    # test
    file_name = '/home/shaynaor/Desktop/detection_in_the_dark/dataset/jpg_images/Sony_test_list.txt'
    create_txt_file(path, file_name, test_prefix)


if __name__ == "__main__":
    main()
