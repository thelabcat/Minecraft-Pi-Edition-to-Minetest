# Minecraft-Pi-Edition-to-Minetest
Translate Minecraft Pi Edition blocks with data into Minetest blocks with param2

Hey, everybody! It's Jaywright, and today, I have written a lookup table for converting Minecraft Pi Edition blocks to Minetest blocks. This table assumes Minetest Game mods, Moreblocks, Moreores, and Mesecons. The table includes all blocks in mcpi.block plus all blocks in the Minecraft Pi Edition v0.1.1-6 Creative inventory. 

Some blocks did not have direct Minetest equivalents, so I chose Minetest blocks with similar function or appearance that conversely did not directly have Minecraft Pi Edition inventory+mcpi.block equivalents. Some such blocks may actually have direct equivalents in Minecraft Pi edition only accessible through the API, though.

- TRANSLATE is a dictionairy from all-caps block names (based on mcpi.block variables in most cases), each having one or more Minetest block names, porentially with param2 values to be set. Each dictionary value is either a string (the block name), a list of strings (block names to be indexed by the Minecraft block data), or a list of tuples, each tuple containing a string (the block name) and an integer (the param2 value the Minetest block should have).

- ID_TO_NAME looks up all-caps names from numeric block ID.

Enjoy!

S.D.G.
