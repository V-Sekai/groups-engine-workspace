# Readm for fire

Use push instead of to get the git repos.

```
git config --global url.git@github.com:fire.pushInsteadOf https://github.com/fire
git config --global url.git@github.com:godot-extended-libraries.pushInsteadOf https://github.com/godot-extended-libraries
git config --global url.git@gitlab.com:.insteadOf https://gitlab.com/
git config --global url.git@gitlab.com:SaracenOne.pushInsteadOf https://gitlab.com/SaracenOne
```

```
ssh-keyscan github.com >> ~/.ssh/known_hosts
ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
```

```
sudo yum install -y scons pkgconfig libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel \
libXi-devel mesa-libGL-devel mesa-libGLU-devel alsa-lib-devel pulseaudio-libs-devel \
libudev-devel yasm gcc-c++ libstdc++-static libatomic-static
```

```
pacman -S mingw-w64-x86_64-git-lfs
export PATH=/mingw64/bin/:$PATH >> ~/.bashrc
```

## Visual Studio Code Extensions

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

dnf check-update
sudo dnf install code

1. cpp
1. clangd
1. prettier
1. codelldb

## Fedora Silverblue

rpm-ostree install scons pkgconfig libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel     libXi-devel mesa-libGL-devel mesa-libGLU-devel alsa-lib-devel pulseaudio-libs-devel libudev-devel yasm gcc-c++ libstdc++-static libatomic-static clang

## Pop OS!

sudo apt-get install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev \
    libgl1-mesa-dev libglu-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev yasm ninja-build ccache clang lldb lld
