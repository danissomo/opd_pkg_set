#!/usr/bin/python3
import rospy
if __name__ == '__main__':
    rospy.init_node('robo_param', log_level=rospy.DEBUG)
    #common
    rospy.set_param('~rs_image_topic', '/realsense_gripper/color/image_raw')
    rospy.set_param('~rs_image_topic_c', '/realsense_gripper/color/image_raw/compressed')
    rospy.set_param('~rs_depth_topic', '/realsense_gripper/aligned_depth_to_color/image_raw')
    rospy.set_param('~rs_camera_info', '/realsense_gripper/color/camera_info')
    rospy.set_param('~rs_frame', 'rs_camera')

    # elevator project
    elev_ns = 'elev' 
    rospy.set_param(f'~elev_ns', elev_ns)
    rospy.set_param(f'~{elev_ns}/push_srv_name', f'/{elev_ns}/push_button')
    rospy.set_param(f'~{elev_ns}/recog_srv_name', f'/{elev_ns}/recognition_service')

    #husky param
    husky_ns = 'husky'
    rospy.set_param(f'~husky_ns', husky_ns)
    rospy.set_param(f'~{husky_ns}/movej_srv_name', f'/{husky_ns}/MoveJ')
    rospy.set_param(f'~{husky_ns}/movel_srv_name', f'/{husky_ns}/MoveL')
    rospy.set_param(f'~{husky_ns}/getl_srv_name', f'/{husky_ns}/GetTCPPose')
    rospy.set_param(f'~{husky_ns}/getq_srv_name', f'/{husky_ns}/GetQ')
    rospy.set_param(f'~{husky_ns}/grip_srv_name', f'/{husky_ns}/SetGripper')
    