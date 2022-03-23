#!/usr/bin/env bash

cd godot
git fetch
git checkout groups-shared-4.x -f
git reset --hard origin/groups-shared-4.x
cd -