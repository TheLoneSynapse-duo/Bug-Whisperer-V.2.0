#!/usr/bin/env python3
"""DEMO: PyTorch mistake — moving a model to a device but leaving tensors on CPU.

Run with:
    .\run.bat demos\demo_torch.py

NOTE: This demo requires PyTorch installed.
If you see ModuleNotFoundError, run: pip install torch
"""
import torch
import torch.nn as nn

model = nn.Linear(10, 1)

# WRONG (RuntimeError: Expected all tensors to be on the same device):
# The model is on cuda (if available) but the input tensor is still on CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

x = torch.randn(4, 10)
y = model(x)
print("Output shape:", y.shape)
