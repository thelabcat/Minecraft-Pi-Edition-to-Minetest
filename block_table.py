#Minecraft Pi to Minetest translation table v1.0
#S.D.G.

ID_TO_NAME={
    0: 'AIR',
    1: 'STONE',
    2: 'GRASS',
    3: 'DIRT',
    4: 'COBBLESTONE',
    5: 'WOOD_PLANKS',
    6: 'SAPLING',
    7: 'BEDROCK',
    8: 'WATER',
    9: 'WATER_STATIONARY',
    10: 'LAVA',
    11: 'LAVA_STATIONARY',
    12: 'SAND',
    13: 'GRAVEL',
    14: 'GOLD_ORE',
    15: 'IRON_ORE',
    16: 'COAL_ORE',
    17: 'WOOD',
    18: 'LEAVES',
    20: 'GLASS',
    21: 'LAPIS_LAZULI_ORE',
    22: 'LAPIS_LAZULI_BLOCK',
    24: 'SANDSTONE',
    26: 'BED',
    27: 'RAIL_POWERED',
    28: 'RAIL_DETECTOR',
    30: 'COBWEB',
    31: 'GRASS_TALL',
    32: 'DEAD_BUSH',
    35: 'WOOL',
    37: 'FLOWER_YELLOW',
    38: 'FLOWER_CYAN',
    39: 'MUSHROOM_BROWN',
    40: 'MUSHROOM_RED',
    41: 'GOLD_BLOCK',
    42: 'IRON_BLOCK',
    43: 'STONE_SLAB_DOUBLE',
    44: 'STONE_SLAB',
    45: 'BRICK_BLOCK',
    46: 'TNT',
    47: 'BOOKSHELF',
    48: 'MOSS_STONE',
    49: 'OBSIDIAN',
    50: 'TORCH',
    51: 'FIRE',
    53: 'STAIRS_WOOD',
    54: 'CHEST',
    56: 'DIAMOND_ORE',
    57: 'DIAMOND_BLOCK',
    58: 'CRAFTING_TABLE',
    60: 'FARMLAND',
    61: 'FURNACE_INACTIVE',
    62: 'FURNACE_ACTIVE',
    63: 'SIGN_STANDING',
    64: 'DOOR_WOOD',
    65: 'LADDER',
    66: 'RAIL',
    67: 'STAIRS_COBBLESTONE',
    68: 'SIGN_WALL',
    71: 'DOOR_IRON',
    73: 'REDSTONE_ORE',
    76: 'TORCH_REDSTONE',
    78: 'SNOW',
    79: 'ICE',
    80: 'SNOW_BLOCK',
    81: 'CACTUS',
    82: 'CLAY',
    83: 'SUGAR_CANE',
    85: 'FENCE',
    86: 'PUMPKIN',
    87: 'NETHERRACK',
    88: 'SOUL_SAND',
    89: 'GLOWSTONE_BLOCK',
    91: 'LIT_PUMPKIN',
    95: 'BEDROCK_INVISIBLE',
    96: 'TRAPDOOR',
    98: 'STONE_BRICK',
    102: 'GLASS_PANE',
    103: 'MELON',
    107: 'FENCE_GATE',
    108: 'STAIRS_BRICK',
    109: 'STAIRS_STONE_BRICK',
    110: 'MYCELIUM',
    112: 'NETHER_BRICK',
    113: 'FENCE_NETHER_BRICK',
    114: 'STAIRS_NETHER_BRICK',
    121: 'END_STONE',
    126: 'WOODEN_SLAB',
    128: 'STAIRS_SANDSTONE',
    129: 'EMERALD_ORE',
    157: 'RAIL_ACTIVATOR',
    161: 'LEAVES2',
    167: 'TRAPDOOR_IRON',
    188: 'FENCE_SPRUCE',
    189: 'FENCE_BIRCH',
    190: 'FENCE_JUNGLE',
    191: 'FENCE_DARK_OAK',
    192: 'FENCE_ACACIA',
    193: 'DOOR_SPRUCE',
    194: 'DOOR_BIRCH',
    195: 'DOOR_JUNGLE',
    196: 'DOOR_ACACIA',
    197: 'DOOR_DARK_OAK',
    246: 'GLOWING_OBSIDIAN',
    247: 'NETHER_REACTOR_CORE',
    59: "WHEAT",
    74: "LIT_REDSTONE_ORE",
    105: "MELON_STEM",
    155: "QUARTZ_BLOCK",
    156: "QUARTZ_STAIRS"
    }

