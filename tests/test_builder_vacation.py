from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
VACATION_DIR = ROOT / "builder" / "vacation"
if str(VACATION_DIR) not in sys.path:
    sys.path.insert(0, str(VACATION_DIR))

from CityVacationBuilder import CityVacationBuilder
from OutdoorsVacationBuilder import OutdoorsVacationBuilder


class TestVacationBuilders(unittest.TestCase):
    def test_city_add_accommodation_1_and_event(self) -> None:
        builder = CityVacationBuilder()

        self.assertIs(builder, builder.addAccommodation_1())
        self.assertIs(builder, builder.addEvent("Magic"))

        vacation_str = str(builder.getVacation())
        self.assertIn("---- City Vacation Builder ----", vacation_str)
        self.assertIn("You're staying at Hotel", vacation_str)
        self.assertIn("See the Magic show", vacation_str)

    def test_city_add_accommodation_3_formats_reservation_and_room(self) -> None:
        builder = CityVacationBuilder()

        builder.addAccommodation_3("Grand", 2024, 1, 2, 3, 42)
        vacation_str = str(builder.getVacation())

        self.assertIn("You're staying at Grand", vacation_str)
        self.assertIn("arrival date: 2024-01-02 00:00:00", vacation_str)
        self.assertIn("staying for 3 nights", vacation_str)
        self.assertIn("in Room number 42", vacation_str)

    def test_outdoors_add_accommodation_2_and_event(self) -> None:
        builder = OutdoorsVacationBuilder()

        self.assertIs(builder, builder.addAccommodation_2("Camp Spot"))
        self.assertIs(builder, builder.addEvent("Canyon Trail"))

        vacation_str = str(builder.getVacation())
        self.assertIn("---- Outdoorsy Vacation Builder ----", vacation_str)
        self.assertIn("You're staying at Camp Spot", vacation_str)
        self.assertIn("Hike: Canyon Trail", vacation_str)

    def test_outdoors_add_accommodation_1_uses_default_tent(self) -> None:
        builder = OutdoorsVacationBuilder()

        builder.addAccommodation_1()
        vacation_str = str(builder.getVacation())

        self.assertIn("You're staying at Tent", vacation_str)

    def test_outdoors_add_accommodation_3_formats_reservation_and_site(self) -> None:
        builder = OutdoorsVacationBuilder()

        builder.addAccommodation_3("Forest Camp", 2024, 6, 7, 2, 18)
        vacation_str = str(builder.getVacation())

        self.assertIn("You're staying at Forest Camp", vacation_str)
        self.assertIn("arrival date: 2024-06-07 00:00:00", vacation_str)
        self.assertIn("staying for 2 nights", vacation_str)
        self.assertIn("in Site number 18", vacation_str)


if __name__ == "__main__":
    unittest.main()
