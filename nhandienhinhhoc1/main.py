import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from keras.models import load_model


model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = [line.strip() for line in open("labels.txt")]

class WebcamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nhận diện hình ảnh vật thể ")

        self.camera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        self.label = tk.Label(root, text="", font=("Helvetica", 16))
        self.label.pack()

        self.update()

    def update(self):
        ret, image = self.camera.read()

        if ret:
            image = cv2.resize(image, (640, 480))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(image))
            self.canvas.create_image(0, 0, anchor='nw', image=self.photo)

            prediction = self.predict_image(image)
            self.label.config(text=prediction)

        self.root.after(10, self.update)

    def predict_image(self, image):
        resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        image_array = np.asarray(resized_image, dtype=np.float32).reshape(1, 224, 224, 3)
        normalized_image = (image_array / 127.5) - 1

        prediction = model.predict(normalized_image)
        index = np.argmax(prediction)
        class_name = class_names[index][2:]

        return f"Dự đoán: {class_name}"

    def quit_app(self):
        self.camera.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    root.mainloop()
    cv2.destroyAllWindows()
