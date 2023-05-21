from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Python Calculator",
    options = options,
    version = "1.0",
    description = 'Python Calculator',
    executables = executables
)