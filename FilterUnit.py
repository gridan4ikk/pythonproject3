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
        elif mode == "BACKWASH":
            print("Starting backwash process...")
            self.current_mode = "BACKWASH"
        elif mode == "RINSE":
            print("Starting rinse process...")
            self.current_mode = "RINSE"
        elif mode == "WASTE":
            print("Starting waste process...")
            self.current_mode = "WASTE"
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

        print("Starting rinse...")
        # simulate sand compaction process
        time.sleep(30)
        print("Rinse complete.")

        print("Switching back to filtration mode...")
        self.is_dirty = False
        self.current_mode = "FILTRATION"
        print("Filter is now in filtration mode.")

        local_filter_unit = FilterUnit()
        local_filter_unit.switch_mode("FILTRATION")

    def is_on(self):
        pass


def filter_unit():
    return None
