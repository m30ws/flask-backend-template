def loadfile(path, importname):
	""" """
	import importlib
	import importlib.spec
	import sys

	spec = importlib.util.spec_from_file_location(importname, path)
	module = importlib.util.module_from_spec(spec)
	sys.modules[spec.name] = module 
	spec.loader.exec_module(module)

	globals()[importname] = module # Add module to namespace