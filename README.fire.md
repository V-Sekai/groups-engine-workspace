# Readme for fire

Use push instead of to get the git repos.

```
pacman -S mingw-w64-x86_64-git-lfs git python3 ssh-pageant
eval $(/usr/bin/ssh-pageant -r -a "/tmp/.ssh-pageant-$USERNAME") >> ~/.bashrc
export PATH=/mingw64/bin/:$PATH >> ~/.bashrc
git config --global url.git@github.com:fire.pushInsteadOf https://github.com/fire
git config --global url.git@github.com:godot-extended-libraries.pushInsteadOf https://github.com/godot-extended-libraries
git config --global url.git@gitlab.com:.insteadOf https://gitlab.com/
git config --global url.git@gitlab.com:SaracenOne.pushInsteadOf https://gitlab.com/SaracenOne
ssh-keyscan github.com >> ~/.ssh/known_hosts
ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
```

## Fedora OS

```
sudo yum install -y scons pkgconfig libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel \
libXi-devel mesa-libGL-devel mesa-libGLU-devel alsa-lib-devel pulseaudio-libs-devel \
libudev-devel yasm gcc-c++ libstdc++-static libatomic-static clang ccache clang-tools-extra lld dos2unix recode libasan-static libasan libubsan-static
```

## Pop OS!

```
sudo apt-get install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev \
    libgl1-mesa-dev libglu-dev libasound2-dev libpulse-dev libudev-dev libxi-dev libxrandr-dev yasm ninja-build ccache clang lldb lld libxt-dev
```

Install codelldb in visual studio code.

### Msys2 Windows

```
# install scoop
scoop bucket add dorado https://github.com/chawyehsu/dorado
scoop install llvm-mingw msys2
pacman -S ssh-pageant openssh git python3
notepad ~/.bashrc
# eval $(/usr/bin/ssh-pageant -r -a "/tmp/.ssh-pageant-$USERNAME")
source ~/.bashrc
sh ./update_godot_v_sekai.sh
cd ..
git clone https://github.com/V-Sekai/groups-workspace-fire workspace
cd workspace
./update_repos.sh
# Open visual studio code on workspace.
# Start a build.
# Go to https://github.com/V-Sekai/godot and update the master branch using the Github ui.
```