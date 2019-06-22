import subprocess

from colour import Color


#get primary color from pywal values
color = subprocess.check_output(['grep', 'color1:', '/home/cta/.Xresources'])
color = color.decode().rstrip().split(' ')
print(color)
color = color[-1]

primary_col = Color(color)
print(primary_col.get_saturation(), primary_col.hex)
primary_col.set_saturation(primary_col.get_saturation() - .01)
print(primary_col.get_saturation(), primary_col.hex)
