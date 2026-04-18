import torch.nn as nn


class SkyCNN(nn.Module):
    """VGG-style CNN for predicting solar irradiance from sky images"""
    
    def __init__(self):
        super().__init__()
        
        # Convolutional blocks
        self.conv_block1 = self._conv_block(3, 32)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv_block2 = self._conv_block(32, 64)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv_block3 = self._conv_block(64, 128)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv_block4 = self._conv_block(128, 256)
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Adaptive pooling
        self.adaptive_pool = nn.AdaptiveAvgPool2d((7, 7))
        
        # Flatten
        self.flatten = nn.Flatten()
        
        # Fully connected layers
        self.classifier = nn.Sequential(
            nn.Linear(256 * 7 * 7, 1024),
            nn.ReLU(),
            nn.Linear(1024, 256),
            nn.ReLU(),
            nn.Linear(256, 1)
        )

    def _conv_block(self, in_channels, out_channels, kernel_size=3, padding=1):
        """Create a VGG-style convolutional block"""

        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size, padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size, padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        """Forward pass through the network"""

        x = self.pool1(self.conv_block1(x))
        x = self.pool2(self.conv_block2(x))
        x = self.pool3(self.conv_block3(x))
        x = self.pool4(self.conv_block4(x))
        
        x = self.adaptive_pool(x)
        x = self.flatten(x)
        x = self.classifier(x)
        
        return x
