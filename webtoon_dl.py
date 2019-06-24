import sys
import os

from get_imgurl import naver_get_imgurl, daum_get_imgurl
from dl_img import dl_img
from domain_iden import n_or_d


def main():
    input_url = sys.argv[1]
    out_dir = sys.argv[2]

    if (n_or_d(input_url) == 'n'):
        print("Naver comic given")
        # links, name = naver_get_imgurl(input_url)
    elif (n_or_d(input_url) == 'd'):
        print("Daum comic given")
        links, name = daum_get_imgurl(input_url)
    else:
        print("Only Naver or Daum links are supported.")

    dl_img(links, out_dir, name)
    # print(os.path.join(out_dir,'{0}{1}'.format('1','.img')))


if __name__ == '__main__':
    main()

# copy and paste:
# python webtoon_dl.py http://webtoon.daum.net/webtoon/viewer/68383 ~/webtoon_dl
