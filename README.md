# Application-of-multimodal-digitalhuman-synthesis
## Usage
- [x] **文本播报**
- [x] **数字人交互**
- [ ] **新闻播报**
- [ ] **数字人带货**
<div align=center>
  <img src="https://s2.loli.net/2024/06/02/sWr3HIxeJuOtLo9.gif" alt="obama gif" width="500">
</div>     

## 1 Install
Tested on Ubuntu 20.04, Python3.10, Pytorch 1.12 and CUDA 11.3
### 1.1 Clone the project
```bash
git clone https://github.com/Crossroadscodes/Realtime-digitalhuman-synthesis.git
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
## 2 Start
```bash
export HF_ENDPOINT=https://hf-mirror.com
python app.py --listenport 6006 --transport webrtc
```

