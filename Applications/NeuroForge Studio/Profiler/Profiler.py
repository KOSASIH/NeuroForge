import time
import torch

class Profiler:
    def __init__(self, model):
        self.model = model

    def start(self, layer_name=None):
        if layer_name is not None:
            self.layer_start_time = {}
            self.layer_name = layer_name

    def stop(self):
        if self.layer_start_time:
            layer_times = [self.layer_start_time[name] for name in self.layer_name]
            print(f"Layer execution times (ms): {layer_times}")

    def profile_layers(self):
        if isinstance(self.model, torch.nn.Module):
            for name, module in self.model.named_modules():
                if module.__class__.__name__ in layer_profiler_dict:
                    layer_profiler_dict[module.__class__.__name__](module, name)
        else:
            print("Model is not an instance of torch.nn.Module")
