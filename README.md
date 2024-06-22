# django-auto-import

The **import_dir** function allows you to dynamically import all Python modules from a specified directory into the namespace of the current module. This is particularly useful in Django projects to streamline the import process across multiple directories like serializers, views, viewsets, etc.

## USAGE

In each directory where you want to dynamically import modules (e.g., serializers, viewsets), modify or create an **\_\_init\_\_.py** file. Use the **import_dir** function to automate the module imports.

For example:

```
# backend/serializers/__init__.py

from auto_import.utils import import_dir

import_dir(__name__)
```

```
# backend/viewsets/__init__.py

from auto_import.utils import import_dir

import_dir(__name__)
```

## Summary

Using the **import_dir** function simplifies and automates the process of importing modules within your Django project, reducing boilerplate code and ensuring a more organized codebase. This approach enhances maintainability and readability by centralizing import logic for directories containing multiple modules.
