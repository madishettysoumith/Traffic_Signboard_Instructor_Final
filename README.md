# Traffic Signboard Instructor

## Introduction

Traffic signs are essential components of road infrastructure, providing crucial information for safe navigation. Misinterpretation or lack of awareness about these signs can lead to road accidents and safety issues. Our project, **Traffic Signboard Instructor**, is a comprehensive AI-powered system designed to address these challenges.

### Key Features:
- **Recognition and Learning**: Enable users to recognize and learn about traffic signs using a robust image recognition model trained with a Convolutional Neural Network (CNN).
- **Secure and User-Friendly Design**: Offer a secure platform with user authentication and an admin dashboard for seamless management of functionalities.
- **Seamless Deployment**: Deploy the application on **Hugging Face Spaces**, making it accessible, scalable, and easy to use.

## Core Functionalities:
1. **User Authentication**: Secure login and user registration.
2. **Admin Dashboard**: Manage users and system settings.
3. **Image Upload & Traffic Sign Recognition**: Upload images and get predictions for traffic sign recognition.
4. **Informational Display**: View information about the recognized traffic signs.
5. **Deployment**: Hosted on **Hugging Face Model Hub** for scalable access.

## Details on CNN and Model Training

### Convolutional Neural Networks (CNN)
CNN is a type of deep learning model specifically designed for analyzing visual data, such as images. It mimics how the human brain processes visual information, using layers of filters to automatically detect patterns like edges, shapes, and textures in images. These patterns are then combined in later layers to recognize more complex structures, such as traffic signs.

### Technologies Used

- **Convolutional Neural Networks (CNN)**: Used to extract features from images, enabling accurate classification of traffic signs.
- **Keras**: Simplifies the development and training of deep learning models.
- **Machine Learning Frameworks**: Built using libraries for efficient training and deployment.
- **Data Handling and Preprocessing**:
  - **Pandas & NumPy**: Managed and processed large datasets for model training.
  - **Data Augmentation Libraries**: Applied techniques like rotation, scaling, and flipping to enhance model robustness.

- **Web Development Framework**:
  - **Django**: The backbone of the application, handling user authentication, the admin dashboard, and traffic sign upload functionalities. It enables rapid development of secure web applications.

## Evaluation Criteria

The project was evaluated across four key milestones:
1. Successful implementation of **user authentication** and an **admin dashboard**.
2. Accurate **traffic sign classification** using the trained CNN.
3. Functional and **user-friendly interface** with seamless image upload and sign recognition.
4. Integration of AI and web technologies for a secure, scalable, and intuitive platform.

## Technologies Used
- **Python**: Programming language for model development and web application.
- **Django**: Web framework for backend and user authentication.
- **Keras**: Deep learning framework for CNN model development.
- **TensorFlow**: For model training and deployment.
- **Hugging Face Spaces**: Platform for deployment.

## Screenshots

- **Homepage**: The landing page for the Traffic Signboard Instructor project.
- **Login and Signup Page**: User registration and login.
- **Upload Page**: Users can upload an image of a traffic sign for recognition.
- **Welcome Page**: After login, users are directed to the dashboard with available functionalities.

## Future Enhancements
- **Real-time Video Processing**: Improve the system by adding real-time traffic sign recognition via video processing.
- **Mobile App Integration**: Build a mobile app to increase accessibility.

## Conclusion

The **Traffic Signboard Instructor** project successfully demonstrates the integration of AI and web technologies to address real-world challenges in traffic sign recognition. By leveraging CNN for accurate image classification and deploying the model on Hugging Face Spaces, we created a scalable, user-friendly, and secure platform. The project not only enhances road safety awareness but also showcases the practical application of machine learning in education and automation.

## License

This project is licensed under the MIT License.

