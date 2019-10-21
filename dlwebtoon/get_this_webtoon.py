import subprocess

mainUrl = 'https://comic.naver.com/webtoon/detail.nhn?titleId=729767&no='
no = 8
restUrl = '&weekday=fri'

dir = '~/webtoon_dl'

for x in range(no, 19):
    url = "{}{}{}".format(mainUrl, str(x), restUrl)
    cmd = "{} \'{}\' {}".format('dlwebtoon', url, '~/webtoon_dl')
    print(cmd)
    # print(url)
    # # print('dlwebtoon' + ' \'' + url + '\' ' + '~/webtoon_dl')
    # subprocess.run(['dlwebtoon', url, '~/webtoon_dl'])
    subprocess.run(cmd, shell=True)



