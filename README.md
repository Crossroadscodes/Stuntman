# Application-of-multimodal-digitalhuman-synthesis
## Usage
- [x] **特定文本播报**
- [ ] **数字人交互**
- [ ] **新闻播报**
- [ ] **数字人带货**
## Install
Tested on Ubuntu 20.04, Python3.10, Pytorch 1.12 and CUDA 11.3
### 1.1 Clone the project
```bash
git clonehttps://github.com/Crossroadscodes/Application-of-multimodal-digitalhuman-synthesis.git
cd Application-of-multimodal-digitalhuman-synthesis
```
### 1.2 Install dependency
```bash
conda create -n nerfstream python=3.10
conda activate nerfstream
conda install pytorch==1.12.1 torchvision==0.13.1 cudatoolkit=11.3 -c pytorch
pip install -r requirements.txt
pip install "git+https://github.com/facebookresearch/pytorch3d.git"
pip install tensorflow-gpu==2.8.0
pip install --upgrade "protobuf<=3.20.1"
```
## Start
```bash
export HF_ENDPOINT=https://hf-mirror.com
python app.py --listenport 6006 --transport webrtc
```

