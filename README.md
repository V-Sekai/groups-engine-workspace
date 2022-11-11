# groups-workspace-fire

A workspace that gives a quick start to the V-Sekai Groups projects.

## Readme for fire

```
scoop install msys2
msys2
pacman -S git python3 ssh-pageant
# copy 
# eval $(/usr/bin/ssh-pageant -r -a "/tmp/.ssh-pageant-$USERNAME")
# export PATH=/mingw64/bin/:$PATH
# To the end of ~/.bashrc
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"
mkdir -p ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts
ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
```