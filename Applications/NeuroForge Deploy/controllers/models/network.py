class Network:
    def __init__(self, name, architecture, config):
        self.name = name
        self.architecture = architecture
        self.config = config

    def deploy(self, target_platform):
        # Deploy network to target platform
        pass

def create_network(name, architecture, config):
    # Create a new neural network
    return Network(name, architecture, config)
