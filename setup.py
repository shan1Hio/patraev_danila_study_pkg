from setuptools import find_packages, setup

package_name = 'patraev_danila_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shan1Hio',
    maintainer_email='roflanmoment@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = patraev_danila_study_pkg.talker:main',
            'listener = patraev_danila_study_pkg.listener:main',
            'even_number_publisher = patraev_danila_study_pkg.even_number_publisher:main',
            'overflow_listener = patraev_danila_study_pkg.overflow_listener:main',
        ],
    },
)
