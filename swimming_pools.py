import numpy as np
import pandas as pd

from FilterUnit import FilterUnit
from filters import Filters
from modified_zeolites import ModifiedZeolites


class SwimmingPool:
    def __init__(self, volume, length, width, depth):
        self.volume = volume
        self.length = length
        self.width = width
        self.depth = depth
        self.temperature = 25
        self.ph_level = 7.0
        self.chlorine_level = 0.0
        self.filters = Filters()
        self.zeolites = ModifiedZeolites()
        self.filter_unit = FilterUnit()
        self.water_is_clean = False

    def water_purification(self, mode_choice=None):
        self.temperature = np.random.normal(25, 1)  # update temperature with a random value
        self.ph_level = np.random.normal(7.0, 0.1)  # update pH level with a random value
        self.chlorine_level = np.random.normal(0.5, 0.1)  # update chlorine level with a random value

        if not self.filter_unit.is_on():
            self.filter_unit.switch_mode("FILTRATION")

        if self.filter_unit.is_dirty:
            self.filter_unit.clean_filter()

        if self.zeolites.is_full:
            self.filter_unit.switch_mode("SAND COMPACTION")
            self.filter_unit.switch_mode("RECIRCULATION")
            self.zeolites.regenerate()
            self.filter_unit.switch_mode("FILTRATION")
            if mode_choice == "2":
                self.filter_unit.switch_mode("WASHING")
            elif mode_choice == "4":
                self.filter_unit.switch_mode("EMPTYING")
            elif mode_choice == "6":
                self.filter_unit.switch_mode("CLOSED")

        self.water_is_clean = True
        print("The water is now clean and ready for use.")

    def is_water_clean(self):
        return self.water_is_clean

    def pool_status(self):
        data = {
            'Temperature': [self.temperature],
            'pH Level': [self.ph_level],
            'Chlorine Level': [self.chlorine_level]
        }
        df = pd.DataFrame(data)

        print(df)

    def tap_modes(self, mode_choice=None):
        while True:
            print("\nTap modes:")
            print("1. Water purification")
            print("2. Pool status")
            print("3. Filter unit mode")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.water_purification()
            elif choice == "2":
                self.pool_status()
            elif choice == "3":
                print("\nFilter unit mode:")
                print("1. Filtration")
                print("2. Backwash")
                print("3. Rinse")
                print("4. Waste")
                print("5. Recirculation")
                print("6. Closed")
                mode_choice = input("Enter filter unit mode: ")
                if mode_choice == "1":
                    self.filter_unit.switch_mode("FILTRATION")
                elif mode_choice == "2":
                    self.filter_unit.switch_mode("BACKWASH")
                elif mode_choice == "3":
                    self.filter_unit.switch_mode("SAND COMPACTION")
                elif mode_choice == "4":
                    self.filter_unit.switch_mode("WASTE")
                elif mode_choice == "5":
                    self.filter_unit.switch_mode("RECIRCULATION")
                elif mode_choice == "6":
                    self.filter_unit.switch_mode("CLOSED")
                else:
                    print("Invalid filter unit mode. Try again.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    pool = SwimmingPool(100000, 50, 20, 2)
    pool.tap_modes()
