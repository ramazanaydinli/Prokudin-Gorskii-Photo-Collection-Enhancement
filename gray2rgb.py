import cv2
import os
import numpy as np

desktop_path = os.path.split(os.getcwd())[0]
hw1_data_dir_path = os.path.join(desktop_path, "hw1_data", "data")
#since it takes too long to find optimal shifting ranges, record will be saved as green_x,green_y,red_x,red_y
pixel_shifting = []

def calculate_ssd(img_1, img_2):
    ssd=0
    w,h = img_1.shape
    for width in range(w):
        for height in range(h):
            ssd+= np.square(int(img_1[width][height]) - int(img_2[width][height]))
    return ssd

def min_ssd_calculation(img1, img2):
    nominal_min_ssd = calculate_ssd(img1, img2)
    for x in range(30):
        for y in range(30):
            x_rolled_img2 = np.roll(img2, x-15, axis=1)
            fully_rolled_img2=np.roll(x_rolled_img2, y-15, axis=0)
            ssd_result = calculate_ssd(img1, fully_rolled_img2)
            if ssd_result <= nominal_min_ssd:
                nominal_min_ssd = ssd_result
                best_x = x-15
                best_y = y-15
                print(nominal_min_ssd, best_x, best_y)
    best_x_rolled_img2 = np.roll(img2, best_x, axis=1)
    best_fully_rolled_img2 = np.roll(best_x_rolled_img2, best_y, axis=0)
    return best_fully_rolled_img2, best_x, best_y

for file in os.listdir(hw1_data_dir_path):
    file_path = os.path.join(hw1_data_dir_path, file)
    img = cv2.imread(file_path, 0)
    height, width = img.shape
    cropped_img = img[15:height-15, 15:width-15]
    cropped_height, cropped_width = cropped_img.shape
    first_boundary = int(cropped_height/3)
    second_boundary = 2 * int(cropped_height/3)
    blue = cropped_img[0:first_boundary,:]
    green = cropped_img[first_boundary:second_boundary,:]
    red = cropped_img[second_boundary:second_boundary+int(cropped_height/3),:]
    file_saving_dir = os.path.join(desktop_path, "hw1_data", "rgb_images")
    file_saving_path = os.path.join(file_saving_dir, file)
    aligned_green,best_x_green, best_y_green = min_ssd_calculation(blue, green)
    aligned_red, best_x_red, best_y_red = min_ssd_calculation(blue, red)
    pixel_shifting.append([best_x_green,best_y_green,best_x_red, best_y_red])
    img_color = cv2.merge([blue, aligned_green, aligned_red])
    cv2.imwrite(file_saving_path, img_color)
    print(pixel_shifting)




