# This snippet from CUDA-torch.py:
# Description: Check if CUDA is available and the version of the torch library.

# I had trouble with the CUDA version and I had to uninstall the torch library and install it again.
# This code helped me to check if the CUDA was available and the version of the torch library.
# If you find an error related to the CUDA version, you can run this lines in the terminal to fix it:
    # Step 1: Uninstall the torch library
        # pip uninstall torch torchvision torchaudio

    # Step 2: Install the torch library again
        # pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

    #Step 3: Run this code to check if the CUDA is available and the version of the torch library.

import torch

print("Torch version:", torch.__version__)
print("Is CUDA available:", torch.cuda.is_available())
print("CUDA Version:", torch.version.cuda)