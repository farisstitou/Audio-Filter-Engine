import numpy as np

def low_pass(cutoff):
    def filter_function(freq_axis):
        return (np.abs(freq_axis) < cutoff).astype(float)
    return filter_function

def high_pass(cutoff):
    def filter_function(freq_axis):
        return (np.abs(freq_axis) > cutoff).astype(float)
    return filter_function