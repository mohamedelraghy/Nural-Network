from tkinter import *
from PIL import Image, ImageTk
import os


class GUI:
    def __init__(self, trainning_function, prediction_function, change_weights_function):

        # ---------- Parameter functions ----------

        self.trainning_function = trainning_function
        self.prediction_function = prediction_function
        self.change_weights_function = change_weights_function

        # ---------- Root main window ----------

        self.root = Tk()
        self.root.geometry("851x640")

        # ---------- Image Label ----------

        self.display = Label(self.root)
        self.set_image("pics/example1.png")
        self.display.grid(row=0, column=0)

        # ---------- Train button ----------

        trainButton = Button(self.root, text="train",
                             command=self.train)
        trainButton.grid(row=1, column=1, rowspan=2)

        # ---------- Predict button ----------

        predictButton = Button(self.root, text="predict",
                               command=self.predict)
        predictButton.grid(row=1, column=2, rowspan=2)

        # ---------- Weights List Box ----------

        self.weightListBox = Listbox(self.root, selectmode=SINGLE)
        self.weightListBox.grid(row=0, column=1)

        # ---------- Pictures List Box ----------
        self.picturesListBox = Listbox(self.root, selectmode=SINGLE)
        for pic in self.get_available_images():
            self.picturesListBox.insert(0, pic)
        self.picturesListBox.bind("<Double-Button-1>", self.change_image)
        self.picturesListBox.grid(row=0, column=2)

        # ---------- Show the window ----------
        self.root.mainloop()

    def update_weight(self, newWeight):
        newWeight = self.change_weights_function()
        self.weightListBox.insert(0, newWeight)

    def change_image(self, event):
        selectedImage = self.picturesListBox.selection_get()
        print("Changing image to " + selectedImage)
        imagePath = "pics/" + selectedImage
        self.set_image(imagePath)

    def set_image(self, imagePath):
        self.original = Image.open(imagePath)
        resized = self.original.resize((400, 600), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.config(image=self.image)

    def get_available_images(self):
        return os.listdir("./pics")

    def train(self):
        self.trainning_function()

    def predict(self):
        self.prediction_function()
