#!/usr/bin/env python
import fire
import importlib
import pkgutil
def find_and_run_plugins(plugin_prefix):
    plugins = {}
    print("Searching for plugins:")
    for _,name,_ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module
    for name,module in plugins.items():
        print('Running plugins')
        module.run()
if __name__=='__main__':
    fire.Fire()
    
        
