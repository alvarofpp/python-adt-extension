class Set(set):
    """Set with validation rule for the elements that will be inserted
    into the set.
    """

    def __init__(self, seq=(), rule=None):
        self.rule = rule
        super().__init__(seq)
