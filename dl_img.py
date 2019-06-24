import imageio
import os


def dl_img(links, dir, n):
    out_dir = os.path.join(dir, 'output', n)
    length = len(links)

    if (os.path.isdir(out_dir) == False):
        os.mkdir(os.path.join(dir, 'output'))
        os.mkdir(out_dir)

    for index, l in enumerate(links):
        print('Downloading {0} of {1} images'.format(index + 1, length))
        im = imageio.imread(l)
        filename = os.path.join(out_dir, '{0}{1}'.format(str(index + 1), '.jpeg'))
        imageio.imwrite(filename, im)

    print('Complete')
