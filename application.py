import gooeypie as gp
import numpy as np
import cv2
from program import import_image
from program import process_image

image = None

x = 1

def browse_path(event):
    file_path = browse_image_win.open()
    global image
    image = import_image(file_path)
    scan_button.disabled = False
    

def scan(event):
    global image
    img =  image
    global x
    process_image(img, x)
    scan_button.disabled = True
    
def smooth_change(event):
   if (check.checked == True):
        global x
        x = 0
   else: 
        x =  1
    

app = gp.GooeyPieApp('Barcdode scanner')

app.width = 400
app.height = 200

app.resizable_horizontal = False
app.resizable_vertical = False



browse_image_win = gp.OpenFileWindow(app, 'Browse image')
browse_image_win.set_initial_folder('desktop')

browse_button = gp.Button(app, 'Browse..', browse_path )
choose_directory_label = gp.StyleLabel(app, 'Browse for image:')
app.set_grid(5, 5) 
app.add(choose_directory_label, 1, 1, align='center')
app.add(browse_button, 1, 2, align ='center')
choose_directory_label.font_name = 'Comic Sans'
choose_directory_label.font_size = 10
browse_button.width = '15'

scan_button = gp.Button(app, 'Scan', scan)
app.add(scan_button, 2, 2, align ='center')
scan_button.width = '15'
scan_button.disabled = True

check = gp.Checkbox(app, 'White area noise remove')
app.add(check, 3, 2, align = 'center' )
check.add_event_listener('change', smooth_change)

app.run()
