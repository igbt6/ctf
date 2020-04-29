# Ext Super Magic

__PROBLEM__

We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the [filesystem](https://2018shell.picoctf.com/static/9f563e291d847c30879277c3b6c16260/ext-super-magic.img) out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_2_5e1f8bfb15060228f577045924e4fca8 on the shell server.

__HINT__

Are there any [tools](https://en.wikipedia.org/wiki/Fsck) for diagnosing corrupted filesystems? What do they say if you run them on this one?
How does a linux machine know what [type](https://www.garykessler.net/library/file_sigs.html) of [file](https://linux.die.net/man/1/file) a file is?
You might find this [doc](http://www.nongnu.org/ext2-doc/ext2.html) helpful.
Be careful with [endianness](https://en.wikipedia.org/wiki/Endianness) when making edits.
Once you've fixed the corruption, you can use /sbin/[debugfs](https://linux.die.net/man/8/debugfs) to pull the flag file out.

__SOLUTION__

```
wget  https://2018shell.picoctf.com/static/9f563e291d847c30879277c3b6c16260/ext-super-magic.img --no-check-certificate

```

Following the hint, let's try to use `e2fsck` tool, which you can use to check the integrity of Linux file system.
`e2fsck` tool specifically checks ext2, ext3 or ext4 file systems.

```
$ e2fsck ext-super-magic.img
e2fsck 1.44.1 (24-Mar-2018)
ext2fs_open2: Bad magic number in super-block
e2fsck: Superblock invalid, trying backup blocks...
e2fsck: Bad magic number in super-block while trying to open ext-super-magic.img

The superblock could not be read or does not describe a valid ext2/ext3/ext4
filesystem.  If the device is valid and it really contains an ext2/ext3/ext4
filesystem (and not swap or ufs or something else), then the superblock
is corrupt, and you might try running e2fsck with an alternate superblock:
    e2fsck -b 8193 <device>
 or
    e2fsck -b 32768 <device>
```

The info which `e2fsck` gave us clearly stated: "Bad magic number in super-block".
From the hints i know the file system in the image file is ext2 (Ext SuperMagic II-class).
Googling a bit for superblock of ext2 i found: https://wiki.osdev.org/Ext2#Superblock
"The Superblock is always located at byte 1024 from the beginning of the volume and is exactly 1024 bytes in length."
I also fund that magic number is at offset 56 bytes in superblock Ext2 signature (0xef53), used to help confirm the presence of Ext2 on a volume.

Run the `solver.py` script which fixes magic number and try to mount it then to see the flag:

```
$ python3 solver.py
$ mkdir mounted
$ sudo mount ext-super-magic-fixed.img mounted
$ ls mounted/ | grep flag
flag.jpg
$ pix mounted/flag.jpg
```

Read the flag from the photo :)


FLAG - `picoCTF{ab0CD63BC762514ea2f4fc9eDEC8cb1E}`
