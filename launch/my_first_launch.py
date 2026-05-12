
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    freq_arg = DeclareLaunchArgument(
        'publish_frequency',           
        default_value='10.0',          
        description='Частота публикации чётных чисел (Гц)'
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='100',
        description='Порог, после которого происходит переполнение'
    )

    # Получаем текущее значение аргумента
    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')

    return LaunchDescription([
        freq_arg,          # не забудь добавить аргумент сюда!
        threshold_arg,

        Node(
            package='patraev_danila_study_pkg',
            executable='even_number_publisher',
            name='even_number_publisher',
            parameters=[
                {'publish_frequency': frequency},   # используем аргумент
                {'overflow_threshold': threshold},
            ],
            output='screen',
        ),
    ])
