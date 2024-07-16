from setuptools import setup, find_packages

setup(
    name='canadapost-tracker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # If you want to add command-line scripts
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python wrapper for tracking Canada Post shipments and sending updates to Discord.',
    url='https://github.com/yourusername/canadapost-tracker',  # Update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)