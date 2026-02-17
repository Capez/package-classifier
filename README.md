# package-classifier

Sorts packages into STANDARD / SPECIAL / REJECTED based on volume (W×H×L), max dimension 150cm, and mass 20kg. See problem description for exact rules.

**Usage:** dimensions in cm, mass in kg.

```python
from classifier import sort
sort(10, 10, 10, 5)   # STANDARD
sort(100, 100, 100, 20)   # REJECTED
```

**Tests:** `pip install pytest` then `python -m pytest tests/ -v` (run from project root)
