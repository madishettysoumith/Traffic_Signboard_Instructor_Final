# TRAFFIC SIGNBOARD INSTRUCTOR

Traffic Signboard Instructor is an intelligent web application developed using Django that enables users to upload images of traffic signs and receive accurate classifications. This system is designed to assist learners preparing for driving tests, educators conducting road safety sessions, and anyone looking to better understand traffic signage.

The platform not only identifies traffic signs from uploaded images but also displays their official meaning, helping users to learn about them visually and interactively. It comes with user authentication, an admin dashboard, and simple navigation—all aimed at delivering an educational yet seamless experience.

---

## FEATURES

- **Image Upload and Prediction:** Users can upload traffic sign images, and the system will classify them using a trained model.
- **Meaning Display:** Along with the predicted class, the description and official meaning of the sign is presented.
- **User Authentication:** Signup, login, logout, and password reset functionality using secure email-based authentication.
- **Admin Dashboard:** A backend interface for administrators to view statistics, monitor user activity, and manage image predictions.
- **Email Notification:** Password reset and account-related notifications are sent via Gmail using Django's email configuration.
- **Database Storage:** Image data, predictions, and user information are stored in an SQLite database for simplicity and portability.

---

## TECHNOLOGIES USED

- **Backend:** Python 3, Django Framework
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite3
- **Image Handling:** Python Imaging Library (PIL), optional integration with OpenCV or TensorFlow for image classification
- **Email:** SMTP configuration with Gmail
- **Development Tools:** Git, VS Code, Django Admin Panel

---

## INSTALLATION INSTRUCTIONS

### STEP 1: Clone the Repository
First, download the source code to your local machine.

