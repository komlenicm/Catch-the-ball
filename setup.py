import cx_Freeze

executables = [cx_Freeze.Executable("primer.py")]

cx_Freeze.setup(

    name="Catch the ball!",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["ball2.jpg","paddle3.png"]}},

    executables = executables
)
