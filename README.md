# Secure Medical Data Transmission with Paillier Homomorphic Encryption

## Project Overview

This project is a web application built with **Flask** and **Firebase**, focusing on secure data transmission between patients and doctors using **Paillier Homomorphic Encryption**. The application allows patients to send their medical analysis results to a chosen doctor, and the doctor can provide diagnoses. All data remains encrypted throughout the process, ensuring privacy and security during storage and transmission via Firebase.

## Features

- **Patient-Doctor Communication**:
  - Patients send encrypted medical analysis data to a doctor of their choice.
  - Doctors respond with encrypted diagnoses without needing to decrypt the original data.
  
- **Paillier Homomorphic Encryption**:
  - This form of encryption allows operations to be performed on encrypted data (e.g., adding values) without decrypting the data first.
  
- **Firebase Integration**:
  - **Firebase Realtime Database** is used to securely store and manage encrypted data.
  - Firebase Authentication manages the login process for both patients and doctors.

- **Flask Backend**:
  - Flask manages server-side functionality, user requests, and interactions between patients and doctors.
  - Paillier encryption is used to ensure privacy during all stages of data transmission and processing.

## Technologies Used

- **Flask**: To handle the web server and routing.
- **Firebase**:
  - **Realtime Database**: For secure storage of encrypted data.
  - **Firebase Authentication**: To manage patient and doctor login.
- **Paillier Homomorphic Encryption**:
  - Used to encrypt sensitive medical data so that computations can be performed directly on the encrypted data.
- **Python Libraries**: For encryption and secure data handling.

## Data Flow

1. **Patient Interaction**:
   - The patient logs in.
   - The patient enters their medical analysis information.
   - The data is encrypted using Paillier Homomorphic Encryption before being sent to Firebase.
   - The encrypted data is stored in Firebase under the chosen doctor's records.

2. **Doctor Interaction**:
   - The doctor logs in and retrieves the encrypted data.
   - The doctor can perform diagnostic computations directly on the encrypted data using Paillier encryption.
   - The diagnostic result is encrypted and sent back to the patient via Firebase.

3. **Data Storage**:
   - All data is stored in Firebase in its encrypted form, ensuring that no sensitive data is ever exposed in plain text, even in storage.

## Paillier Homomorphic Encryption

The **Paillier cryptosystem** is used in this project because it supports addition and scalar multiplication of encrypted values without needing to decrypt them. This makes it suitable for securely handling medical data in a privacy-preserving way.

### Key Features:
- Homomorphic addition of ciphertexts.
- Scalar multiplication of ciphertexts.

