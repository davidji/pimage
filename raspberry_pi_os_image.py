
import json
import subprocess

def get_removable_block_devices():
    process = subprocess.run(
        "/usr/bin/lsblk --json --tree".split(), 
        capture_output=True, text=True)

    lsblk_json = json.loads(process.stdout)
    return { device['name']: device for device in lsblk_json['blockdevices'] if device.get('rm', False) }

def unmount_all(device):
    mountpoints = [ mountpoint 
        for mountpoint in child.get('mountpoints', [])
        if mountpoint 
        for child in device.get('children', [])]
    if len(mountpoints):
        subprocess.run(['/usr/bin/umount'] + mountpoints)

def prepare_sdcard(devname = None):
    devices = get_removable_block_devices()
    if devname:
        device = devices[devname]
    elif len(devices) == 1:
        device = devices.values()[0]
    else:
        raise Exception("Multiple devices: {} please specify device".format(devices.keys))
    unmount_all(device)

print(prepare_sdcard())
