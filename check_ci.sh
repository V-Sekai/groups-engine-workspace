./bin/godot.linuxbsd.double.tools.64.san --audio-driver Dummy -e -q --path test_project 2>&1 | tee sanitizers_log.txt || true
  misc/scripts/check_ci_log.py sanitizers_log.txt
