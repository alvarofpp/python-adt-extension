# adt-extension
<a href="https://pypi.org/project/adt-extension/">
  <img src="https://img.shields.io/pypi/v/adt-extension.svg" alt="latest release" />
</a>

Python abstract data structure (ADT) extension.

**Install**:
```bash
pip install adt-extension
```

**Import**:
```python
from adt_extension import SwitchDict
```

## Extensions
Currently the package have the ADT extensions:

| Class | Extension of | Description |
| ----- | ------------ | ----------- |
| `SwitchDict` | [`dict`](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries) | Dictionary with the possibility of behavior of a `switch case`. |


### SwitchDict
Dictionary with the possibility to perform a function or return a value when trying to access a nonexistent index in the dictionary class.

**Example**:
```python
from adt_extension import SwitchDict

# Same behavior of a normal dictionary
switch_dict = SwitchDict({
    'Apartament': 125,
    'House': 250,
    'Condominium': 300,
})

# Add default case
switch_dict.default_case = 999

# List example
properties_list = [
    'Apartament',
    'House',
    'Condominium',
    'Treehouse',
    'Hotel',
]

# Get values
properties_values = [ switch_dict[ x ] for x in properties_list ]
print(properties_values)
# Output:
# [ 125, 250, 300, 999, 999 ]

# Remove default case, becomes a normal dictionary
switch_dict.default_case = None
```
