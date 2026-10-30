# masking-object-in-video
Rotoscoping or masking object in a video
// Python Modules

pip install rembg
pip install opencv-python
pip install pillow
pip install numpy

// To install pytorch on CPU only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

// To install python with GPU
pip install torch torchvision torchaudio

RVM MobileNetV3 (fastest for CPU)

https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3.pth 

// To install on PC with GPU
pip install rvm
rvm download


// Download the pre-train Model
RVM MobileNetV3 (fastest for CPU)

https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3.pth 

Save model on our chosen path.


// FFMPEG
Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/
Extract the ZIP
Copy the bin folder path (contains ffmpeg.exe)
Add it to System PATH
Windows Search → “Edit the system environment variables”
Environment Variables → PATH → Add new → paste the bin folder path

// Verify
ffmpeg -version

// Additional notes
If you run into installation errors ask an AI for help, make sure to specify whether you are using a CPU-only system or have a GPU.

Please give a like to my videos and subscribe!
https://www.youtube.com/@jonislab
