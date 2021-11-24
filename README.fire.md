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
pacman -S mingw-w64-x86_64-git-lfs
export PATH=/mingw64/bin/:$PATH >> ~/.bashrc
```