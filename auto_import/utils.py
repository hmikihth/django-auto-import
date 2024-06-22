import importlib
import os
import sys

def import_dir(package_name):
    """
    Imports all modules from the given package directory into the current module's namespace.
    
    :param package_name: The name of the package to import modules from
    """
    # Get the package's module object
    package = importlib.import_module(package_name)
    
    # Get the package's directory path
    package_directory = os.path.dirname(package.__file__)
    
    # Iterate through all Python files in the directory
    for file_name in os.listdir(package_directory):
        # Exclude __init__.py and any non-Python files
        if file_name.endswith('.py') and file_name != '__init__.py':
            # Construct the module name
            module_name = f"{package_name}.{file_name[:-3]}"  # Remove the .py extension
            
            try:
                # Try to import the module dynamically
                module = importlib.import_module(module_name)
                
                # Import all symbols from the module to the caller's namespace
                caller_globals = sys.modules[package_name].__dict__
                caller_globals.update({name: getattr(module, name) for name in module.__dict__ if not name.startswith('__')})
                
            except ModuleNotFoundError:
                print(f"Module {module_name} not found.")
                continue
