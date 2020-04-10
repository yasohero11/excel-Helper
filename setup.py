from cx_Freeze import setup , Executable


setup(
    name = "main",
    version='0.1',
    description="as asdas",
    executables = [Executable("main.py",icon = "excel.ico")] 
)