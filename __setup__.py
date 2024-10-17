import sys
import pkgutil
from cx_Freeze import setup, Executable

# sys.argv.append("build")
# sys.argv.append("bdist_msi")

_executables = [
    Executable(
        script = "__main__.py",
        target_name = "Flagsweeper.exe",
        shortcut_name = "Flagsweeper",
        shortcut_dir = "DesktopFolder",
        icon = "resources\icon.ico",
        base = "Win32GUI"
    )
]

_build_exe_options = dict(
    build_exe = "Flagsweeper v0.4.2.1",
    packages = [],
    include_files =  ["resources"],
    zip_include_packages = ["*"],
    zip_exclude_packages = [],
    replace_paths = [("*", "")],
    optimize = 2,
    include_msvcr = True,
    silent = False,
)

setup(
    name = "Flagsweeper",
    version = "0.4.2.1",
    description = "Flagsweeper",
    options = {"build_exe": _build_exe_options},
    executables = _executables
)

