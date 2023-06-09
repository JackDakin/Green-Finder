import os
from Modules import detectGreen as dg

# directories

## in this part, you input the source and destination directories you want to use.
## it then steps through everything in the sourece directory, applies do_makemask, and outputs B/w images to dst dir

src_dir = r'C:\Users\jackf\Pictures\PFR PLANT CODING\Additional Work 19.07\2.Cropped'
dst_dir = r'C:\Users\jackf\Pictures\PFR PLANT CODING\Additional Work 19.07\3.Mask'


for current_dir, dirname, filename in os.walk(src_dir):
    print(f"\n{current_dir}\n{dirname}\n{filename}")

    destination_dir = current_dir.replace(src_dir, dst_dir)
    print(destination_dir)

    for file in filename:
        print(file)

        dg.do_makemask(file, current_dir, destination_dir)






