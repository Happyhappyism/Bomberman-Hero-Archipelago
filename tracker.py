from .Regions import region_data_table
from .Locations import location_data_table, radio_data_table, gem_data_table
import logging
#from .Rules import get_location_rules
logger = logging.getLogger("Tracker")

class trackerstate:
    def has(item, count=1):
        if count > 1:
            return f"{item}:{count}"
        else:
            return item
        
full_location_table = location_data_table | radio_data_table | gem_data_table

stage_coords = {
    "Planet Bomber": [80,280],
    # Bomber
    "Battle Room": [60, 90],
    "Hyper Room": [80, 100],
    "Secret Room": [40, 125],
    "Heavy Room": [90, 90],
    "Sky Room": [90, 80],

    "Blue Cave": [210, 55],
    "Hole Lake": [230, 70],
    "Red Cave": [205, 65],
    "Big Cannon": [175, 40],
    "Dark Wood": [175, 60],
    "Dragon Road": [200, 35],
    "Vs Nitros Planet Bomber": [240, 35],

    "Clown Valley": [215, 165],
    "Great Rock": [200, 135],
    "Fog Route": [230, 135],
    "Vs Endol": [260, 130],

    # Primus
    "Groog Hills": [340, 120],
    "Bubble Hole": [380, 125],
    "Erars Lake": [400, 115],
    "Waterway": [375, 95],
    "Water Slider": [405, 100],

    "Rockn Road": [500, 50],
    "Water Pool": [485, 45],
    "Millian Road": [525, 45],
    "Warp Room": [505, 70],
    "Dark Prison": [545, 60],
    "Vs Nitros Primus": [540, 30],

    "Killer Gate": [525, 165],
    "Spiral Tower": [565, 150],
    "Snake Route": [550, 135],
    "Vs Baruda": [555, 115],

    # Kanatia
    "Hades Crater": [40, 460],
    "Magma Lake": [25, 470],
    "Magma Dam": [90, 465],
    "Crysta Hole": [75, 460],
    "Emerald Tube": [90, 450],

    "Death Temple": [180, 415],
    "Death Road": [190, 410],
    "Death Garden": [200, 400],
    "Float Zone": [180, 385],
    "Aqua Tank": [220, 405],
    "Aqua Way": [225, 415],
    "Vs Nitros Kanatia": [230, 390],

    "Hard Coaster": [185, 520],
    "Dark Maze": [210, 505],
    "Mad Coaster": [255, 505],
    "Move Stone": [250, 485],
    "Vs Bolban": [210, 475],

    # Mazone
    "Hopper Land": [375, 475],
    "Junfalls": [380, 455],
    "Freeze Lake": [430, 475],
    "Cool Cave": [410, 460],

    "Snowland": [510, 415],
    "Storm Valley": [560, 420],
    "Snow Circuit": [535, 395],
    "Heaven Sky": [570, 395],
    "Eye Snake": [550, 370],

    "Vs Nitros Mazone": [590, 520],
    "Air Room": [550, 495],
    "Zero G Room": [570, 500],
    "Mirror Room": [600, 495],
    "Vs Natia": [575, 480],

    # Garaden
    "Boss Room 1": [235, 290],
    "Boss Room 2": [225, 300],
    "Boss Room 3": [235, 300],
    "Boss Room 4": [245, 300],
    "Boss Room 5": [245, 310],
    "Boss Room 6": [225, 310],
    "Vs Bagular": [235, 320],
}

location_rules = {
    "Heaven Sky Clear":
        lambda state: [state.has("Bombup")],
    "Heaven Sky Points":
        lambda state: [state.has("Bombup")],
    "Vs Endol Points":
        lambda state: [state.has("Fireup", 3)],
    "Vs Baruda Points":
        lambda state: [state.has("Bombup", 2)],
    "Vs Bolban Points":
        lambda state: [state.has("Fireup", 2)],
    "Vs Natia Clear":
        lambda state: [f"{state.has("Fireup", 3)}, {state.has("Healthup", 2)}"],
    "Vs Natia Points":
        lambda state: [f"{state.has("Fireup", 3)}, {state.has("Healthup", 2)}"],
    "Boss Room 2 Points":
        lambda state: [state.has("Fireup", 3)],
    "Boss Room 5 Clear":
        lambda state: [state.has("Bombup", 1)],
    "Boss Room 5 Points":
        lambda state: [state.has("Bombup", 2)],
    "Boss Room 6 Clear":
        lambda state: [state.has("Fireup", 3)],
    "Boss Room 6 Points":
        lambda state: [state.has("Fireup", 3)],
    "Aqua Way Points":
        lambda state: [state.has("Bombup")],
    "Freeze Lake Points":
        lambda state: [state.has("Bombup", 3)],
}

def gen_location_mapping():
    for location, data in full_location_table.items():
        logger.warning(f"[{hex(data.address)}] = {"{{"} '@{data.region}/{location}' {"}}"}")



def group_locations():
    region_groups = {}
    for stage, coords in stage_coords.items(): 
        region_groups[stage] = []
    for location, data in full_location_table.items():
        region_groups[data.region].append(location)
    return region_groups

def gen_item_json():
    item_json = []
    for stage, coords in stage_coords.items():
        entry_data = {}
        entry_data["name"] = stage
        entry_data["type"] = "toggle"
        entry_data["img"] = f"images/items/{stage.replace(" ","").lower()}.png"
        entry_data["codes"] = stage
        item_json.append(entry_data)
    return item_json

def populate_location_json():
    location_json = []
    #gen_location_mapping()
    region_groups = group_locations()
    special_stages = ["Planet Bomber","Battle Room","Vs Bagular"]
    for stage, coords in stage_coords.items():
        entry_data = {}
        entry_data["name"] = stage
        if stage in special_stages:
            if stage == "Vs Bagular":
                entry_data["access_rules"] = ["$get_adok_requirement"]
        else:
            entry_data["access_rules"] = [f"{stage}"]
        entry_data["map_locations"] = [{"map": "BomberNebula", "x": coords[0], "y": coords[1]}]
        entry_data["sections"] = []
        for location in region_groups[stage]:
            section_data = {}
            section_data["name"] = location
            section_data["item_count"] = 1
            loc_type = (full_location_table[location].type).lower()
            section_data["chest_unopened_img"] = f"images/chest/{loc_type}closed.png"
            section_data["chest_opened_img"] = f"images/chest/{loc_type}open.png"
            if loc_type == "radio":
                section_data["visibility_rules"] = ["Radiosanity"]
            elif loc_type == "crystal":
                crystal_total = location.split(" ")[1]
                section_data["visibility_rules"] = [f"Crystal Checks:{crystal_total}"]
            if location in location_rules:
                loc_rules = location_rules[location]
                section_data["access_rules"] = f"[{loc_rules(trackerstate)}]"
            entry_data["sections"].append(section_data)
        location_json.append(entry_data)
    return location_json