"""
Look up by mcpi.block absolute variable names.
- If value is a string, use that Minetest block.
- If value is a list or tuple of strings, look up string by Minecraft block data.
- If value is a list or tuple of tuples, look up tuple by Minecraft block data, and
    use first tuple element (string) as Minetest block, and
    use second tuple element (integer) as Minetest param2 value.
"""

TRANSLATE = {
    "AIR" : "default:air",

    "STONE" : "default:stone",
    #Minecraft stone data starts with stone,
    #then goes through granite, diorite, and andesite,
    #with each mineral's smooth variant after the base variant

    "GRASS" : "default:dirt_with_grass",

    "DIRT" : "default:dirt",
    #Minecraft dirt data goes through dirt, coarse dirt, and podzol

    "COBBLESTONE" : "default:cobble",

    "WOOD_PLANKS" : "default:wood",
    "SAPLING" : ("default:sapling", "default:pine_sapling", "default:aspen_sapling", "default:junglesapling", "default:emergent_jungle_sapling", "default:acacia_sapling"),
    #Minecraft data on wood planks AND saplings goes through tree type
    #(oak, spruce, birch, jungle, acacia, dark oak, oak, oak).
    #Saplings then go through a second stage of maturity

    "BEDROCK" : "default:desert_stone",

    "WATER_FLOWING" : ["default:water_source"]+["default:air"]*7,
    "WATER" : ["default:water_source"]+["default:air"]*7,
    "WATER_STATIONARY" : ["default:water_source"]+["default:air"]*7,
    "LAVA_FLOWING" : ["default:lava_source"]+["default:air"]*7,
    "LAVA" : ["default:lava_source"]+["default:air"]*7,
    "LAVA_STATIONARY" : ["default:lava_source"]+["default:air"]*7,
    #Minecraft data on liquid goes through 8 fill levels,
    #(from full to almost empty), plus 8 unknown levels?

    "SAND" : "default:sand",
    #Minecraft data on sand can change it to red sand

    "GRAVEL" : "default:gravel",
    "GOLD_ORE" : "default:stone_with_gold",
    "IRON_ORE" : "default:stone_with_iron",
    "COAL_ORE" : "default:stone_with_coal",

    "WOOD" : [("default:"+i+"tree", p) for p in (0, 12, 7) for i in ("", "pine_", "aspen_", "jungle", "jungle", "acacia_")],
    #Minecraft data on logs goes through tree type
    #(oak, spruce, birch, jungle, acacia, dark oak, oak, oak),
    #Then through axes (Y, X, Z, none [X])

    "LEAVES" : [("default:"+i, p) for p in (0, 1, 0, 1) for i in ("leaves", "pine_needles", "aspen_leaves", "jungleleaves", "jungleleaves", "acacia_leaves")],
    #Minecraft data on leaves goes through tree type
    #(oak, spruce, birch, jungle, acacia, dark oak, oak, oak),
    #Then through 'check_decay' and 'decayable' values
    #(FT, FF, TT, TF).

    "GLASS" : "default:glass",
    "LAPIS_LAZULI_ORE" : "moreores:mineral_mithril",
    "LAPIS_LAZULI_BLOCK" : "moreores:mithril_block",

    "SANDSTONE" : ["default:sandstone"]+["default:sandstone_block"]*2,
    #Minecraft data on sandstone goes through plain, chiseled, and smooth variants

    "BED" : [("beds:bed_"+x, p) for x in ("bottom", "top") for ignore in range(2) for p in (2, 3, 0, 1)],
    #Minecraft data on beds goes through facing (SWNE),
    #then occupied (False, True assumed), then the same on the head half of the bed.

    "RAIL_POWERED" : "carts:powerrail",

    "RAIL_DETECTOR" : "boost_cart:detectorrail",
    #Minecraft data on detector rails goes through 9 unknown variants of N-S facing,
    #then east-west, then four ascending variants (EWNS)

    "COBWEB" : "default:air",

    "GRASS_TALL" : ["default:"+x for x in ("bush_stem", "grass_1", "fern_1")],
    #Minecraft data for tall grass goes through deadbush, tall grass, and fern

    "DEAD_BUSH" : "default:bush_stem",

    "WOOL" : ["wool:"+x for x in ("white", "orange", "magenta", "cyan", "yellow", "green", "pink", "dark_grey", "grey", "cyan", "violet", "blue", "brown", "dark_green", "red", "black")],
    #Minecraft data for wool goes through colors:
    #(white, orange, magenta, light blue, yellow, lime, pink, grey, silver, cyan, purple, blue, brown, green, red, black)

    "FLOWER_YELLOW" : "flowers:dandelion_yellow",

    "FLOWER_CYAN" : ["flowers:"+x for x in ("rose", "geranium", "geranium", "dandelion_white", "tulip", "tulip_black", "tulip_black", "dandelion_white")],
    #Minecraft data for "red" flower goes through types:
    #(poppy, blue orchid, allium, houstonia, red tulip, orange tulip, white tulip, pink tulip, oxeye daisy)

    "MUSHROOM_BROWN" : "flowers:mushroom_brown",
    "MUSHROOM_RED" : "flowers:mushroom_red",
    "GOLD_BLOCK" : "default:goldblock",
    "IRON_BLOCK" : "default:steelblock",

    "STONE_SLAB_DOUBLE" : ["default:"+x for x in ("stone", "sandstone", "wood", "cobble", "brick", "stonebrick", "desert_stonebrick", "silver_sandstone_block")],
    "STONE_SLAB" : [("moreblocks:slab_"+x, p) for p in (0, 20) for x in ("stone", "sandstone", "wood", "cobble", "brick", "stonebrick", "desert_stonebrick", "silver_sandstone_block")],
    #Minecraft data for slabs goes through type
    #(stone, sandstone, old wood, cobblestone, brick, stone brick, nether brick, quartz),
    #Then for double slabs it goes to seamless, and for single slabs switches to top half.

    "BRICK_BLOCK" : "default:brick",
    "TNT" : "tnt:tnt",
    "BOOKSHELF" : "default:bookshelf",
    "MOSS_STONE" : "default:mossycobble",
    "OBSIDIAN" : "default:obsidian",

    "TORCH" : [("default:torch", 1)]+[("default:torch_wall", p) for p in (3, 2, 4, 5)],
    #Minecraft data on torches starts on floor, then changes wall-mount facing (EWSN)

    "FIRE" : "fire:flame",

    "STAIRS_WOOD" : [("moreblocks:stair_wood", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    #Minecraft stair data works through back-is-facing (EWSN), then upside-down.
    #Turned shapes are not included in the data

    "CHEST" : [("default:chest", p) for p in (2, 2, 2, 0, 1, 3)],
    #Minecraft data on chests goes through three unknown North-facing variants, then SWE.

    "DIAMOND_ORE" : "default:stone_with_diamond",
    "DIAMOND_BLOCK" : "default:diamond_block",
    "CRAFTING_TABLE" : "moreblocks:circular_saw",

    "FARMLAND" : ["farming:soil"]+["farming:soil_wet"]*7,
    #Minecraft data on farming soil changes the moisture level (0-7).

    "FURNACE_INACTIVE" : [("default:furnace", p) for p in (2, 2, 2, 0, 1, 3)],
    "FURNACE_ACTIVE" : [("default:furnace_active", p) for p in (2, 2, 2, 0, 1, 3)],
    #Minecraft data on furnaces goes through three unknown North-facing variants, then SWE.


    "SIGN_STANDING" : "default:sign_wall_wood",
    #Minecraft data on signs goes through 16 levels of clockwise rotation, starting facing South.

    "DOOR_WOOD" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    #Minecraft door data works through space-is-facing (ESWN), then open, then upper.
    #The first door block is West closed bottom, the last is North open top.

    "LADDER" : [("default:ladder_wood", p) for p in (5, 5, 5, 4, 2, 3)],
    #Minecraft data on ladders goes through three unknown North-facing variants, then SWE.

    "RAIL" : "carts:rail",
    "STAIRS_COBBLESTONE" : "moreblocks:stair_cobble",

    "SIGN_WALL" : [("default:sign_wall_wood", p) for p in (5, 5, 5, 4, 2, 3)],
    #Minecraft data on wall-mounted signs goes through three unknown North-facing variants, then SWE.

    "DOOR_IRON" : [("doors:door_steel_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    #Minecraft door data works through space-is-facing (ESWN), then open, then upper.
    #The first door block is West closed bottom, the last is North open top.

    "REDSTONE_ORE" : "default:stone_with_mese",

    "TORCH_REDSTONE" : [("mesecons_torch:mesecon_torch_on", p) for p in (1, 3, 2, 4, 5)],
    #Minecraft data on torches starts on floor, then changes wall-mount facing (EWSN)

    "SNOW" : ["default:snow"]*3+["stairs:slab_snowblock"]*3+["default:snowblock"]*2,
    #Minecraft data on layered snow goes through eight thickness levels, from thin layer to full block.

    "ICE" : "default:ice",
    "SNOW_BLOCK" : "default:snowblock",
    "CACTUS" : "default:cactus",
    "CLAY" : "default:clay",
    "SUGAR_CANE" : "default:papyrus",
    "FENCE" : "default:fence_wood",

    "PUMPKIN" : "default:apple",
    #Minecraft data on pumpkins goes through facing (SWNE)

    "NETHERRACK" : "default:desert_cobble",
    "SOUL_SAND" : "default:desert_sand",
    "GLOWSTONE_BLOCK" : "default:meselamp",

    "LIT_PUMPKIN" : "default:meselamp",
    #Minecraft data on pumpkins goes through facing (SWNE)

    "STAINED_GLASS" : "default:obsidian_glass",
    #Minecraft data for stained glass goes through colors:
    #(white, orange, magenta, light blue, yellow, lime, pink, grey, silver, cyan, purple, blue, brown, green, red, black)


    "BEDROCK_INVISIBLE" : "default:air",

    "TRAPDOOR" : [("doors:trapdoor"+o, p) for o in ("", "_open") for p in (2, 0, 1, 3)],
    #Minecraft trapdoor data works through facing (NSWE), then open, then upper.
    #The first trapdoor block is North closed bottom, the last is East open top.

    "STONE_BRICK" : ["default:stonebrick"]*3+["moreblocks:circle_stone_bricks"],
    #Minecraft data on stone brick goes through standard, mossy, cracked, and chiseled variants.

    "GLASS_PANE" : "xpanes:pane_flat",
    "MELON" : "default:apple",

    "FENCE_GATE" : [("doors:gate_wood_"+o, p) for o in ("closed", "open") for p in (2, 3, 0, 1)],
    #Minecraft data on fence gates goes through opens-inwart-to-facing (SWNE), then open

    "STAIRS_BRICK" : [("moreblocks:stair_brick", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    "STAIRS_STONE_BRICK" : [("moreblocks:stair_stonebrick", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    #Minecraft stair data works through back-is-facing (EWSN), then upside-down.
    #Turned shapes are not included in the data
    
    "MYCELIUM" : "default:air",
    "NETHER_BRICK" : "default:desert_stonebrick",
    "FENCE_NETHER_BRICK" : "default:fence_junglewood",
    
    "STAIRS_NETHER_BRICK" : [("moreblocks:stair_desert_stonebrick", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    #Minecraft stair data works through back-is-facing (EWSN), then upside-down.
    #Turned shapes are not included in the data
    
    "END_STONE" : "default:sandstone_block",

    "WOODEN_SLAB" : [("moreblocks:slab_"+i+"wood", p) for p in (0, 20) for i in ("", "pine_", "aspen_", "jungle", "acacia_", "jungle", "", "")],
    #Minecraft data on slabs goes through tree type
    #(oak, spruce, birch, jungle, acacia, dark oak, oak, oak),
    #Then upper-half slabs

    "STAIRS_SANDSTONE" : [("moreblocks:stair_sandstone", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    #Minecraft stair data works through back-is-facing (EWSN), then upside-down.
    #Turned shapes are not included in the data
    
    "EMERALD_ORE" : "default:stone_with_tin",
    "RAIL_ACTIVATOR" : "boost_cart:startstoprail",

    "LEAVES2" : [("default:"+v.strip()+"_bush_leaves", p*(v[-1]!=" ")) for p in (0, 1, 0, 1) for v in ("acacia", "jungle", "acacia ", "acacia ")],
    #Minecraft data on leaves2 goes through four vague variants (acacia, dark oak, acacia, acacia),
    #Then through check_decay and decayable values (FT, FF, TT, TF),
    #EXCEPT that all of the secondary acacia variant pairs were always FT.

    "TRAPDOOR_IRON" : [("doors:trapdoor_steel"+o, p) for o in ("", "_open") for p in (2, 0, 1, 3)],
    #Minecraft trapdoor data works through facing (NSWE), then open, then upper.
    #The first trapdoor block is North closed bottom, the last is East open top.
    
    "FENCE_SPRUCE" : "default:fence_pine_wood",
    "FENCE_BIRCH" : "default:fence_aspen_wood",
    "FENCE_JUNGLE" : "default:fence_junglewood",
    "FENCE_DARK_OAK" : "default:fence_junglewood",
    "FENCE_ACACIA" : "default:fence_acacia_wood",
    
    "DOOR_SPRUCE" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    "DOOR_BIRCH" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    "DOOR_JUNGLE" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    "DOOR_ACACIA" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    "DOOR_DARK_OAK" : [("doors:door_wood_"+x, p) for x, p in (("a", 1), ("a", 2), ("a", 3), ("a", 0), ("c", 2), ("c", 3), ("c", 0), ("c", 1))]+["default:air"]*8,
    #Minecraft door data works through space-is-facing (ESWN), then open, then upper.
    #The first door block is West closed bottom, the last is North open top.

    "GLOWING_OBSIDIAN" : "default:obsidian",
    "NETHER_REACTOR_CORE" : "mesecons_commandblock:commandblock_off"
    #Minecraft data on terracotta goes through facing (SWNE)

    "WHEAT" : [("farming:wheat_"+str(x), 3) for x in range(1, 9)]
    #Minecraft data on wheat takes it through 8 ages (just planted to harvest)
    
    "LIT_REDSTONE_ORE" : "default:stone_with_mese"
    
    "MELON_STEM" : ["default:blueberry_bush_leaves"]*7+["default:blueberry_bush_leaves_with_berries"]
    #Minecraft data on melon stem takes it through 8 ages (just planted to mature)
    
    "QUARTZ_BLOCK" : "default:silver_sandstone_block"
    
    "QUARTZ_STAIRS" : [("moreblocks:stair_silver_sandstone_block", p) for p in (1, 3, 2, 0, 23, 21, 22, 20)],
    #Minecraft stair data works through back-is-facing (EWSN), then upside-down.
    #Turned shapes are not included in the data
    }
