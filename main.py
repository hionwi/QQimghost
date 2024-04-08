import base64
import hashlib
import typer

import requests

QQid = 123456789
robot_id = 123465789
ip = 'localhost'
port = 5700


def calculate_md5(file_path):
    with open(file_path, "rb") as f:
        md5_hash = hashlib.md5()

        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)

    md5_hex = md5_hash.hexdigest()
    return md5_hex


def send_pic(pic_name):
    with open(pic_name, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode()
    # 填写go-cqhttp对应的ip与port
    url = f'http://{ip}:{port}/send_private_msg'
    # 填写QQ号
    data = {'user_id': QQid,
            'message': f"[CQ:image,type=show,file=base64://{image_base64}]",
            'auto_escape': False}
    response = requests.post(url, json=data)


def main(image_file_paths: list[str]):
    for image_file_path in image_file_paths:
        image_md5 = calculate_md5(image_file_path).upper()
        send_pic(image_file_path)
        pic_bed_url = f'https://c2cpicdw.qpic.cn/offpic_new/{QQid}//{QQid}-{robot_id}-{image_md5}/0'
        print(pic_bed_url)


if __name__ == '__main__':
    typer.run(main)
