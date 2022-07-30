from Zone import Zone
from ZoneCentral import ZoneCentral
from ZoneEastern import ZoneEastern
from ZoneMountain import ZoneMountain
from ZonePacific import ZonePacific


class ZoneFactory:
    def createZone(self, zoneId: str) -> Zone:
        zone: Zone = None
        if zoneId == "US/Pacific":
            zone = ZonePacific()
        elif zoneId == "US/Mountain":
            zone = ZoneMountain()
        elif zoneId == "US/Central":
            zone = ZoneCentral()
        elif zoneId == "US/Eastern":
            zone = ZoneEastern()
        return zone