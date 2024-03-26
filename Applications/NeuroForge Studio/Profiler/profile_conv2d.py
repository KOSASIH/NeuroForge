layer_profiler_dict = {}

def profile_conv2d(module, name):
    def hook(module, input, output):
        layer_start_time[name] = time.time()

    layer_start_time = {}

    module.register_forward_hook(hook)

def profile_linear(module, name):
    def hook(module, input, output):
        layer_start_time[name] = time.time()

    layer_start_time = {}

    module.register_forward_hook(hook)
