import sys
import argparse
import requests

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = '5538994d5ffa3de221ffdc494e637777'


def generate_tag(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if len(result['label_kr']) > 0:
            if type(result['label_kr'][0]) != str:
                result['label_kr'] = map(lambda x: str(x.encode("utf-8")), result['label_kr'])
            print("이미지를 대표하는 태그는 \"{}\"입니다.".format(','.join(result['label_kr'])))
        else:
            print("이미지로부터 태그를 생성하지 못했습니다.")

    except Exception as e:
        print(str(e))
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify Tags')
    parser.add_argument('image_url', type=str, nargs='?',
        default="https://www.ikea.com/kr/ko/images/products/svartra-led-lighting-chain-with-12-lights-black-outdoor__0568769_PH145979_S5.JPG",
        help='image url to classify')

    args = parser.parse_args()

    generate_tag(args.image_url)
