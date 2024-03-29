class SwitchDict(dict):
    """Dictionary with the possibility to perform a function or return a
    value when trying to access a nonexistent index in the dictionary class.
    """

    def __init__(self, seq=None, **kwargs):
        self.default_case = None  # Switch default case

        # Case "switch_dict = SwitchDict()"
        if seq is None:
            seq = {}

        super().__init__(seq, **kwargs)

    def __getitem__(self, index):
        """ x.__getitem__(y) <==> x[y] """
        try:
            return super(SwitchDict, self).__getitem__(index)
        except KeyError as err:
            if self.default_case is None:
                raise err
            return self.default_case
