import velodyne_decoder as vd
import numpy as np
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
import pylab
import imageio
import skimage.io
import open3d as o3d

# reference: https://programming-surgeon.com/en/euler-angle-python-en/
def rotation_matrix(theta1, theta2, theta3, order='xyz'):
    c1 = np.cos(theta1 * np.pi / 180)
    s1 = np.sin(theta1 * np.pi / 180)
    c2 = np.cos(theta2 * np.pi / 180)
    s2 = np.sin(theta2 * np.pi / 180)
    c3 = np.cos(theta3 * np.pi / 180)
    s3 = np.sin(theta3 * np.pi / 180)
    matrix = np.array([[c2 * c3, -c2 * s3, s2],
                       [c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, -c2 * s1],
                       [s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, c1 * c2]])
    return matrix


'''
capture the lidar data
'''

# config = vd.Config(model='VLP-32C', rpm=600)
# pcap_file = '2023-03-03-15-43-54_Intersection-120-Amsterdam.pcap'
#
# video_image = cv2.imread('video_image.png')
# # cv2.imshow('image', video_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# data_length = 10000000000
#
# cloud_arrays = np.zeros((data_length, 6))
#
# data_index = 0
# counter = 0 # there are 30 collected data in one second
#
#
# for stamp, points in vd.read_pcap(pcap_file, config):
#     points = np.array(points)
#     # print("Real Time: ", datetime.fromtimestamp(stamp), points.shape)
#     # # print(str(datetime.fromtimestamp(stamp))[-15:-7])
#     # if str(datetime.fromtimestamp(stamp))[-15:-7] == "15:43:57":
#     #     # print("Real Time: ", datetime.fromtimestamp(stamp))
#     #     cloud_arrays[data_index:data_index + points.shape[0]] = points
#     #     data_index = data_index + points.shape[0]
#     #     print(data_index)
#
#     if counter != 30:
#         counter = counter + 1
#         print("Real Time: ", datetime.fromtimestamp(stamp), points.shape)
#         cloud_arrays[data_index:data_index + points.shape[0]] = points
#         data_index = data_index + points.shape[0]
#         print(data_index)
#     else:
#         counter = 0
#         break
#
# data_xyz = cloud_arrays[0:data_index, 0:3]
# print(data_xyz.shape)
# # print(data_xyz)
#
# print('rotation matrix: ', rotation_matrix(0, 0, 60))
# data_xyz_rotation = rotation_matrix(0, 0, 60).dot(data_xyz.T).T # reference: https://stackoverflow.com/questions/38372194/python-numpy-apply-rotation-matrix-to-each-line-in-array
# print(data_xyz_rotation.shape)
#
# data_xyz_rotation_projection = data_xyz_rotation[:, 0:2]
# data_xyz_rotation_projection[:, 1] = -data_xyz_rotation_projection[:, 1]
#
#
# center = [None] * len(data_xyz_rotation_projection)
# for i in range(len(data_xyz_rotation_projection)):
#     center[i] = (int(130 + 20 * data_xyz_rotation_projection[i, 0]), int(734 + 20 * data_xyz_rotation_projection[i, 1]))
#
# # for i in range(len(data_xyz_rotation_projection)):
# #     synchronization_image = cv2.circle(video_image, center[i], radius=0, color=(0, 0, 255), thickness=-1)
# # cv2.imshow('image', synchronization_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# # pcd = o3d.geometry.PointCloud()
# # pcd.points = o3d.utility.Vector3dVector(data_xyz_rotation)
# # # pcd.rotate(pcd.get_rotation_matrix_from_xyz((0, 0, 1.03)))
# # vis = o3d.visualization.Visualizer()
# # vis.create_window()
# # vis.add_geometry(pcd)
# # # o3d.visualization.ViewControl.set_zoom(vis.get_view_control(), 0.015)
# # # o3d.visualization.ViewControl.translate(vis.get_view_control(), x=-1000, y=1000, xo=0, yo=0)
# # vis.run()
# # # vis.capture_screen_image('point cloud.png')






'''
capture the video data
'''
cap = cv2.VideoCapture('outputvideo_343_transformed.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS) # fps = 15
    # cv2.imwrite('video_image.png', frame)
    # for i in range(len(data_xyz_rotation_projection)):
    #     synchronization_image = cv2.circle(frame, center[i], radius=0, color=(0, 0, 255), thickness=-1)
    # cv2.imshow('image', synchronization_image)
    cv2.imshow('image', frame)

    # press any buttom
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


