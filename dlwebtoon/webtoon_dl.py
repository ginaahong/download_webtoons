import sys
import os

from dlwebtoon.get_imgurl import naver_get_imgurl, daum_get_imgurl
from dlwebtoon.dl_img import daum_dl_img, naver_dl_img
from dlwebtoon.domain_iden import n_or_d


def main():
    input_url = sys.argv[1]
    # print(sys.argv) // make sure there aren't any ambpersand in url
    out_dir = sys.argv[2]

    if (n_or_d(input_url) == 'n'):
        print("Naver comic given")
        links, name = naver_get_imgurl(input_url)
        naver_dl_img(links, out_dir, name)
    # links, name = naverå_get_imgurl(input_url)
    elif (n_or_d(input_url) == 'd'):
        print("Daum comic given")
        links, name = daum_get_imgurl(input_url)
        daum_dl_img(links, out_dir, name)
    else:
        print("Only Naver or Daum links are supported.")

    # print(os.path.join(out_dir,'{0}{1}'.format('1','.img')))


if __name__ == '__main__':
    main()

# copy and paste:
# python webtoon_dl.py 'http://webtoon.daum.net/webtoon/viewer/68383' ~/webtoon_dl
# python webtoon_dl.py 'https://comic.naver.com/webtoon/detail.nhn?titleId=702672&no=155' ~/webtoon_dl
