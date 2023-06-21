import streamlit as st
import base64
from PIL import Image
import requests
import cv2
import numpy as np
import sys
import yaml
import os
sys.path.insert(0,'./AnimatedDrawings')
sys.path.insert(1,'./examples')
sys.path.insert(2,'./TextExtraction-to-voice')

from examples.image_to_animation import image_to_animation
from examples.image_to_annotations import image_to_annotations
from animated_drawings import render
from typing import Union
from dotenv import load_dotenv
from streamlit_cropper import st_cropper
import tempfile
load_dotenv()
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from get_image import  audio_ocr
cloudinary.config(
  cloud_name = "djvu7apub",
  api_key = os.getenv("API_KEY_CLOUD"),
  api_secret = os.getenv("API_SECRET"),
  secure = True
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def create_image(motion, image_path):

    image_path = image_path
    char_anno_dir = os.getenv("OUTPUT")

    if motion == 'dab' or motion == 'jumping' or motion == 'wave_hello':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET')

        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    elif motion == 'jesse_dance':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_JESSE'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_JESSE')

        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    elif motion == 'zombie':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_ZOMBIE'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_ZOMBIE')

        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    elif motion == 'jumping_jacks':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_JACKS'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_JACKS')


        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    elif motion == 'Running_Motion':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_RUNNING'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_RUNNING')


        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            # os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    elif motion == 'RUNNING_MOTION':
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_RUNNING_FORWARD'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_RUNNING_FORWARD')


        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")
    else:
        print("enter")
        image_to_animation(image_path, char_anno_dir, f"{os.getenv('MOTION')}/{motion}.yaml", os.getenv('RETARGET_WALKING'))
        with open(os.getenv("EXPORT_GIF"), "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        data['scene']['ANIMATED_CHARACTERS'][0]['character_cfg'] = os.getenv("OUTPUT_CHAR_CFG")
        data["scene"]["ANIMATED_CHARACTERS"][0]["motion_cfg"] = f"{os.getenv('MOTION')}/{motion}.yaml"
        data['scene']['ANIMATED_CHARACTERS'][0]['retarget_cfg'] = os.getenv('RETARGET_WALKING')


        try :
            with open('example.yaml', 'w') as file:
                yaml.dump(data, file)
            render.start("./example.yaml")
            # audio_url = audio_ocr(image_path)

        except Exception as e:
            raise e
        finally:
            upload_result = cloudinary.uploader.upload("./vedio.gif", resource_type="auto")
            # upload_audio = cloudinary.uploader.upload("./test-file.wav", resource_type="auto")

            os.remove("./example.yaml")
            # os.unlink(image_path)
            # os.remove("./vedio.gif")

        
    return {
            "url": upload_result["secure_url"], 
            # "audio_url": upload_audio["secure_url"]
        }


def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5; /* Set the background color */
            font-family: Arial, sans-serif; /* Set the font family */
            padding: 20px; /* Add padding to the content */
        }
        .stButton button { 
            background-color: #336699; /* Set the button background color */
            color: white; /* Set the button text color */
            padding: 8px 16px; /* Adjust button padding */
            border-radius: 4px; /* Add button border radius */
            border: none; /* Remove button border */
            cursor: pointer; /* Add cursor pointer on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Animated Drawings")
    st.write("Upload an image and see it displayed below:")

    if 'rotation_angle' not in st.session_state:
        st.session_state.rotation_angle = 0
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        rotated_image = Image.open(uploaded_file)
        rotated_image = st_cropper(rotated_image, box_color=(255, 255, 255, 0.5), realtime_update=True)
        st.session_state.rotation_angle += 90
        rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
        rotated_image = rotated_image.rotate(rotation_angle, expand=True)
        st.image(rotated_image, caption="Uploaded Image", width=300)
        # if st.button("Done"):
        #     images_list.append(rotated_image)

    else:
        st.write("Please upload an image file.")



    Jesse_Dance, Dancing, Jumping, Jumping_Jacks, Walking, Running, Wave_hand = False, False, False, False, False, False, False
    flag = False
    button_container = st.empty()
    with button_container.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Dancing"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Dancing = True
                st.write("Dancing Animation is playing")
        with col2:
            if st.button("Walking"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Walking = True
                st.write("walking Animation is playing")
        with col3:
            if st.button("Running"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Running = True
                st.write("Running Animation is playing")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Jumping Jacks"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Jumping_Jacks = True
                st.write("Jumping Jacks Animation is playing")
        with col2:
            if st.button("Jesse Dance"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Jesse_Dance = True
                st.write("Jessie Dance Animation is playing")
        with col3:
            if st.button("Jumping"):
                img_cv = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite("temp.jpg", img_cv)
                Jumping  = True
                st.write("Jumping Animation is playing")
    upload_result_joint_overlap = cloudinary.uploader.upload("./temp.jpg")

    image_url = upload_result_joint_overlap['secure_url']
    # Create a temporary file to save the uploaded image
    print(image_url)
    url = 'http://localhost:7000/Animation'
    if Jumping == True:
        st.info("Please wait for a while")
        payload = {
        'motion': 'jumping', 
        'image_path': image_url
        }
        print('started')
        response = requests.post(url, params=payload)
        st.info("Jumping")
        # gif_url = response['url']
        Jumping = False
        flag = True

    
    if Walking == True:
        st.info("Please wait for a while")
        payload = {
        'motion': 'zombie', 
        'image_path': str(image_url)
        }
        print('started')
        response = requests.post(url, params=payload).content
        # response = create_image('zombie', "./temp.jpg")
        st.info("Walking")
        # gif_url = response['url']
        Walking = False
        flag = True
    if Running == True:
        st.info("Please wait for a while")
        payload = {
        'motion': 'Running_Motion', 
        'image_path': './temp.jpg'
        }
        print('started')
        response = requests.post(url, params=payload)
        st.info("Running")
        # gif_url = response['url']
        Running = False
        flag = True

    if Jumping_Jacks == True:
        st.info("Please wait for a while")
        payload = {
        'motion': 'jumping_jacks', 
        'image_path': './temp.jpg'
        }
        print('started')
        response = requests.post(url, params=payload).content
        st.info("Jumping Jacks")
        # gif_url = response['url']

        Jumping_Jacks = False
        flag = True

    if Dancing == True:
        st.info("Please wait for a while")
        payload = {
        'motion': 'dab', 
        'image_url': 'https://res.cloudinary.com/djvu7apub/image/upload/v1685354924/rp7mmnyaoqlxcy3pej4c.jpg'
        }
        print('started')
        response = requests.post(url, json=payload)
        st.info("Dancing")
        st.info(response.content)

        Dancing = False
        flag = True

    if Jesse_Dance == True:
        st.info("Please wait for a while")
        
        response = create_image('jesse_dance', "./temp.jpg")
        st.info("Jesse Dance")
        # gif_url = response['url']

        Jesse_Dance = False
        flag = True


    if flag == True:
        st.image('./vedio.gif', use_column_width=True)

        # url = audio_ocr("./temp.jpg")
        # print(url)

        
        # audio_file = open('./save.wav', 'rb')
        # audio_bytes = audio_file.read()

        # st.audio(audio_bytes, format='audio/ogg')

        flag = False






if __name__ == "__main__":
    main()


