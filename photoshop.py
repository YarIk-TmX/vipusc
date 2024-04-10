from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
import os
from PIL import ImageFilter

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.image_path = None
        self.save_dir = 'modifilied/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        self.image_path = os.path.join(dir, filename)
        self.image = Image.open(self.image_path)
    def showImage(self, parth):
        img_lbl.hide()
        piximage = QPixmap(parth)
        w, h = img_lbl.width(), img_lbl.height()
        piximage = piximage.scaled(w, h)
        img_lbl.setPixmap(piximage)
        img_lbl.show()    
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_zerkalo(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_pravo(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_levo(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blure(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_kontur(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

app2 =QApplication([])
win2 = QWidget()
win2.resize(700, 500)
win2.setWindowTitle('Абоба')
#------------------------------
dir_btn = QPushButton('папка')
left_btn = QPushButton('лево')
right_btn = QPushButton('право')
mirror_btn = QPushButton('зеркало')
rez_btn = QPushButton('блюр')
bw_btn = QPushButton('ч/б')
o_btn = QPushButton('контур')
#-------------------------------
img_lbl = QLabel('картинка')
imgs_list = QListWidget()
#-------------------------------
main_line = QHBoxLayout()
btns_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
#---------------------------------
btns_line.addWidget(left_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(mirror_btn)
btns_line.addWidget(rez_btn)
btns_line.addWidget(bw_btn)
btns_line.addWidget(o_btn)
v_line1.addWidget(dir_btn)
v_line1.addWidget(imgs_list)
v_line2.addWidget(img_lbl)
v_line2.addLayout(btns_line)

main_line.addLayout(v_line1)
main_line.addLayout(v_line2)
win2.setLayout(main_line)
#---------------------------------
workdir = ''

workImage = ImageProcessor()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
def openFolder():
    global workdir
    extensions = ['.jpg', '.png', '.jpeg', '.bnp', '.gif']
    workdir = QFileDialog.getExistingDirectory()
    file_list = os.listdir(workdir)
    filenames = filter(file_list, extensions)
    imgs_list.clear()
    imgs_list.addItems(filenames)

def openImage():
    filename = imgs_list.currentItem().text()
    workImage.loadImage(workdir, filename)
    workImage.showImage(workImage.image_path)

o_btn.clicked.connect(workImage.do_kontur)
rez_btn.clicked.connect(workImage.do_blure)
left_btn.clicked.connect(workImage.do_levo)
right_btn.clicked.connect(workImage.do_pravo)
mirror_btn.clicked.connect(workImage.do_zerkalo)
bw_btn.clicked.connect(workImage.do_bw)
dir_btn.clicked.connect(openFolder)
imgs_list.itemClicked.connect(openImage)




