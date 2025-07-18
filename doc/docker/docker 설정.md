# Ubuntu 에서 Docker 설치 및 설정

---

## Docker 설치 및 권한 설정

```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
sudo newgrp docker
```

- `sudo systemctl status docker` : docker 상태 확인

## VsCode 확장 설치

- Docker DX (Docker)
- Docker (Microsoft)
- Dev Containers (Microsoft)
- docker 탭에서 오류 메세지 확인

## Docker image 다운로드

```bash
docker pull osrf/ros:noetic-desktop-full
```

## GUI 설정

- X11 설정
  - login 화면에서 Xorg로 실행
- xhost 권한 설정

```bash
xhost +local:
```

## Docker container 실행

- gpu 없을때.
```bash
docker run -it -d --name ros1_noetic --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --net=host osrf/ros:noetic-desktop-full
```

- gpu 있을때.
  -host
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |     sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |     sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

```

```bash
docker run -it \
  --name=linux_gui_r1 \
  --env="DISPLAY=$DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume="/usr/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:ro" \
  --device=/dev/nvidia0:/dev/nvidia0 \
  --device=/dev/nvidia-modeset:/dev/nvidia-modeset \
  --ipc=host \
  --net=host \
  --runtime=nvidia \
  --env="NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,display" \
  osrf/ros:noetic-desktop-full \
  bash
```

## dev container 실행

- Vscode 의 container 탭에서 만들어진 container 에서 Attach VsCode Studio Code 클릭
