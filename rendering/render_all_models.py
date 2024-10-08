import os
import argparse

parser = argparse.ArgumentParser(description='Renders glbs')
parser.add_argument(
    '--save_folder', type=str, default='/home/jtremblay/code/mvs_objaverse/output/',
    help='path for saving rendered image')
parser.add_argument(
    '--folder_assets', type=str, default='/home/jtremblay/.objaverse/hf-objaverse-v1/glbs/',
    help='path to downloaded 3d assets')
parser.add_argument(
    '--blender_root', type=str, default='/home/jtremblay/Desktop/blender-3.2.0-alpha+master.e2e4c1daaa47-linux.x86_64-release/blender',
    help='path to blender executable')
opt = parser.parse_args()



# get all the file
import glob 
data = sorted(glob.glob(f"{opt.folder_assets}/*/"))

for path in data:
    # path = data[-5]
    path = sorted(glob.glob(path + "/*.glb"))[0]

    render_cmd = '%s -b -P /kaggle/working/mvs_objaverse/rendering/render_blender.py -- --obj %s --output %s --views 12 --resolution 224 > tmp.out' % (
        opt.blender_root, path, opt.save_folder
    )
    print(render_cmd)
    os.system(render_cmd)
    break
