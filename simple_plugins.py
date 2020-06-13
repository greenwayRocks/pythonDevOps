#!/usr/bin/env python3

import fire
import pkgutil
import importlib

def run_plugins(prefix):
    plugins = {}

    # Discover and Load Plugins
    print(f'Discovering plugin with prefix: {prefix}')
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    # Run plugins
    for name, module in plugins.items():
        print(f'Running plugin {name}')
        module.run()

if __name__ == '__main__':
    fire.Fire()
