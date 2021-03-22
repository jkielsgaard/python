Small python engine to run a python setup in 3 steps.
1. `api.py` - flask api webserver
2. `engine.py` - run all python files in PyFiles folder
3. `PyFiles` (folder) - Python code to make API calls

This setup is build to modified python file in the PyFiles folder when the system is running

how to start it
1. Run `api.py` 
2. Run `engine.py`
3. edit files in `PyFiles` folder to call API on flask server.

The python in `PyFiles` folder will be exec every 5 sec, can be modified in the `engine.py` script