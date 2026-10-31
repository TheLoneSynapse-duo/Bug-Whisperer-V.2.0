#!/usr/bin/env python3
"""DEMO: TensorFlow mistake — passing a tf.constant with incompatible shapes.

Run with:
    .\run.bat demos\demo_tensorflow.py

NOTE: This demo requires TensorFlow installed.
If you see ModuleNotFoundError, run: pip install tensorflow
"""
import tensorflow as tf

# WRONG (tf.errors.InvalidArgumentError / ValueError at graph execution):
# Two constants with incompatible shapes cannot be added.
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([1, 2, 3])
result = a + b
print("Result:", result)
