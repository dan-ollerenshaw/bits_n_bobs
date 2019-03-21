class reduce_args():
    """ This is useful in the situation where:
        - we have a config file stored as a dict
        - we want to use this to pass parameters to functions, via **config
        - but we don't need all the parameters
        
        Standard behaviour is to throw a KeyError. By applying this
        decorator you can avoid it.
        
        Note: when applying this decorator, you should pass in the config
        dict as an argument, notthe unpacked **config.
    """
    def __init__(self, config):
        self.config = config
    
    def __call__(self, f):
        def wrapped_f(*args):
            func_args = f.__code__.co_varnames
            config = {k:v for k,v in self.config.items() if k in func_args}
            return f(**config)
        return wrapped_f