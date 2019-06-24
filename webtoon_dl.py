import sys
from get_imgurl import get_imgurl
from dl_img import dl_img


def main():
    input_url = sys.argv[1]
    out_dir = sys.argv[2]

    links = get_imgurl(input_url)
    dl_img(links, out_dir)


if __name__ == '__main__':
    main()
