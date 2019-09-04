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
from adt_extension import Set, SwitchDict
```

## Extensions
Currently the package have the ADT extensions:

| Class | Extension of | Description |
| ----- | ------------ | ----------- |
| `Set` | [`set`](https://docs.python.org/3.7/tutorial/datastructures.html#sets) | Set with element type and validation rule. |
| `SwitchDict` | [`dict`](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries) | Dictionary with the possibility of behavior of a `switch case`. |

### Set
Set with element type and validation rule for the elements that will be inserted into the set.

**Example**:
```python
from adt_extension import Set

# A set with only even integers
set_int_even = Set(element_type=int, rule=lambda x: (x % 2 == 0))

# Elements that satisfies the element type and validation rule
set_int_even.update({4, 6})
# Elements that satisfies the element type, but not validation rule
set_int_even.update({5})
# Elements that not satisfies the element type
set_int_even.update({"qwe", True})

print(set_int_even)
# Output:
# Set({4, 6})

# Remove element type
set_int_even.element_type = None
# Remove validation rule
set_int_even.rule = None
```

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
