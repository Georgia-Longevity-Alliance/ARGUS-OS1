"""Vision source for ARGUS (YOLO + CellPose) — computes SNR / metrics for
the MHS microscope driver and the exploration->compile loop (ground truth).

Runs on Jetson Orin NX / AGX. `report_snr()` gives a scalar signal-to-noise
ratio used for closed-loop autofocus / objective-cleaning triggers.
"""
from __future__ import annotations

import math
from typing import Any, Optional


class VisionSource:
    """Wraps a camera frame provider and detection models (CellPose/YOLO)."""

    def __init__(self, camera, detect: Optional[Any] = None):
        self.camera = camera          # object with .grab() -> np.ndarray (grayscale/int)
        self.detect = detect          # optional segmentation/detection model

    def grab_frame(self):
        return self.camera.grab()

    def signal_noise_ratio(self, frame=None, dark_region: Optional[tuple] = None) -> float:
        """Simple SNR: mean(signal) / std(noise). Falls back to frame statistics."""
        import numpy as np
        if frame is None:
            frame = np.asarray(self.grab_frame(), dtype=np.float64)
        if frame.ndim == 3:                 # RGB -> luminance
            frame = frame.mean(axis=2)
        if dark_region is not None:
            (y, x, h, w) = dark_region
            noise = frame[y:y + h, x:x + w]
            signal = np.delete(frame, np.s_[y:y + h], 0) if h else frame
        else:
            noise = frame
            signal = frame
        mu = float(signal.mean())
        sd = float(noise.std())
        return 0.0 if sd < 1e-9 else float(mu / max(sd, 1e-9))

    def mitosis(self, frame=None, min_conf: float = 0.5) -> list:
        """Trigger: 'mitosis complete' for sample exchange (V9 task #1)."""
        if self.detect is None:
            return []
        return self.detect(frame if frame is not None else self.grab_frame(),
                           min_conf=min_conf)

    def report_snr(self) -> float:
        return round(self.signal_noise_ratio(), 3)
