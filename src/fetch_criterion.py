
from importlib import import_module

def fetch_criterion(name):
    criterion = import_module(f"src.criteria.evaluate_{name.replace(' ', '_')}")
    
    return getattr(criterion, f"evaluate_{name.replace(' ', '_')}")
