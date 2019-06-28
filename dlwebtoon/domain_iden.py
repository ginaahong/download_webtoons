
# url --> int
# if url is naver, return True
# o.w return False


def n_or_d(url):
    if 'comic.naver' in str(url):
        return 'n'
    elif 'webtoon.daum' in str(url):
        return 'd'
    else:
        return 'a'
