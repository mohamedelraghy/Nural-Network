from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from main import *
from my_tools import *


class GUI:
    def __init__(self):

        # ---------- Parameter functions ----------
        self.train_x_orig, self.train_y, self.test_x_orig, self.test_y, self.classes = load_data()
        print(self.train_x_orig.shape)

        # ---------- Root main window ----------
        self.trained = False
        self.current_immage = 50
        self.root = Tk()
        self.root.title("Cat classifier")
        self.root.geometry("731x403")
        self.v = StringVar()
        # ---------- Image Label ----------

        self.display = Label(self.root)
        self.set_image("50")
        self.display.grid(row=0, column=0, rowspan=5)

        # ---------- Weights Label ----------

        self.weightsLabel = Label(self.root, text='Costs')
        self.weightsLabel.grid(row=0, column=1)

        # ---------- acuticy Label ----------
        self.v.set("")
        self.acurcyLabel = Label(self.root, textvariable=self.v)

        self.acurcyLabel.grid(row=2, column=1)

        # ---------- Weights List Box ----------

        self.weightListBox = Listbox(self.root, selectmode=SINGLE, width=25)
        self.weightListBox.grid(row=1, column=1)

        # ---------- pictures Label ----------

        self.picturesLabel = Label(self.root, text='pictures')
        self.picturesLabel.grid(row=0, column=2)

        # ---------- Pictures List Box ----------

        self.picturesListBox = Listbox(self.root, selectmode=SINGLE, width=15)
        for pic in range(1, 51):
            self.picturesListBox.insert(END, pic)
        self.picturesListBox.bind("<Double-Button-1>", self.change_image)
        self.picturesListBox.grid(row=1, column=2)

        # ---------- Train button ----------

        trainButton = Button(self.root, text="train",
                             command=self.train)
        trainButton.grid(row=4, column=1, rowspan=2)

        # ---------- Predict button ----------

        predictButton = Button(self.root, text="predict",
                               command=self.predict)
        predictButton.grid(row=4, column=2, rowspan=2)

        # ---------- Show the window ----------
        self.root.mainloop()

    def change_image(self, event):
        selectedImage = self.picturesListBox.selection_get()
        print(selectedImage)
        print("Changing image to " + selectedImage)
        self.current_immage = int(selectedImage);
        self.set_image(selectedImage)

    def set_image(self, imagePath):
        self.original = Image.fromarray(self.test_x_orig[int(imagePath) - 1], mode='RGB')
        resized = self.original.resize((400, 400), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.config(image=self.image)

    def get_available_images(self):
        return os.listdir("./pics")

    def add_costs(self, new_cost):
        self.weightListBox.insert(0, new_cost)

    def train(self):
        print("Training!")
        self.trained=True
        (self.parameters, self.test_x, self.pred_train, self.pred_test) = train(self)
        strtment = "training set accuracy = " + self.pred_train[:5] + "\ntest set accuracy = " + self.pred_test[:5]
        print(strtment)
        self.v.set(strtment)
        print("koko")
        plt.show()

    def predict(self):
        if self.trained:
            print("predicting")
            prid = predict_one_image(self.test_x[:, self.current_immage - 1].reshape(self.test_x.shape[0], 1),
                                     self.parameters)
            if prid == 1:
                prid = "a Cat"
            else:
                prid = "not a Cat"
            messagebox.showinfo(title="prediction for image number" + str(self.current_immage),
                                message="this image is " + prid)
        else: messagebox.showerror(title="untrained error", message="you have to train the model befor use it")