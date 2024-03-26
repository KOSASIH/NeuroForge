import torch.nn as nn

# create a simple neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 16 * 6, 100)
        self.fc2 = nn.Linear(100, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 16 * 6)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

# create a model
model = Net()

# create a profiler
profiler = Profiler(model)

# start profiling
profiler.start()

# run the model
output = model(input)

# stop profiling
profiler.stop()

# profile the layers
profiler.profile_layers()
