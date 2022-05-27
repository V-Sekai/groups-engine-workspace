cd godot
scons bits=64 compiledb=yes vsproj=yes test=yes debug_symbols=no deprecated=no -j32 platform=windows bits=64 target=release_debug custom_modules=../godot-modules-groups