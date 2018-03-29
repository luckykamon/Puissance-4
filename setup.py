from cx_Freeze import setup, Executable
setup(
    name = "salut",
    version = "0.1",
    description = "Ce programme vous dit bonjour",
    executables = [Executable("salut.py")],
)
