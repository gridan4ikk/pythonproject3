class Filters:
    def __init__(self):
        self.is_dirty = True

    def clean(self):
        self.is_dirty = False
        print("Filters have been cleaned.")

    def is_dirty(self):
        return self.is_dirty

    def is_clean(self):
        return not self.is_dirty

    def __repr__(self):
        return f"Filters(is_dirty={self.is_dirty})"
