git pull --recurse-submodules
cd godot
git reset --hard origin/groups-4.x
cd -
git add godot
git commit -m "Updated Godot submodule."
git push