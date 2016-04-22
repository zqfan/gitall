from setuptools import setup, find_packages

setup(
    name = 'gitall',
    packages = find_packages(),
    version = '0.1.2',
    install_requires = [
        'GitPython',
        'requests'
    ],
    entry_points = {
        'console_scripts': [
            'gitall = gitall.gitall:main',
        ],
    },
    description = 'clone/pull all repositories of a specified orgnization',
    author = 'ZhiQiang Fan',
    author_email = 'zqfan.dev+gitall@gmail.com',
    url = 'https://github.com/zqfan/gitall',
    download_url = 'https://github.com/zqfan/gitall/tarball/0.1.2',
    keywords = ['github', 'gitall'],
    classifiers = [],
)
