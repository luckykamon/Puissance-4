from cx_Freeze import setup, Executable
setup(
    name = "salut",
    version = "0.1",
    description = "Ceci est un puissance 4",
    executables = [Executable("puissance4.py")],
)
