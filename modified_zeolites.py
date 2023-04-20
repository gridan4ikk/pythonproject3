class ModifiedZeolites:
    """Class for modified zeolites."""

    def __init__(self):
        """Initialize the object."""
        self.capacity = 100
        self._is_full = True

    def regenerate(self):
        """Regenerate the zeolites."""
        self._is_full = False
        print("Modified zeolites have been regenerated.")

    @property
    def is_full(self):
        """Check if the zeolites are full."""
        return self._is_full

    @is_full.setter
    def is_full(self, value):
        self._is_full = value

    def __repr__(self):
        return f"ModifiedZeolites(capacity={self.capacity}, is_full={self.is_full})"
