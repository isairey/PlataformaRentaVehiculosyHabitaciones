import os
import cv2
import json
import base64
import numpy as np
import firebase_admin
from django.conf import settings
from firebase_admin import storage
from django.template import loader
from django.utils.text import slugify
from django.core.mail import EmailMultiAlternatives



os.environ['FIREBASE_CRED'] = json.dumps(credentials)

service_account_info = json.loads(os.environ.get('FIREBASE_CRED', None))
if not firebase_admin._apps:
    cred = firebase_admin.credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred, {'storageBucket': 'faer-342211.appspot.com'})

default_img_url = 'https://storage.googleapis.com/faer-342211.appspot.com/default.jpg'


def write_to_tmp(file):
    file_path = f'temp/{file}'
    encoded_file = base64.b64encode(file.read())

    # with open(file_path, 'wb+') as f:
    #     f.write(file.read())
    print(f'File added encoded:{file_path}')
    return {
        'file_name': file,
        'encoded_file': encoded_file.decode("utf-8")
    }


def serializeImg(img):
    image = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)
    _, img_buffer_arr = cv2.imencode(".jpg", image)
    img_bytes = img_buffer_arr.tobytes()
    print(len(img_bytes))
    return img_bytes


def remove_from_tmp(file_path):
    os.remove(file_path)
    print(f'File removed :{file_path}')


def upload_to_storage(image, parent):
    fileName, ext = image['file_name'].split(".")
    bucket = storage.bucket()
    blob = bucket.blob('faer/'+parent.__class__.__name__+'/'+str(parent.pk) + '/' + slugify(fileName)[:50] + '.'+ext)
    # blob.upload_from_filename(fileName)
    decoded_file = base64.b64decode(image['encoded_file'])
    blob.upload_from_string(decoded_file, content_type='image/png')
    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("File has been uploaded to : ", blob.public_url)
    return blob.public_url


def get_media_url(image, parent=None):

    media_url = upload_to_storage(image, parent)
    return media_url if media_url else default_img_url


def upload_to_firebase(file):
    fileName = 'random.png'
    bucket = storage.bucket()
    blob = bucket.blob('faer/' + fileName)
    blob.upload_from_string(file.read(), content_type='image/png')
    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("File has been uploaded to : ", blob.public_url)
    return blob.public_url


def send_email(sub, user, owner, product, to):
    template = loader.get_template("reservation_email.txt")
    context = {
        "renter": owner,
        "user": user,
        "product": product
    }
    message = template.render(context)
    msg = EmailMultiAlternatives(subject=sub, from_email=settings.EMAIL_HOST_EMAIL,
                                 to=[to], body=message)
    msg.content_subtype = "html"
    msg.send()
    print("Mail Sent Successfuly")
