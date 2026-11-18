# Face Age Transformation

An experimental deep learning project exploring facial age transformation
using Style-based Age Manipulation (SAM).

## What I worked on

- Generated synthetic faces using a pretrained StyleGAN model.
- Prepared a sample of 1,000 UTKFace images: 883 for training and 117 for testing.
- Fine-tuned a pretrained SAM model for 100 steps on a Tesla T4 GPU.
- Compared age transformations before and after fine-tuning.
- Explored hypothetical facial visualization from a mummified face.

## Important limitations

- Age-transformed images are hypothetical, not predictions of a person's
  actual future appearance.
- The image split does not guarantee that every person is separate between
  training and testing.
- The mummy experiments are exploratory and do not establish the person's
  real appearance.
- The fine-tuned checkpoint is not included in this repository.

## Technologies

Python, PyTorch, Google Colab, StyleGAN, SAM and Hugging Face.

## Getting started

Open the notebook in Google Colab and select a GPU runtime.
Run the cells in order. The notebook may require downloading pretrained
weights and preparing dataset paths before training or inference.

Review the licenses and terms of the models, datasets and images before use.

## Credits

- [Style-based Age Manipulation (SAM)](https://github.com/yuval-alaluf/SAM)
- [StyleGAN2-ADA PyTorch](https://github.com/NVlabs/stylegan2-ada-pytorch)
- [UTKFace-Cropped dataset](https://huggingface.co/datasets/py97/UTKFace-Cropped)
