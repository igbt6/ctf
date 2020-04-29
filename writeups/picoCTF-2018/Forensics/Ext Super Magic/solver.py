
EXT2_IMG       = "ext-super-magic.img"
EXT2_IMG_FIXED = "ext-super-magic-fixed.img"

EXT2_SUPERBLOCK_OFFSET           = 0x400  # EXT2_SUPERBLOCK_OFFSET bytes
EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET = 0x38   # EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET bytes

EXT2_MAGIC_NUMBER = b"\x53\xef"

'''
    1st way
'''
# Read the magic number
with open(EXT2_IMG, "rb") as ext2_img:
    ext2_img.seek(EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET)  # seek to super block + magic number offset
    print(ext2_img.read(2)) #MAGIC number


# Fix the magic number
import shutil
shutil.copy2(EXT2_IMG, EXT2_IMG_FIXED)

with open(EXT2_IMG_FIXED, "r+b") as ext2_img:
    ext2_img.seek(EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET)  # seek to super block + magic number offset
    ext2_img.write(EXT2_MAGIC_NUMBER)


# Read the magic number
with open(EXT2_IMG_FIXED, "rb") as ext2_img:
    ext2_img.seek(EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET)  # seek to super block + magic number offset
    print(ext2_img.read(2)) # MAGIC number


'''
    2nd way with pwn
'''
# from pwn import *

# with open(EXT2_IMG, 'rb') as ext2_img:
#     data = ext2_img.read()

# print(enhex(data[EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET : EXT2_SUPERBLOCK_OFFSET+EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET+2]))

# data = data[: EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET] + p16(0xEF53) + data[EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET+2 :]

# print(enhex(data[EXT2_SUPERBLOCK_OFFSET + EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET : EXT2_SUPERBLOCK_OFFSET+EXT2_SUPERBLOCK_MAGIC_NUM_OFFSET+2]))

# with open(EXT2_IMG_FIXED, 'wb') as ext2_img:
#     ext2_img.write(data)