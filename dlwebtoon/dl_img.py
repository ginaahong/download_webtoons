import imageio
import os
import requests
import shutil


def daum_dl_img(links, dir, n):
    # change so that you use requests and shutil (reduce packages by not using imageio (which in turn req numpy and pillow))
    out_dir = os.path.join(dir, 'output', n)
    length = len(links)

    if (os.path.isdir(out_dir) == False):
        if (os.path.isdir(os.path.join(dir, 'output')) == True):
            os.mkdir(out_dir)
        else:
            os.mkdir(os.path.join(dir, 'output'))
            os.mkdir(out_dir)

    for index, l in enumerate(links):
        print('Downloading {0} of {1} images'.format(index + 1, length))
        im = imageio.imread(l)
        filename = os.path.join(out_dir, '{0}{1}'.format(str(index + 1), '.jpeg'))
        imageio.imwrite(filename, im)

    print('Complete')


def naver_dl_img(links, dir, n):
    # uses requests and shutil since user-agent had to be specified to access the images.
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.U6'
    }
    out_dir = os.path.join(dir, 'output', n)
    length = len(links)

    if (os.path.isdir(out_dir) == False):
        if (os.path.isdir(os.path.join(dir, 'output')) == True):
            os.mkdir(out_dir)
        else:
            os.mkdir(os.path.join(dir, 'output'))
            os.mkdir(out_dir)

    for index, l in enumerate(links):
        print('Downloading {0} of {1} images'.format(index + 1, length))
        # im = imageio.imread(l)
        filename = os.path.join(out_dir, '{0}{1}'.format(str(index + 1), '.jpg'))
        # imageio.imwrite(filename, im)

        response = requests.get(l, headers=headers, stream=True)
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

    print('Complete')
