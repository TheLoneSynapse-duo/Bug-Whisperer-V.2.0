"""TEST: torch — RuntimeError when tensors and model are on different devices."""
import pytest

try:
    import torch
    import torch.nn as nn
except ImportError as exc:
    torch = None
    nn = None
    _TORCH_IMPORT_ERROR = exc


def test_torch_model_and_input_same_device() -> None:
    """A model and its input on the same device produce an output."""
    if torch is None:
        pytest.skip(f"torch not installed: {_TORCH_IMPORT_ERROR}")

    device = torch.device("cpu")
    model = nn.Linear(10, 1).to(device)
    x = torch.randn(4, 10, device=device)
    y = model(x)
    assert y.shape == (4, 1)


def test_torch_model_input_device_mismatch() -> None:
    """A model on one device and an input on another raises RuntimeError."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("torch CUDA not available — cannot reproduce device mismatch")

    model = nn.Linear(10, 1).to("cuda")
    x = torch.randn(4, 10)  # stays on CPU
    with pytest.raises(RuntimeError):
        model(x)
