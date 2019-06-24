import sys
import os

from get_imgurl import get_imgurl
from dl_img import dl_img


def main():
    input_url = sys.argv[1]
    out_dir = sys.argv[2]

    links, name = get_imgurl(input_url)
    dl_img(links, out_dir, name)
    # print(os.path.join(out_dir,'{0}{1}'.format('1','.img')))


if __name__ == '__main__':
    main()

# copy and paste:
# python webtoon_dl.py http://webtoon.daum.net/webtoon/viewer/68383 ~/webtoon_dl
