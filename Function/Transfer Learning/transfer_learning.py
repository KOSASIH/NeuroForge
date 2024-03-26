import torch
from torch import nn
from torch.optim import Adam
from torchvision import datasets, transforms

def transfer_learning(model, num_classes, pretrained_model_path, learning_rate=0.001):
    """
    Function to perform transfer learning using a pre-trained model.
    
    Parameters:
    model (nn.Module): The neural network model to be trained.
    num_classes (int): The number of classes in the target dataset.
    pretrained_model_path (str): The path to the pre-trained model.
    learning_rate (float): The learning rate for the optimizer.
    
    Returns:
    model (nn.Module): The trained model with transfer learning.
    """
    # Load the pre-trained model
    pretrained_model = torch.load(pretrained_model_path)
    
    # Remove the last layer of the pre-trained model
    pretrained_model.fc = nn.Linear(pretrained_model.fc.in_features, num_classes)
    
    # Set the model to evaluation mode
    pretrained_model.eval()
    
    # Create a new optimizer for the model
    optimizer = Adam(model.parameters(), lr=learning_rate)
    
    # Train the model using transfer learning
    for epoch in range(10):  # Number of epochs
        for inputs, targets in dataloader:
            optimizer.zero_grad()
            
            outputs = model(inputs)
            loss = nn.functional.cross_entropy(outputs, targets)
            
            loss.backward()
            optimizer.step()
    
    return model
