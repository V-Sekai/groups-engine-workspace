# Readme for fire

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
libudev-devel yasm gcc-c++ libstdc++-static libatomic-static clang ccache clang-tools-extra
```

```
pacman -S mingw-w64-x86_64-git-lfs
export PATH=/mingw64/bin/:$PATH >> ~/.bashrc
```

## Pop OS!

sudo apt-get install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev \
    libgl1-mesa-dev libglu-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev yasm ninja-build ccache clang lldb lld

## Keep branches in submodules

```
# https://stackoverflow.com/questions/1777854/how-can-i-specify-a-branch-tag-when-adding-a-git-submodule
git submodule foreach -q --recursive 'branch="$(git config -f $toplevel/.gitmodules submodule.$name.branch)"; git switch $branch'
```
