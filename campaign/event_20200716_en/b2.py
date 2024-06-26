from campaign.event_20200716_en.b1 import Config as ConfigBase
from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

MAP = CampaignMap('B2')
MAP.camera_sight = (-4, -2, 4, 2)
MAP.shape = 'J8'
MAP.camera_data = ['D2', 'D6', 'G2', 'G6']
MAP.camera_data_spawn_point = []
MAP.map_data = """
    -- -- ++ ++ ++ ++ -- -- ++ ++
    MS -- MB ++ ++ ++ ME -- ++ ++
    -- Me -- -- ++ ++ MS __ -- --
    -- ++ ++ __ ++ ++ ME -- ME --
    Me -- ME -- -- ME -- -- -- SP
    MB -- -- -- -- __ -- ME -- SP
    Me -- ME Me ME -- -- ++ -- SP
    -- Me -- ++ ++ MS ME -- -- --
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, J7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, J8, \
    = MAP.flatten()


class Config(ConfigBase):
    MAP_SIREN_COUNT = 2


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True

        return self.battle_default()

    def battle_5(self):
        self.fleet_boss.capture_clear_boss()

