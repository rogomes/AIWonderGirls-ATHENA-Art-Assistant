from dalle_mini.model import CustomFlaxBartForConditionalGeneration
from transformers import BartTokenizer
import jax
import random
from tqdm.notebook import tqdm, trange
from vqgan_jax.modeling_flax_vqgan import VQModel
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, FlaxCLIPModel
import os
import genvideo

# set a prompt
prompt = 'picture of a waterfall under the sunset'

def gen_paintings(prompt):
    # make sure we use compatible versions
    DALLE_REPO = 'flax-community/dalle-mini'
    DALLE_COMMIT_ID = '4d34126d0df8bc4a692ae933e3b902a1fa8b6114'
    # make sure we use compatible versions
    VQGAN_REPO = 'flax-community/vqgan_f16_16384'
    VQGAN_COMMIT_ID = '90cc46addd2dd8f5be21586a9a23e1b95aa506a9'

    # set up tokenizer and model
    tokenizer = BartTokenizer.from_pretrained(DALLE_REPO, revision=DALLE_COMMIT_ID)
    model = CustomFlaxBartForConditionalGeneration.from_pretrained(DALLE_REPO, revision=DALLE_COMMIT_ID)

    # tokenize the prompt
    tokenized_prompt = tokenizer(prompt, return_tensors='jax', padding='max_length', truncation=True, max_length=128)
    tokenized_prompt

    n_predictions = 8

    # create random keys
    seed = random.randint(0, 2**32-1)
    key = jax.random.PRNGKey(seed)
    subkeys = jax.random.split(key, num=n_predictions)
    # generate sample predictions
    encoded_images = [model.generate(**tokenized_prompt, do_sample=True, num_beams=1, prng_key=subkey) for subkey in tqdm(subkeys)]

    # remove first token (BOS)
    encoded_images = [img.sequences[..., 1:] for img in encoded_images]

    # set up VQGAN
    vqgan = VQModel.from_pretrained(VQGAN_REPO, revision=VQGAN_COMMIT_ID)

    # decode images
    decoded_images = [vqgan.decode_code(encoded_image) for encoded_image in tqdm(encoded_images)]

    # normalize images
    clipped_images = [img.squeeze().clip(0., 1.) for img in decoded_images]

    # convert to image
    images = [Image.fromarray(np.asarray(img * 255, dtype=np.uint8)) for img in clipped_images]

    # set up model and processor
    clip = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # evaluate scores
    inputs = processor(text=prompt, images=images, return_tensors='np')
    logits = clip(**inputs).logits_per_image
    scores = jax.nn.softmax(logits, axis=0).squeeze()  # normalize and sum all scores to 1

    # Save generated images
    if not os.path.exists('./images_dir'):
        os.makedirs('./images_dir')

    for i, img in enumerate(images):
      # save a image using extension
      im1 = img.save("./images_dir/" + str(i) + ".png")

    if not os.path.exists('./video_dir'):
         os.makedirs('./video_dir')

if __name__ == '__main__':
    # Taking the input for the paths of the variables mentioned below.
    folder_path = "./images_dir/"
    audio_path = "./audio_dir/ludwig.mp3"
    video_path_name = "./video_dir/generated_video.mp4"
    prompt = input("Enter a sentence or paragraph : ")

    import time

    start = time.time()
    gen_paintings(prompt)
    end = time.time()
    print(end - start)

    # Invoking the parameterized constructor of the MP3ToMP4 class.
    genvideo.MP3ToMP4(folder_path, audio_path, video_path_name)
