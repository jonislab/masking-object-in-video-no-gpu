# masking-object-in-video
Rotoscoping or masking object in a video

# Video Matting Tool Installation Guide

A comprehensive tool for video matting using RobustVideoMatting (RVM). Follow these simple steps to set up and run the script on your system.

## Prerequisites
Before you begin, ensure you have **Python 3.8+** installed on your computer.

---

### Step 1: Download or Clone the Repository
Click the green **Code** button at the top right of this GitHub page, select **Download ZIP**, and extract the files to a folder on your computer.

---

### Step 2: Install Dependencies (Choose CPU or CUDA/GPU)
Open your terminal (Mac/Linux) or Command Prompt / PowerShell (Windows), navigate to your project folder, and choose **one** of the installation options below based on your hardware:

#### Option A: For NVIDIA GPU (CUDA) Users — *Recommended for Speed*
If you have a compatible NVIDIA graphics card, run the following commands to install PyTorch with GPU acceleration and the required libraries:
```bash
pip install torch torchvision torchaudio
pip install -r requirements.txt
```

#### Option B: For CPU-Only Users
If you are running on a standard CPU, use the CPU-specific PyTorch wheel index to ensure proper compatibility:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

---

### Step 3: Download the Pre-Trained Model
1. Download the **RVM MobileNetV3** model file (fastest for CPU/general use) from the official release page:
   👉 [Download rvm_mobilenetv3.pth](https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3.pth)
2. Save the downloaded `.pth` file directly inside your project folder (or your designated model path).

---

### Step 4: Install and Configure FFmpeg
This script requires FFmpeg to process video files. 

1. Download FFmpeg for Windows from the official build page: [Gyan.dev FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the downloaded ZIP file.
3. Open the extracted folder, find the **`bin`** folder (which contains `ffmpeg.exe`), and copy its file path.
4. Add it to your System PATH:
   * Press the Windows Search bar and type: **“Edit the system environment variables”**
   * Click the **Environment Variables** button at the bottom right.
   * Under "System variables", select `Path` and click **Edit**.
   * Click **New** and paste the path to your FFmpeg `bin` folder, then click **OK** on all windows to save.

### Additional notes
If you run into installation errors ask an AI for help, make sure to specify whether you are using a CPU-only system or have a GPU.

Please give a like to my videos and subscribe!
https://www.youtube.com/@jonislab


