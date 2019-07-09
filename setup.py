import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='dlwebtoon',
    version='1.0',
    author='Gina Hong',
    description='Download webtoons for offline reading!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ginaahong/download_webtoons',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['dlwebtoon=dlwebtoon.webtoon_dl:main'],
    }
)
# setup.py enables -->
# cd /folder/of/webtoon_dl
# pip install dlwebtoon
# dlwebtoon 'link_to_comic' /path/to/output_dir
