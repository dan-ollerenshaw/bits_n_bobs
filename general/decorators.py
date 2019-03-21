class reduce_args():
    """ This is useful in the situation where:
        - we have a config file stored as a dict
        - we want to use this to pass parameters to functions, via **config
        - but we don't need all the parameters
        
        Standard behaviour is to throw a KeyError. By applying this
        decorator you can avoid it.
        
        Note: when applying this decorator, if all your arguments are in the
        config dict, you don't need to use any arguments when calling the
        decorated function. However, if the decorated function has arguments outside
        the config, you do need to specify them.
    """
    def __init__(self, config):
        self.config = config
    
    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            func_args = f.__code__.co_varnames
            config = {k:v for k,v in self.config.items() if k in func_args}
            return f(*args, **kwargs, **config)
        return wrapped_f
