from setuptools import setup

setup(
    name='clean_folder',
    version='1.0',
    description='program for organizing files in your folders',
    url='https://github.com/Ivan-Danyleiko/Clean_folder_project',
    author='Ivanko Danyleiko',
    author_email='vanyadanuleyko@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    long_description="Some long desctiption",
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
    include_package_data=True
)