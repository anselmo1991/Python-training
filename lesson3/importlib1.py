import importlib

def get_package_path(setup):
    loader = importlib.find_loader(setup)
    if loader is None:
        return "Package not found"
    else:
        return loader.path


print(get_package_path('setup'))
