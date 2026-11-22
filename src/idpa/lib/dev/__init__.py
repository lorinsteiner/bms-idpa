import importlib.util

IS_DEV = importlib.util.find_spec("pytest") is not None
