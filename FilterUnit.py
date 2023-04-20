import time


class FilterUnit:
    def __init__(self):
        self.mode = None
        self.is_dirty = False
        self.current_mode = None

    def __repr__(self):
        return f"FilterUnit(is_dirty={self.is_dirty}, current_mode={self.current_mode})"

    def switch_mode(self, mode):
        if self.current_mode == mode:
            print(f"Filter is already in {mode} mode.")
            return

        if mode == "FILTRATION":
            print("Starting filtration process...")
            self.current_mode = "FILTRATION"
        elif mode == "WASHING":
            print("Starting backwash process...")
            self.current_mode = "WASHING"
        elif mode == "SAND COMPACTION":
            print("Starting rinse process...")
            self.current_mode = "SAND COMPACTION"
        elif mode == "EMPTYING":
            print("Starting waste process...")
            self.current_mode = "EMPTYING"
        elif mode == "RECIRCULATION":
            print("Starting recirculation process...")
            self.current_mode = "RECIRCULATION"
        elif mode == "CLOSED":
            print("Closing filter...")
            self.current_mode = "CLOSED"
        else:
            print(f"{mode} is not a valid mode.")
            return

        self.is_dirty = True if mode != "FILTRATION" else False

    def clean_filter(self):
        if self.current_mode != "FILTRATION":
            print("Filter is not in filtration mode.")
            return

        print("Starting backwash...")
        # simulate backwash process
        time.sleep(180)
        print("Backwash complete.")

        print("Starting sand compaction...")
        # simulate sand compaction process
        time.sleep(30)
        print("Sand compaction complete.")

        print("Switching back to filtration mode...")
        self.is_dirty = False
        self.current_mode = "FILTRATION"
        print("Filter is now in filtration mode.")

        filter_unit = FilterUnit()
        filter_unit.switch_mode("FILTRATION")

    def is_on(self):
        pass


def filter_unit():
    return None
