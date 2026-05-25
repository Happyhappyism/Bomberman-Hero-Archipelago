from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import BombHWorld

stage_names = [
    #"Battle Room",
    "Hyper Room",
    "Secret Room",
    "Heavy Room",
    "Sky Room",

    "Blue Cave",
    "Hole Lake",
    "Red Cave",
    "Big Cannon",
    "Dark Wood",
    "Dragon Road",
    "Vs Nitros Planet Bomber",

    "Clown Valley",
    "Great Rock",
    "Fog Route",
    "Vs Endol",

    "Groog Hills",
    "Bubble Hole",
    "Erars Lake",
    "Waterway",
    "Water Slider",

    "Rockn Road",
    "Water Pool",
    "Millian Road",
    "Warp Room",
    "Dark Prison",
    "Vs Nitros Primus",

    "Killer Gate",
    "Spiral Tower",
    "Snake Route",
    "Vs Baruda",

    "Hades Crater",
    "Magma Lake",
    "Magma Dam",
    "Crysta Hole",
    "Emerald Tube",

    "Death Temple",
    "Death Road",
    "Death Garden",
    "Float Zone",
    "Aqua Tank",
    "Aqua Way",
    "Vs Nitros Kanatia",

    "Hard Coaster",
    "Dark Maze",
    "Mad Coaster",
    "Move Stone",
    "Vs Bolban",

    "Hopper Land",
    "Junfalls",
    "Freeze Lake",
    "Cool Cave",
    "Snowland",

    "Storm Valley",
    "Snow Circuit",
    "Heaven Sky",
    "Eye Snake",

    "Vs Nitros Mazone",
    "Air Room",
    "Zero G Room",
    "Mirror Room",
    "Vs Natia",

    "Boss Room 1",
    "Boss Room 2",
    "Boss Room 3",
    "Boss Room 4",
    "Boss Room 5",
    "Boss Room 6",
    #"Vs Bagular",

    #"Outter Road",
    #"Inner Road",
    #"Vs Evil Bomber",

]


class BombHLocation(Location):
    game = "Bomberman Hero"


class BombHLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["BombHWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None
    type: Optional[str] = None




location_data_table: Dict[str, BombHLocationData] = {
 
    "Battle Room Clear": BombHLocationData(
        region="Battle Room",
        address=0x1348088,
        type= "Clear"
    ),
    "Hyper Room Clear": BombHLocationData(
        region="Hyper Room",
        address=0x1348098,
        type= "Clear"
    ),
    "Secret Room Clear": BombHLocationData(
        region="Secret Room",
        address=0x13480A8,
        type= "Clear"
    ),
    "Heavy Room Clear": BombHLocationData(
        region="Heavy Room",
        address=0x13480B8,
        type= "Clear"
    ),
    "Sky Room Clear": BombHLocationData(
        region="Sky Room",
        address=0x13480C8,
        type= "Clear"
    ),

    "Blue Cave Clear": BombHLocationData(
        region="Blue Cave",
        address=0x13480F8,
        type= "Clear"
    ),
    "Hole Lake Clear": BombHLocationData(
        region="Hole Lake",
        address=0x1348108,
        type= "Clear"
    ),
    "Red Cave Clear": BombHLocationData(
        region="Red Cave",
        address=0x1348118,
        type= "Clear"
    ),
    "Big Cannon Clear": BombHLocationData(
        region="Big Cannon",
        address=0x1348128,
        type= "Clear"
    ),
    "Dark Wood Clear": BombHLocationData(
        region="Dark Wood",
        address=0x1348138,
        type= "Clear"
    ),
    "Dragon Road Clear": BombHLocationData(
        region="Dragon Road",
        address=0x1348148,
        type= "Clear"
    ),
    "Vs Nitros Planet Bomber Clear": BombHLocationData(
        region="Vs Nitros Planet Bomber",
        address=0x1348158,
        type= "Clear"
    ),

    "Clown Valley Clear": BombHLocationData(
        region="Clown Valley",
        address=0x1348168,
        type= "Clear"
    ),
    "Great Rock Clear": BombHLocationData(
        region="Great Rock",
        address=0x1348178,
        type= "Clear"
    ),
    "Fog Route Clear": BombHLocationData(
        region="Fog Route",
        address=0x1348188,
        type= "Clear"
    ),
    "Vs Endol Clear": BombHLocationData(
        region="Vs Endol",
        address=0x1348198,
        type= "Clear"
    ),

    # Primus
    "Groog Hills Clear": BombHLocationData(
        region="Groog Hills",
        address=0x13481D8,
        type= "Clear"
    ),
    "Bubble Hole Clear": BombHLocationData(
        region="Bubble Hole",
        address=0x13481E8,
        type= "Clear"
    ),
    "Erars Lake Clear": BombHLocationData(
        region="Erars Lake",
        address=0x13481F8,
        type= "Clear"
    ),
    "Waterway Clear": BombHLocationData(
        region="Waterway",
        address=0x1348208,
        type= "Clear"
    ),
    "Water Slider Clear": BombHLocationData(
        region="Water Slider",
        address=0x1348218,
        type= "Clear"
    ),

    "Rockn Road Clear": BombHLocationData(
        region="Rockn Road",
        address=0x1348248,
        type= "Clear"
    ),
    "Water Pool Clear": BombHLocationData(
        region="Water Pool",
        address=0x1348258,
        type= "Clear"
    ),
    "Millian Road Clear": BombHLocationData(
        region="Millian Road",
        address=0x1348268,
        type= "Clear"
    ),
    "Warp Room Clear": BombHLocationData(
        region="Warp Room",
        address=0x1348278,
        type= "Clear"
    ),
    "Dark Prison Clear": BombHLocationData(
        region="Dark Prison",
        address=0x1348288,
        type= "Clear"
    ),
    "Vs Nitros Primus Clear": BombHLocationData(
        region="Vs Nitros Primus",
        address=0x1348298,
        type= "Clear"
    ),

    "Killer Gate Clear": BombHLocationData(
        region="Killer Gate",
        address=0x13482B8,
        type= "Clear"
    ),
    "Spiral Tower Clear": BombHLocationData(
        region="Spiral Tower",
        address=0x13482C8,
        type= "Clear"
    ),
    "Snake Route Clear": BombHLocationData(
        region="Snake Route",
        address=0x13482D8,
        type= "Clear"
    ),
    "Vs Baruda Clear": BombHLocationData(
        region="Vs Baruda",
        address=0x13482E8,
        type= "Clear"
    ),

    # Kanatia
    "Hades Crater Clear": BombHLocationData(
        region="Hades Crater",
        address=0x1348328,
        type= "Clear",
    ),
    "Magma Lake Clear": BombHLocationData(
        region="Magma Lake",
        address=0x1348338,
        type= "Clear",
    ),
    "Magma Dam Clear": BombHLocationData(
        region="Magma Dam",
        address=0x1348348,
        type= "Clear",
    ),
    "Crysta Hole Clear": BombHLocationData(
        region="Crysta Hole",
        address=0x1348358,
        type= "Clear",
    ),
    "Emerald Tube Clear": BombHLocationData(
        region="Emerald Tube",
        address=0x1348368,
        type= "Clear",
    ),

    "Death Temple Clear": BombHLocationData(
        region="Death Temple",
        address=0x1348398,
        type= "Clear",
    ),
    "Death Road Clear": BombHLocationData(
        region="Death Road",
        address=0x13483A8,
        type= "Clear",
    ),
    "Death Garden Clear": BombHLocationData(
        region="Death Garden",
        address=0x13483B8,
        type= "Clear",
    ),
    "Float Zone Clear": BombHLocationData(
        region="Float Zone",
        address=0x13483C8,
        type= "Clear",
    ),
    "Aqua Tank Clear": BombHLocationData(
        region="Aqua Tank",
        address=0x13483D8,
        type= "Clear",
    ),
    "Aqua Way Clear": BombHLocationData(
        region="Aqua Way",
        address=0x13483E8,
        type= "Clear",
    ),
    "Vs Nitros Kanatia Clear": BombHLocationData(
        region="Vs Nitros Kanatia",
        address=0x13483F8,
        type= "Clear",
    ),

    "Hard Coaster Clear": BombHLocationData(
        region="Hard Coaster",
        address=0x1348408,
        type= "Clear",
    ),
    "Dark Maze Clear": BombHLocationData(
        region="Dark Maze",
        address=0x1348418,
        type= "Clear",
    ),
    "Mad Coaster Clear": BombHLocationData(
        region="Mad Coaster",
        address=0x1348428,
        type= "Clear",
    ),
    "Move Stone Clear": BombHLocationData(
        region="Move Stone",
        address=0x1348438,
        type= "Clear",
    ),
    "Vs Bolban Clear": BombHLocationData(
        region="Vs Bolban",
        address=0x1348448,
        type= "Clear",
    ),

    # Mazone
    "Hopper Land Clear": BombHLocationData(
        region="Hopper Land",
        address=0x1348478,
        type= "Clear",
    ),
    "Junfalls Clear": BombHLocationData(
        region="Junfalls",
        address=0x1348488,
        type= "Clear",
    ),
    "Freeze Lake Clear": BombHLocationData(
        region="Freeze Lake",
        address=0x1348498,
        type= "Clear",
    ),
    "Cool Cave Clear": BombHLocationData(
        region="Cool Cave",
        address=0x13484A8,
        type= "Clear",
    ),

    "Snowland Clear": BombHLocationData(
        region="Snowland",
        address=0x13484E8,
        type= "Clear",
    ),
    "Storm Valley Clear": BombHLocationData(
        region="Storm Valley",
        address=0x13484F8,
        type= "Clear",
    ),
    "Snow Circuit Clear": BombHLocationData(
        region="Snow Circuit",
        address=0x1348508,
        type= "Clear",
    ),
    "Heaven Sky Clear": BombHLocationData(
        region="Heaven Sky",
        address=0x1348518,
        type= "Clear",
    ),
    "Eye Snake Clear": BombHLocationData(
        region="Eye Snake",
        address=0x1348528,
        type= "Clear",
    ),

    "Vs Nitros Mazone Clear": BombHLocationData(
        region="Vs Nitros Mazone",
        address=0x1348558,
        type= "Clear",
    ),
    "Air Room Clear": BombHLocationData(
        region="Air Room",
        address=0x1348568,
        type= "Clear",
    ),
    "Zero G Room Clear": BombHLocationData(
        region="Zero G Room",
        address=0x1348578,
        type= "Clear",
    ),
    "Mirror Room Clear": BombHLocationData(
        region="Mirror Room",
        address=0x1348588,
        type= "Clear",
    ),
    "Vs Natia Clear": BombHLocationData(
        region="Vs Natia",
        address=0x1348598,
        type= "Clear",
    ),

    #Garadan
    
    "Boss Room 1 Clear": BombHLocationData(
        region="Boss Room 1",
        address=0x13485C8,
        type= "Clear",
    ),
    "Boss Room 2 Clear": BombHLocationData(
        region="Boss Room 2",
        address=0x13485D8,
        type= "Clear",
    ),
    "Boss Room 3 Clear": BombHLocationData(
        region="Boss Room 3",
        address=0x13485E8,
        type= "Clear",
    ),
    "Boss Room 4 Clear": BombHLocationData(
        region="Boss Room 4",
        address=0x13485F8,
        type= "Clear",
    ),
    "Boss Room 5 Clear": BombHLocationData(
        region="Boss Room 5",
        address=0x1348608,
        type= "Clear",
    ),
    "Boss Room 6 Clear": BombHLocationData(
        region="Boss Room 6",
        address=0x1348618,
        type= "Clear",
    ),
    "Vs Bagular": BombHLocationData(
        region="Vs Bagular",
        address=0x1348628,
        locked_item="Disk",
        type= "Clear",
    ),

    # Gossick
    #"Outter Road Clear": BombHLocationData(
    #    region="Outter Road",
    #    address=0x1348718,
    #),
    #"Inner Road Clear": BombHLocationData(
    #    region="Inner Road",
    #    address=0x1348728,
    #),
    #"Vs Evil Bomber Clear": BombHLocationData(
    #    region="Vs Evil Bomber",
    #    address=0x1348738,
    #),


    # Clear Points
    # Bomber Planet
    "Battle Room Points": BombHLocationData(
        region="Battle Room",
        address=0x1348089,
        type= "Points",
    ),
    "Hyper Room Points": BombHLocationData(
        region="Hyper Room",
        address=0x1348099,
        type= "Points",
    ),
    "Secret Room Points": BombHLocationData(
        region="Secret Room",
        address=0x13480A9,
        type= "Points",
    ),
    "Heavy Room Points": BombHLocationData(
        region="Heavy Room",
        address=0x13480B9,
        type= "Points",
    ),
    "Sky Room Points": BombHLocationData(
        region="Sky Room",
        address=0x13480C9,
        type= "Points",
    ),

    "Blue Cave Points": BombHLocationData(
        region="Blue Cave",
        address=0x13480F9,
        type= "Points",
    ),
    "Hole Lake Points": BombHLocationData(
        region="Hole Lake",
        address=0x1348109,
        type= "Points",
    ),
    "Red Cave Points": BombHLocationData(
        region="Red Cave",
        address=0x1348119,
        type= "Points",
    ),
    "Big Cannon Points": BombHLocationData(
        region="Big Cannon",
        address=0x1348129,
        type= "Points",
    ),
    "Dark Wood Points": BombHLocationData(
        region="Dark Wood",
        address=0x1348139,
        type= "Points",
    ),
    "Dragon Road Points": BombHLocationData(
        region="Dragon Road",
        address=0x1348149,
        type= "Points",
    ),
    "Vs Nitros Planet Bomber Points": BombHLocationData(
        region="Vs Nitros Planet Bomber",
        address=0x1348159,
        type= "Points",
    ),

    "Clown Valley Points": BombHLocationData(
        region="Clown Valley",
        address=0x1348169,
        type= "Points",
    ),
    "Great Rock Points": BombHLocationData(
        region="Great Rock",
        address=0x1348179,
        type= "Points",
    ),
    "Fog Route Points": BombHLocationData(
        region="Fog Route",
        address=0x1348189,
        type= "Points",
    ),
    "Vs Endol Points": BombHLocationData(
        region="Vs Endol",
        address=0x1348199,
        type= "Points",
    ),

    # Primus
    "Groog Hills Points": BombHLocationData(
        region="Groog Hills",
        address=0x13481D9,
        type= "Points",
    ),
    "Bubble Hole Points": BombHLocationData(
        region="Bubble Hole",
        address=0x13481E9,
        type= "Points",
    ),
    "Erars Lake Points": BombHLocationData(
        region="Erars Lake",
        address=0x13481F9,
        type= "Points",
    ),
    "Waterway Points": BombHLocationData(
        region="Waterway",
        address=0x1348209,
        type= "Points",
    ),
    "Water Slider Points": BombHLocationData(
        region="Water Slider",
        address=0x1348219,
        type= "Points",
    ),

    "Rockn Road Points": BombHLocationData(
        region="Rockn Road",
        address=0x1348249,
        type= "Points",
    ),
    "Water Pool Points": BombHLocationData(
        region="Water Pool",
        address=0x1348259,
        type= "Points",
    ),
    "Millian Road Points": BombHLocationData(
        region="Millian Road",
        address=0x1348269,
        type= "Points",
    ),
    "Warp Room Points": BombHLocationData(
        region="Warp Room",
        address=0x1348279,
        type= "Points",
    ),
    "Dark Prison Points": BombHLocationData(
        region="Dark Prison",
        address=0x1348289,
        type= "Points",
    ),
    "Vs Nitros Primus Points": BombHLocationData(
        region="Vs Nitros Primus",
        address=0x1348299,
        type= "Points",
    ),

    "Killer Gate Points": BombHLocationData(
        region="Killer Gate",
        address=0x13482B9,
        type= "Points",
    ),
    "Spiral Tower Points": BombHLocationData(
        region="Spiral Tower",
        address=0x13482C9,
        type= "Points",
    ),
    "Snake Route Points": BombHLocationData(
        region="Snake Route",
        address=0x13482D9,
        type= "Points",
    ),
    "Vs Baruda Points": BombHLocationData(
        region="Vs Baruda",
        address=0x13482E9,
        type= "Points",
    ),

    # Kanatia
    "Hades Crater Points": BombHLocationData(
        region="Hades Crater",
        address=0x1348329,
        type= "Points",
    ),
    "Magma Lake Points": BombHLocationData(
        region="Magma Lake",
        address=0x1348339,
        type= "Points",
    ),
    "Magma Dam Points": BombHLocationData(
        region="Magma Dam",
        address=0x1348349,
        type= "Points",
    ),
    "Crysta Hole Points": BombHLocationData(
        region="Crysta Hole",
        address=0x1348359,
        type= "Points",
    ),
    #"Emerald Tube Points": BombHLocationData(
    #    region="Emerald Tube",
    #    address=0x1348369,
    #),

    "Death Temple Points": BombHLocationData(
        region="Death Temple",
        address=0x1348399,
        type= "Points",
    ),
    "Death Road Points": BombHLocationData(
        region="Death Road",
        address=0x13483A9,
        type= "Points",
    ),
    "Death Garden Points": BombHLocationData(
        region="Death Garden",
        address=0x13483B9,
        type= "Points",
    ),
    "Float Zone Points": BombHLocationData(
        region="Float Zone",
        address=0x13483C9,
        type= "Points",
    ),
    "Aqua Tank Points": BombHLocationData(
        region="Aqua Tank",
        address=0x13483D9,
        type= "Points",
    ),
    "Aqua Way Points": BombHLocationData(
        region="Aqua Way",
        address=0x13483E9,
        type= "Points",
    ),
    "Vs Nitros Kanatia Points": BombHLocationData(
        region="Vs Nitros Kanatia",
        address=0x13483F9,
        type= "Points",
    ),

    "Hard Coaster Points": BombHLocationData(
        region="Hard Coaster",
        address=0x1348409,
        type= "Points",
    ),
    "Dark Maze Points": BombHLocationData(
        region="Dark Maze",
        address=0x1348419,
        type= "Points",
    ),
    "Mad Coaster Points": BombHLocationData(
        region="Mad Coaster",
        address=0x1348429,
        type= "Points",
    ),
    "Move Stone Points": BombHLocationData(
        region="Move Stone",
        address=0x1348439,
        type= "Points",
    ),
    "Vs Bolban Points": BombHLocationData(
        region="Vs Bolban",
        address=0x1348449,
        type= "Points",
    ),

    # Mazone
    "Hopper Land Points": BombHLocationData(
        region="Hopper Land",
        address=0x1348479,
        type= "Points",
    ),
    "Junfalls Points": BombHLocationData(
        region="Junfalls",
        address=0x1348489,
        type= "Points",
    ),
    "Freeze Lake Points": BombHLocationData(
        region="Freeze Lake",
        address=0x1348499,
        type= "Points",
    ),
    "Cool Cave Points": BombHLocationData(
        region="Cool Cave",
        address=0x13484A9,
        type= "Points",
    ),

    "Snowland Points": BombHLocationData(
        region="Snowland",
        address=0x13484E9,
        type= "Points",
    ),
    "Storm Valley Points": BombHLocationData(
        region="Storm Valley",
        address=0x13484F9,
        type= "Points",
    ),
    "Snow Circuit Points": BombHLocationData(
        region="Snow Circuit",
        address=0x1348509,
        type= "Points",
    ),
    "Heaven Sky Points": BombHLocationData(
        region="Heaven Sky",
        address=0x1348519,
        type= "Points",
    ),
    "Eye Snake Points": BombHLocationData(
        region="Eye Snake",
        address=0x1348529,
        type= "Points",
    ),

    "Vs Nitros Mazone Points": BombHLocationData(
        region="Vs Nitros Mazone",
        address=0x1348559,
        type= "Points",
    ),
    "Air Room Points": BombHLocationData(
        region="Air Room",
        address=0x1348569,
        type= "Points",
    ),
    "Zero G Room Points": BombHLocationData(
        region="Zero G Room",
        address=0x1348579,
        type= "Points",
    ),
    "Mirror Room Points": BombHLocationData(
        region="Mirror Room",
        address=0x1348589,
        type= "Points",
    ),
    "Vs Natia Points": BombHLocationData(
        region="Vs Natia",
        address=0x1348599,
        type= "Points",
    ),

    #Garadan
    
    "Boss Room 1 Points": BombHLocationData(
        region="Boss Room 1",
        address=0x13485C9,
        type= "Points",
    ),
    "Boss Room 2 Points": BombHLocationData(
        region="Boss Room 2",
        address=0x13485D9,
        type= "Points",
    ),
    "Boss Room 3 Points": BombHLocationData(
        region="Boss Room 3",
        address=0x13485E9,
        type= "Points",
    ),
    "Boss Room 4 Points": BombHLocationData(
        region="Boss Room 4",
        address=0x13485F9,
        type= "Points",
    ),
    "Boss Room 5 Points": BombHLocationData(
        region="Boss Room 5",
        address=0x1348609,
        type= "Points",
    ),
    "Boss Room 6 Points": BombHLocationData(
        region="Boss Room 6",
        address=0x1348619,
        type= "Points",
    ),

    # Gossick
    #"Outter Road Points": BombHLocationData(
    #    region="Outter Road",
    #    address=0x1348719,
    #),
    #"Inner Road Points": BombHLocationData(
    #    region="Inner Road",
    #    address=0x1348729,
    #),
    #"Evil Bomber Points": BombHLocationData(
    #    region="Vs Evil Bomber",
    #    address=0x1348739,
    #),

    # Adok Bombs

    "Heavy Room Adok Bomb": BombHLocationData(
        region="Heavy Room",
        address=0x574950,
        type= "Adok",
    ),
    "Sky Room Adok Bomb": BombHLocationData(
        region="Sky Room",
        address=0x574951,
        type= "Adok",
    ),
    "Dark Wood Adok Bomb": BombHLocationData(
        region="Dark Wood",
        address=0x574952,
        type= "Adok",
    ),
    "Dragon Road Adok Bomb": BombHLocationData(
        region="Dragon Road",
        address=0x574953,
        type= "Adok",
    ),
    "Clown Valley Adok Bomb": BombHLocationData(
        region="Clown Valley",
        address=0x574954,
        type= "Adok",
    ),
    "Great Rock Adok Bomb": BombHLocationData(
        region="Great Rock",
        address=0x574955,
        type= "Adok",
    ),
    "Bubble Hole Adok Bomb": BombHLocationData(
        region="Bubble Hole",
        address=0x574956,
        type= "Adok",
    ),
    "Water Slider Adok Bomb": BombHLocationData(
        region="Water Slider",
        address=0x574957,
        type= "Adok",
    ),

    "Water Pool Adok Bomb": BombHLocationData(
        region="Water Pool",
        address=0x574960,
        type= "Adok",
    ),
    "Warp Room Adok Bomb": BombHLocationData(
        region="Warp Room",
        address=0x574961,
        type= "Adok",
    ),
    "Killer Gate Adok Bomb": BombHLocationData(
        region="Killer Gate",
        address=0x574962,
        type= "Adok",
    ),
    "Spiral Tower Adok Bomb": BombHLocationData(
        region="Spiral Tower",
        address=0x574963,
        type= "Adok",
    ),
    "Magma Dam Adok Bomb": BombHLocationData(
        region="Magma Dam",
        address=0x574964,
        type= "Adok",
    ),
    "Crysta Hole Adok Bomb": BombHLocationData(
        region="Crysta Hole",
        address=0x574965,
        type= "Adok",
    ),
    "Death Garden Adok Bomb": BombHLocationData(
        region="Death Garden",
        address=0x574966,
        type= "Adok",
    ),
    "Float Zone Adok Bomb": BombHLocationData(
        region="Float Zone",
        address=0x574967,
        type= "Adok",
    ),

    "Hard Coaster Adok Bomb": BombHLocationData(
        region="Hard Coaster",
        address=0x574970,
        type= "Adok",
    ),
    "Dark Maze Adok Bomb": BombHLocationData(
        region="Dark Maze",
        address=0x574971,
        type= "Adok",
    ),
    "Junfalls Adok Bomb": BombHLocationData(
        region="Junfalls",
        address=0x574972,
        type= "Adok",
    ),
    "Cool Cave Adok Bomb": BombHLocationData(
        region="Cool Cave",
        address=0x574973,
        type= "Adok",
    ),
    "Snowland Adok Bomb": BombHLocationData(
        region="Snowland",
        address=0x574974,
        type= "Adok",
    ),
    "Heaven Sky Adok Bomb": BombHLocationData(
        region="Heaven Sky",
        address=0x574975,
        type= "Adok",
    ),
    "Air Room Adok Bomb": BombHLocationData(
        region="Air Room",
        address=0x574976,
        type= "Adok",
    ),
    "Zero G Room Adok Bomb": BombHLocationData(
        region="Zero G Room",
        address=0x574977,
        type= "Adok",
    ),

}
gem_data_table: Dict[str, BombHLocationData] = {
    "Crystals 1": BombHLocationData(
        region="Planet Bomber",
        address=0x1348061,
        type= "Crystal",
    ),
    "Crystals 2": BombHLocationData(
        region="Planet Bomber",
        address=0x1348062,
        type= "Crystal",
    ),
    "Crystals 3": BombHLocationData(
        region="Planet Bomber",
        address=0x1348063,
        type= "Crystal",
    ),
    "Crystals 4": BombHLocationData(
        region="Planet Bomber",
        address=0x1348064,
        type= "Crystal",
    ),
    "Crystals 5": BombHLocationData(
        region="Planet Bomber",
        address=0x1348065,
        type= "Crystal",
    ),
    "Crystals 6": BombHLocationData(
        region="Planet Bomber",
        address=0x1348066,
        type= "Crystal",
    ),
    "Crystals 7": BombHLocationData(
        region="Planet Bomber",
        address=0x1348067,
        type= "Crystal",
    ),
    "Crystals 8": BombHLocationData(
        region="Planet Bomber",
        address=0x1348068,
        type= "Crystal",
    ),
    "Crystals 9": BombHLocationData(
        region="Planet Bomber",
        address=0x1348069,
        type= "Crystal",
    ),
    "Crystals 10": BombHLocationData(
        region="Planet Bomber",
        address=0x134806A,
        type= "Crystal",
    ),
}
radio_data_table: Dict[str, BombHLocationData] = {
    "Battle Room Radio Entrance": BombHLocationData(
        region="Battle Room",
        address=0x134808A,
        type= "Radio",
    ),
    "Battle Room Radio Platform": BombHLocationData(
        region="Battle Room",
        address=0x134808B,
        type= "Radio",
    ),
    "Battle Room Radio Switch": BombHLocationData(
        region="Battle Room",
        address=0x134808C,
        type= "Radio",
    ),
    "Hyper Room Radio Entrance": BombHLocationData(
        region="Hyper Room",
        address=0x134809A,
        type= "Radio",
    ),
    "Hyper Room Radio Door": BombHLocationData(
        region="Hyper Room",
        address=0x134809B,
        type= "Radio",
    ),
    "Secret Room Radio Entrance": BombHLocationData(
        region="Secret Room",
        address=0x13480AA,
        type= "Radio",
    ),
    "Heavy Room Radio Entrance": BombHLocationData(
        region="Heavy Room",
        address=0x13480BA,
        type= "Radio",
    ),
    "Heavy Room Radio Barrier Tower": BombHLocationData(
        region="Heavy Room",
        address=0x13480BB,
        type= "Radio",
    ),
    "Sky Room Radio Entrance": BombHLocationData(
        region="Sky Room",
        address=0x13480CA,
        type= "Radio",
    ),
    "Red Cave Radio Lower Path": BombHLocationData(
        region="Red Cave",
        address=0x134811A,
        type= "Radio",
    ),
    "Dark Wood Radio Entrance": BombHLocationData(
        region="Dark Wood",
        address=0x134813A,
        type= "Radio",
    ),
    "Groog Hills Radio Entrance": BombHLocationData(
        region="Groog Hills",
        address=0x13481DA,
        type= "Radio",
    ),
    "Groog Hills Radio Right Big Tree": BombHLocationData(
        region="Groog Hills",
        address=0x13481DB,
        type= "Radio",
    ),
    "Groog Hills Radio Freeze Flower": BombHLocationData(
        region="Groog Hills",
        address=0x13481DC,
        type= "Radio",
    ),
    "Bubble Hole Radio Entrance": BombHLocationData(
        region="Bubble Hole",
        address=0x13481EA,
        type= "Radio",
    ),
    "Erars Lake Radio Entrance": BombHLocationData(
        region="Erars Lake",
        address=0x13481FA,
        type= "Radio",
    ),
    "Dark Prison Radio Entrance": BombHLocationData(
        region="Dark Prison",
        address= 0x134828A,
        type= "Radio",
    ),
    "Killer Gate Radio Entrance": BombHLocationData(
        region="Killer Gate",
        address=0x13482BA,
        type= "Radio",
    ),
    "Hades Crater Radio Entrance": BombHLocationData(
        region="Hades Crater",
        address=0x134832A,
        type= "Radio",
    ),
    "Magma Dam Radio Entrance": BombHLocationData(
        region="Magma Dam",
        address=0x134833A,
        type= "Radio",
    ),
    "Magma Dam Radio Left Dam": BombHLocationData(
        region="Magma Dam",
        address=0x134833B,
        type= "Radio",
    ),
    "Float Zone Radio Entrance": BombHLocationData(
        region="Float Zone",
        address=0x13483CA,
        type= "Radio",
    ),
    "Aqua Tank Radio Entrance": BombHLocationData(
        region="Aqua Tank",
        address=0x13483DA,
        type= "Radio",
    ),
    "Hard Coaster Radio Green Warp": BombHLocationData(
        region="Hard Coaster",
        address=0x134840A,
        type= "Radio",
    ),
    "Move Stone Radio Entrance": BombHLocationData(
        region="Move Stone",
        address=0x134843A,
        type= "Radio",
    ),
    "Hopper Land Radio Entrance": BombHLocationData(
        region="Hopper Land",
        address=0x134847A,
        type= "Radio",
    ),
    "Storm Valley Radio Entrance": BombHLocationData(
        region="Storm Valley",
        address=0x13484FA,
        type= "Radio",
    ),
    "Zero G Room Radio Switch": BombHLocationData(
        region="Zero G Room",
        address=0x134857A,
        type= "Radio",
    ),
    "Mirror Room Radio Entrance": BombHLocationData(
        region="Mirror Room",
        address=0x134858A,
        type= "Radio",
    ),
    "Mirror Room Radio Right Ramp": BombHLocationData(
        region="Mirror Room",
        address=0x134858B,
        type= "Radio",
    ),

}


location_table =   {name: data.address for name, data in location_data_table.items() if data.address is not None}
radio_name_table = {name: data.address for name, data in radio_data_table.items() if data.address is not None}
gem_name_table =   {name: data.address for name, data in gem_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
stage_clears = {data.address: ((data.address & 0xFFFFFF0) >> 4) for name, data in location_data_table.items() if data.type == "Clear"}
point_clears = {data.address: ((data.address & 0xFFFFFF0) >> 4) for name, data in location_data_table.items() if data.type == "Points"}