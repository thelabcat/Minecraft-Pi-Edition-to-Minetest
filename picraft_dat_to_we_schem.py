#Convert MCPi picraft block list to Minetest WorldEdit schematic file
#S.D.G.

"""
In both games, up is +Y
In Minetest, North is +Z and East is +X
In Minecraft, North is -Z and East is +X
"""

from block_table import ID_TO_NAME, TRANSLATE
from picraft import *
import pickle

#picraft lists are ordered zxy by default

in_fn=input("Enter path to dat file: ")
if in_fn[-4:]!=".dat":
    in_fn+=".dat"
print("Reading...")
f=open(in_fn, "rb")
blocklist=pickle.load(f)
try:
    startvec=pickle.load(f)
    stopvec=pickle.load(f)
    veclist=vector_range(startvec, stopvec)
except EOFError:
    veclist=""
    while len(veclist)!=len(blocklist):
        startvec=eval("Vector("+input("Enter x, y, z of lowest value corner in Minecraft: ")+")")
        stopvec=eval("Vector("+input("Enter x, y, z of highest value corner in Minecraft: ")+")")
        veclist=vector_range(startvec, stopvec)
        if len(veclist)!=len(blocklist):
            print("Size mismatch: Vector range is length", len(veclist), "while block list is length", len(blocklist))

f.close()

out_fn=input("Enter path to .we output file: ")
if out_fn[-3:]!=".we":
    out_fn+=".we"



print("Start vector is", startvec)
print("Stop vector is", stopvec)
offsetvec=eval("Vector("+input("Enter x, y, z of desired offset from 0 in Minetest: ")+")")

"""
WorldEdit schematic files (*.we) look like this:

5:r1="default:stone";return \
{{x=0,y=0,z=0,name=r1},\
{x=0,y=1,z=0,name=r1},\
{x=0,y=2,z=0,name="default:dirt_with_grass",param2=999}}
"""

print("Converting to WorldEdit schematic...")
we_text="5:r1=\"default:stone\";return {"

unsupported=[]
for i in range(len(blocklist)):
    if blocklist[i].id==0:
        continue
    try:
        lookup=TRANSLATE[ID_TO_NAME[blocklist[i].id]]
    except KeyError:
        if blocklist[i] not in unsupported:
            print(blocklist[i], "not supported")
            unsupported.append(blocklist[i])
    param2=0
    if type(lookup)==str:
        name=lookup
    elif type(lookup[blocklist[i].data%len(lookup)])==str:
        try:
            name=lookup[blocklist[i].data%len(lookup)]
        except IndexError:
            print(lookup, blocklist[i])
            name=lookup[0]
    else:
        try:
            name, param2=lookup[blocklist[i].data%len(lookup)]
        except IndexError:
            print(lookup, blocklist[i])
            name, param2=lookup[0]
    if name=="default:air":
        continue
    we_text+="{x=%i,y=%i,z=%i,name=\"%s\",param2=%i}," % (veclist[i].x+offsetvec.x, veclist[i].y+offsetvec.y, -veclist[i].z+offsetvec.z, name, param2)

we_text=we_text[:-1]+"}"

f=open(out_fn, "w")
f.write(we_text)
f.close()
print("Done!")
