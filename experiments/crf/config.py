import logging

# Logging level
log_level = logging.INFO

logfile = 'output.txt'

# Number of CPUs used for parallel processing
N_PROC = 14

#Maximum number of iterations before optimisation is stopped
MAX_N_IT = -1


# Image/Seg shape
slice_shape = (388,388)

#Initial Parameters
params_initial_liver = [\
3,  # pos_x_std
0.75,  # pos_y_std
3,  # pos_z_std
60,  # bilateral_x_std
15,  # bilateral_y_std
15,  # bilateral_z_std
20.0, # bilateral_intensity_std
0.75,  # pos_w
1.0   # bilateral_w  #we fix this one during optimization
]

params_initial_lesion = [\
3.0,  # pos_x_std
3.0,  # pos_y_std
3.0,  # pos_z_std
60.0,  # bilateral_x_std
60.0,  # bilateral_y_std
60.0,  # bilateral_z_std
20.0, # bilateral_intensity_std
3.0,  # pos_w
10.0   # bilateral_w  #we fix this one during optimization
]


### CHOOSE LIVER OR LESION
params_initial = params_initial_liver
target_label = 1


#Fixed CRF Parameters
max_iterations = 20
dynamic_z = False
ignore_memory = True




###########################
##### 3DIRCA DATASET ######
###########################


test_set=[
(82, '/home/guest/training/volume-82.npy', '/home/guest/training/segmentation-82.npy') ,
(74, '/home/guest/training/volume-74.npy', '/home/guest/training/segmentation-74.npy') ,
(125, '/home/guest/training/volume-125.npy', '/home/guest/training/segmentation-125.npy') ,
(11, '/home/guest/training/volume-11.npy', '/home/guest/training/segmentation-11.npy') ,
(89, '/home/guest/training/volume-89.npy', '/home/guest/training/segmentation-89.npy') ,
(78, '/home/guest/training/volume-78.npy', '/home/guest/training/segmentation-78.npy') ,
(64, '/home/guest/training/volume-64.npy', '/home/guest/training/segmentation-64.npy') ,
(126, '/home/guest/training/volume-126.npy', '/home/guest/training/segmentation-126.npy') ,
(129, '/home/guest/training/volume-129.npy', '/home/guest/training/segmentation-129.npy') ,
(114, '/home/guest/training/volume-114.npy', '/home/guest/training/segmentation-114.npy') ,
(37, '/home/guest/training/volume-37.npy', '/home/guest/training/segmentation-37.npy') ,
(25, '/home/guest/training/volume-25.npy', '/home/guest/training/segmentation-25.npy') ,
(85, '/home/guest/training/volume-85.npy', '/home/guest/training/segmentation-85.npy') ,
(80, '/home/guest/training/volume-80.npy', '/home/guest/training/segmentation-80.npy') ,
(27, '/home/guest/training/volume-27.npy', '/home/guest/training/segmentation-27.npy') ,
(18, '/home/guest/training/volume-18.npy', '/home/guest/training/segmentation-18.npy') ,
(69, '/home/guest/training/volume-69.npy', '/home/guest/training/segmentation-69.npy') ,
(40, '/home/guest/training/volume-40.npy', '/home/guest/training/segmentation-40.npy') ,
(61, '/home/guest/training/volume-61.npy', '/home/guest/training/segmentation-61.npy') ,
(117, '/home/guest/training/volume-117.npy', '/home/guest/training/segmentation-117.npy') ,
(44, '/home/guest/training/volume-44.npy', '/home/guest/training/segmentation-44.npy') ,
(26, '/home/guest/training/volume-26.npy', '/home/guest/training/segmentation-26.npy') ,
(91, '/home/guest/training/volume-91.npy', '/home/guest/training/segmentation-91.npy') ,
(65, '/home/guest/training/volume-65.npy', '/home/guest/training/segmentation-65.npy') ,
(55, '/home/guest/training/volume-55.npy', '/home/guest/training/segmentation-55.npy') ,
(5, '/home/guest/training/volume-5.npy', '/home/guest/training/segmentation-5.npy') ,
(77, '/home/guest/training/volume-77.npy', '/home/guest/training/segmentation-77.npy') ,
(12, '/home/guest/training/volume-12.npy', '/home/guest/training/segmentation-12.npy') ,
(28, '/home/guest/training/volume-28.npy', '/home/guest/training/segmentation-28.npy') ,
(6, '/home/guest/training/volume-6.npy', '/home/guest/training/segmentation-6.npy') ,
(79, '/home/guest/training/volume-79.npy', '/home/guest/training/segmentation-79.npy') ,
(84, '/home/guest/training/volume-84.npy', '/home/guest/training/segmentation-84.npy') ,
(103, '/home/guest/training/volume-103.npy', '/home/guest/training/segmentation-103.npy') ,
(101, '/home/guest/training/volume-101.npy', '/home/guest/training/segmentation-101.npy') ,
(106, '/home/guest/training/volume-106.npy', '/home/guest/training/segmentation-106.npy') ,
(59, '/home/guest/training/volume-59.npy', '/home/guest/training/segmentation-59.npy') ,
(45, '/home/guest/training/volume-45.npy', '/home/guest/training/segmentation-45.npy') ,
(53, '/home/guest/training/volume-53.npy', '/home/guest/training/segmentation-53.npy') ,
(41, '/home/guest/training/volume-41.npy', '/home/guest/training/segmentation-41.npy') ,
(121, '/home/guest/training/volume-121.npy', '/home/guest/training/segmentation-121.npy')]


# Select dataset
#dataset = [irca_train_fold1, irca_test_fold1,\
#		irca_train_fold2, irca_test_fold2,\
#		irca_train_fold3, irca_test_fold3,\
#		irca_train_fold4, irca_test_fold4]
#


#Datset to test
dataset = test_set
