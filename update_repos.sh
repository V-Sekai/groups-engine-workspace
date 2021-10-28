cd godot
git fetch
git checkout groups-4.x -f
git fetch
git reset --hard origin/groups-4.x
# find . -type d -exec bash -c 'cd "$0" && (`ls .git 2>/dev/null`) || (pwd && git lfs pull)' {} \;
cd -