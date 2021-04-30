# About
A Python script to glitch videos frame-by-frame with TotallyNotChase/glitch-this module.

# How it works
- Input video is stored in vid/ (video used in script is configurable in main.py)
- The script would first split the input video into different jpeg frames stored in temp/. It would then apply the glitch-this module to each split jpeg frame
and save the newly glitched frames in glitched_frames/. Finally, the glitched frames (as jpeg) would be re-assembled into a glitched video!

# Usage
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
