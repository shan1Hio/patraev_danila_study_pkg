from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    freq_arg = DeclareLaunchArgument(
        'frequency',
        default_value ='8.0',
        description ='Частота публикации even_number_publisher (Гц)'
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value ='80',
        description ='Порог переполнения счетчика'
    )

    topic_1_arg = DeclareLaunchArgument(
        'topic_name_1', 
        default_value ='even_numbers',
        description = 'Имя топика для публикации чисел'
    )

    topic_2_arg = DeclareLaunchArgument(
        'topic_name_2', 
        default_value ='overflow',
        description = 'Имя топика для публикации максимального числа'
    )

    publisher_arg = DeclareLaunchArgument(
        'node_name_1', 
        default_value ='even_pub',
        description = 'Узел издатель'
    )

    listener_arg = DeclareLaunchArgument(
        'node_name_2', 
        default_value ='overflow_l',
        description = 'Узел подписчик'
    )

    frequency = LaunchConfiguration('frequency')
    overflow_thr = LaunchConfiguration('overflow_threshold')
    topic_1 = LaunchConfiguration('topic_name_1')
    topic_2 = LaunchConfiguration('topic_name_2')
    publisher_node_n = LaunchConfiguration('node_name_1')
    listener_node_n = LaunchConfiguration('node_name_2')

    publisher_node = Node(
        package ='patraev_danila_study_pkg',
        executable ='even_number_publisher',
        name = publisher_node_n,
        parameters = [
            {'publish_frequency': frequency},
            {'overflow_threshold': overflow_thr},
            {'topic_name_1': topic_1},
            {'topic_name_2': topic_2},
            {'node_name_1': publisher_node_n},
            ],
        )
    
    listener_node = Node(
        package ='patraev_danila_study_pkg',
        executable ='overflow_listener',
        name = listener_node_n,
        parameters = [
            {'overflow_threshold': overflow_thr},
            {'topic_name_2': topic_2},
            {'node_name_2': listener_node_n},
            ],
        )

    return LaunchDescription([
        freq_arg,
        threshold_arg,
        topic_1_arg,
        topic_2_arg,
        publisher_arg,
        listener_arg,
        publisher_node,
        listener_node
    ])