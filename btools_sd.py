##################################################################
# B-TOOLS-SD v0.24
#
# Stable Diffusion:
# sd(prompt, save=False, save_path, negative_prompt="", steps, sampler_name,  width, height, cfg_scale,enable_hr=False, denoising_strength, hr_scale, hr_upscaler, hr_second_pass_steps, url)
# upscale(image:str, resize_factor, save=False, save_path, upscaler_1, upscaler_2, upscaler_2_visibility, width, height, url)
# load_image_as_base64() - Utility function for SD methods
#
##################################################################

import requests
from PIL import Image, PngImagePlugin
import base64
import io

# SD() - create a single image, optionally save it to file, and return it as a b64-encoded string
def sd(prompt, save=False, save_path="output.png", negative_prompt="", steps:int=20, sampler_name="Euler",  width:int=512, height:int=512, cfg_scale:int=7,enable_hr=False, denoising_strength:float=0, hr_scale:int=2,hr_upscaler="Latent", hr_second_pass_steps:int=0, url="http://127.0.0.1:7860"):

    # Create the image

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": steps,
        "sampler_name": sampler_name,
        "enable_hr": enable_hr,
        "denoising_strength": denoising_strength,
        "hr_scale": hr_scale,
        "hr_upscaler": hr_upscaler,
        "hr_second_pass_steps": hr_second_pass_steps,
        "batch_size": 1,
        "n_iter": 1,
        "cfg_scale": cfg_scale,
        "width": width,
        "height": height,
        "tiling": False,
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
    }

    print(" Rendering...")

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    if save:
        
        # Process and save the image

        for i in r['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

            png_payload = {
                "image": "data:image/png;base64," + i
            }
            response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))
            image.save(save_path, pnginfo=pnginfo)

        print(" Wrote image.")

    # Return the image (b64-encoded string)
    return r['images'][0]

def load_image_as_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
    return base64_encoded_image

# upscale() - Upscale an image, optionally save it to a file, and return the upscaled image as a b64-encoded string
def upscale(image:str, resize_factor:int=2, save=False, save_path="upscale.png", upscaler_1="", upscaler_2="", upscaler_2_visibility:float=0.5, width:int=512, height:int=512, url="http://127.0.0.1:7860"):

    payload = {
    "upscaling_resize": resize_factor,
    "upscaling_resize_w": width,
    "upscaling_resize_h": height,
    "upscaling_crop": True,
    "upscaler_1": "R-ESRGAN 4x+",
    "upscaler_2": "ESRGAN_4x",
    "extras_upscaler_2_visibility": 0.5,
    "image": image
    }

    print(" Upscaling...")

    response = requests.post(url=f'{url}/sdapi/v1/extra-single-image', json=payload)

    r = response.json()

    
    # Process and save the image

    image = Image.open(io.BytesIO(base64.b64decode(r['image'].split(",",1)[0])))    
    print(image)
    png_payload = {
        "image": "data:image/png;base64," + r['image']
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    # Create a PNGInfo object to store metadata
    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    image.save(save_path, pnginfo=pnginfo)

    print(" Wrote upscale.")

    return r['image'][0]