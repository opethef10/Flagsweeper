import sys
import pkgutil
from cx_Freeze import setup, Executable

sys.argv.append("build")
# sys.argv.append("bdist_msi")

INCLUDES = [
    "collections", "encodings", "importlib", "urllib", 
    "pygame", "pygame.locals", "importlib.resources", "scenes"
]
EXCLUDES = list({module.name for module in list(pkgutil.iter_modules()) if module.ispkg} - set(INCLUDES))
EXCLUDES.extend(
    [
        "_queue", "_bz2", "_hashlib", "_lzma", "_socket", "select",
        'asyncio', 'concurrent', 'ctypes', 'distutils', 'email', 'html',
        'http', 'lib2to3', 'logging', 'multiprocessing', 'pkg_resources',
        'pydoc_data', 'test', 'unittest', 'xml', 'xmlrpc',"PyQt4",
        "PyQt5", 'matplotlib', "numpy", "tkinter", "Tkinter"
    ]
)

_executables = [
    Executable(
        script = "__main__.py", 
        target_name = "Flagsweeper.exe", 
        shortcut_name = "Flagsweeper",
        shortcut_dir = "DesktopFolder",
        icon = "resources\icon.ico",
        base = "Win32GUI",
    )
]

_build_exe_options = dict(
    build_exe = "Flagsweeper v0.4.2.1",
    packages = [],
    include_files =  ["resources"],
    zip_include_packages = ["*"],
    zip_exclude_packages = [],
    includes = INCLUDES,
    excludes = EXCLUDES,
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
