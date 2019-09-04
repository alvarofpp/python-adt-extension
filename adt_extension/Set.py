from typing import Any, Callable, Type


class Set(set):
    """Set with element type and validation rule for the elements
    that will be inserted into the set.
    """

    def __init__(self, seq=(), element_type: Type = None, rule: Callable[[Any], bool] = None):
        self.rule = rule  # Validation rule
        self.element_type = element_type  # Specifies element type
        super().__init__(seq)

    def add(self, *args, **kwargs):
        """Add an element to a set.
        """
        # Check validation rule and type elements exists
        if (len(args) > 1) or ((self.rule is None) and (self.element_type is None)):
            super(Set, self).add(*args)
        else:
            # Applies validation rule on argument
            if self._validate(args[0]):
                super(Set, self).add(*args)

    def update(self, *args, **kwargs):
        """Update a set with the union of itself and others.
        """
        # Check validation rule and type elements exists
        if (self.rule is None) and (self.element_type is None):
            super(Set, self).update(*args)
        else:
            # Applies validation rule on arguments
            validate_args = set()
            for arg in args[0]:
                if self._validate(arg):
                    validate_args.add(arg)

            if len(validate_args) == 0:
                pass

            super(Set, self).update(validate_args)

    def _validate(self, element: Any) -> bool:
        """Validate element.

        Return: bool
            True if elements satisfies element type and/or validation rule, False otherwise.
        """
        # Element that not satisfies the element type
        if (not self.element_type is None) and not isinstance(element, self.element_type):
            return False
        # Element does not meet the validation rule
        if (not self.rule is None) and (not self.rule(element)):
            return False

        return True
