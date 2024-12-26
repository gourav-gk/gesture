# Gesture Click Project 🎥🤚📸

## Overview 🌟✨📖

**Gesture Click** is an innovative web application that simplifies and makes image capturing and sharing fun. Using hand gestures, users can effortlessly capture live camera images and share them across devices connected to the same network. 🎉

This project includes features like:

- A **Home Page** displaying a gallery of images that can be shared.
- A **Receiver Page** to detect hand gestures and display received images.
- A **Gesture Click Page** to capture images with hand gestures. 🤩

---

## Features and Functionalities 🎯💡🛠️

### **1. Home Page (/home)** 🏠🖼️📂

- Displays a grid gallery of images.
- Allows users to share an image from the gallery.
- Simple and user-friendly interface. 😊

### **2. Receiver Page (/receive)** 📥🤖👀

- Detects a user’s hand using a live camera feed.
- Checks for shared images sent by someone on the same network.
- Displays the received image if available.
- Deletes the image from the database after it is displayed to ensure clean data handling. 🧹

### **3. Gesture Click Page (/camera)** 🎥✋📸

- Uses a live camera feed to detect hand gestures.
- Captures an image 1 second after detecting a "hand close" gesture.
- Uploads the captured image to the media folder.
- Saves the image details in the database for sharing. 🗂️

---

## Benefits 🏆👍💼

- **Simplified Interaction**: Capture and share images using just hand gestures. 🙌
- **Effortless Connectivity**: Share images between devices connected to the same network. 🌐
- **User-Friendly**: Intuitive and easy-to-navigate interfaces. 🖱️
- **Innovative**: Eliminates the need for physical buttons or additional hardware for image capturing. 🤖

---

## Setup and Installation 🛠️💻⚙️

### **1. Prerequisites** 📋🔧

- Python (3.8 or higher)
- Django (latest version)
- A web browser
- Devices connected to the same local network 🌐

### **2. Clone the Repository** 📂📥

```bash
git clone https://github.com/gourav-gk/gesture_share.git
cd gesture_project
```

### **3. Install Dependencies** 📦⚙️

```bash
pip install -r requirements.txt
```

### **4. Configure the Database** 🗂️🛢️

Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Start the Development Server** 🚀🌍

Run the server on your local IP:

```bash
python manage.py runserver
```

### **6. Access the Application** 🌐📲

Open a web browser and navigate to:

- **Home Page**: `http://<your-local-ip>:8000/home`
- **Gesture Click Page**: `http://<your-local-ip>:8000/camera`
- **Receiver Page**: `http://<your-local-ip>:8000/receive` 🎥

---

## How to Use 🤓📖💡

### **Gesture Click Page (/camera)** ✋📸⏳

1. Open the Gesture Click page.
2. Show your hand to the live camera feed.
3. Make a "hand close" gesture to capture an image.
4. The image will be uploaded and saved in the database. 🖼️

### **Home Page (/home)** 🖼️📤🎯

1. View the gallery of images.
2. Click on an image to share it.
3. Shared images will be stored in the database for the receiver to access. 🌐

### **Receiver Page (/receive)** 📥✋📷

1. Open the Receiver page.
2. Show your hand (with an "open hand" gesture) to the live camera feed.
3. If an image is shared by a sender on the same network, it will display the image. 🖼️
4. Once displayed, the image is deleted from the database. 🗑️

---

## Future Enhancements 🔮🚀💭

- Extend functionality for devices connected across different networks. 🌐
- Add real-time notifications for image sharing. 🔔
- Improve hand gesture detection for diverse scenarios. ✋🤖

---

## Contribution 🤝💻🌟

We welcome contributions from the community! 🌍 If you want to enhance the project or fix bugs, feel free to:

1. Fork the repository on GitHub.
2. Make your changes in a new branch.
3. Submit a pull request with a clear explanation of your updates.

Your contributions will help improve the project for everyone. 🙏

---

## License 📜⚖️🔓

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as the original license is included in all copies or substantial portions of the software. 🛠️

