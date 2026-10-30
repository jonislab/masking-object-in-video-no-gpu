import os
import sys
import cv2
import torch
import numpy as np
from pathlib import Path
from PIL import Image
import time

# -------- CONFIG --------
VIDEO_INPUT = r"D:\\vidproject1\\myvid.mp4"
OUTPUT_DIR = r"D:\\vidproject1"

# RVM paths, replace this with your own RVM folder
RVM_PATH = r"C:\j\d\py\projects\rotoscope\RVM"
MODEL_PATH = r"C:\j\d\py\projects\rotoscope\RVM\pretrained\rvm_mobilenetv3.pth"

# Add RVM to Python path
sys.path.append(RVM_PATH)
from model import MattingNetwork


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def run_rvm_on_video(video_path, output_dir):
    ensure_dir(output_dir)

    print("Loading RVM model...")
    model = MattingNetwork("mobilenetv3").eval()
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

    rec = [None, None, None, None]

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Cannot open video file.")

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Processing {frame_count} frames...")

    idx = 0
    while True:
        ret, frame_bgr = cap.read()
        if not ret:
            break

        idx += 1
        print(f"[{idx}/{frame_count}] Processing frame...")

        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame_rgb)

        # Prepare tensor
        src = torch.from_numpy(np.array(frame_pil)).float() / 255.0
        src = src.permute(2, 0, 1).unsqueeze(0)

        with torch.no_grad():
            fgr, pha, *rec = model(src, *rec)

        fgr = fgr[0].permute(1, 2, 0).numpy()
        pha = pha[0].permute(1, 2, 0).numpy()

        cutout = np.dstack((fgr, pha))
        cutout_img = Image.fromarray((cutout * 255).astype(np.uint8))

        out_path = os.path.join(output_dir, f"frame_{idx:05d}.png")
        cutout_img.save(out_path)

    cap.release()
    print("RVM frame extraction complete.")


def main():
    run_rvm_on_video(VIDEO_INPUT, OUTPUT_DIR)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    print(f"Total runtime: {minutes} minutes {seconds} seconds")
