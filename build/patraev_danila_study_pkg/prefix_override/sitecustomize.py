import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ldps-06/ros2_ws/src/patraev_danila_study_pkg/install/patraev_danila_study_pkg'
