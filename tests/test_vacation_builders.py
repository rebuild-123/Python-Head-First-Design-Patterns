import os
import sys
import unittest

VACATION_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "builder", "vacation")
)
if VACATION_DIR not in sys.path:
    sys.path.insert(0, VACATION_DIR)

from CityVacationBuilder import CityVacationBuilder
from OutdoorsVacationBuilder import OutdoorsVacationBuilder


class VacationBuilderTests(unittest.TestCase):
    def test_outdoors_add_accommodation_1_uses_default_tent(self) -> None:
        builder = OutdoorsVacationBuilder()

        builder.addAccommodation_1()

        self.assertEqual(1, len(builder.accommodations))
        self.assertEqual("You're staying at Tent\n", builder.accommodations[0])

    def test_outdoors_add_accommodation_3_includes_reservation_and_location(self) -> None:
        builder = OutdoorsVacationBuilder()

        builder.addAccommodation_3("Canvas Tent", 2026, 4, 11, 2, 7)

        accommodation_text = builder.accommodations[0]
        self.assertIn("You're staying at Canvas Tent", accommodation_text)
        self.assertIn("2026-04-11", accommodation_text)
        self.assertIn("staying for 2 nights", accommodation_text)
        self.assertIn("Site number 7", accommodation_text)

    def test_city_builder_get_vacation_preserves_expected_output(self) -> None:
        builder = CityVacationBuilder()
        builder.addAccommodation_2("Downtown Hotel")
        builder.addEvent("Broadway")

        vacation = builder.getVacation()

        self.assertEqual("City Vacation Builder", vacation.name)
        self.assertEqual(1, len(vacation.accommodations))
        self.assertIn("You're staying at Downtown Hotel", vacation.accommodations[0])
        self.assertIn("See the Broadway show", str(vacation))


if __name__ == "__main__":
    unittest.main()
