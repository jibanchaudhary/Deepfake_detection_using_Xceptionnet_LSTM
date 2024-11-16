# **AI-Generated Fake Video Detector**

The AI-Generated Fake Video Detector is a web application designed to identify AI-generated manipulated videos by the implementation of Deep learning Techniques Like Xceptionnet and LSTM, commonly known as deepfakes. By leveraging advanced deep learning techniques, this tool helps combat misinformation and promote trustworthy visual content online.

---

## **Features**

- **High Accuracy**: Achieves an **86.25% overall accuracy** using XceptionNet and LSTM.
- **Real-Time Analysis**: Quick detection with low latency.
- **User-Friendly**: Intuitive interface for seamless interaction.
- **Scalable**: Handles a large volume of videos efficiently.

---

## **System Workflow**

1. **Input Module**:  
   Accepts video files for analysis.

2. **Pre-Processing Module**:  
   - Extracts frames from video files.  
   - Resizes frames for uniform processing.

3. **Processing Module**:  
   ### **Models Used**  
   - **XceptionNet**:  
     - Extracts spatial features from individual frames.  
     - Uses depthwise separable convolutions for computational efficiency.  
   - **LSTM (Long Short-Term Memory)**:  
     - Extracts temporal features across frames.  
     - Effectively handles sequential data, identifying patterns over time.  

4. **Output Module**:  
   Delivers results, categorizing videos as **Real** or **Fake**.

---

## **Results**

### **Performance Metrics**
- **Model Accuracy**: 86.25%  
- **Testing Accuracy**: 83.87%  

### **Visualizations**

1. **Model Loss**
   
   ![Model Loss](https://github.com/user-attachments/assets/f4da678b-f28f-4a70-a91e-82b72ecb0bd8)  

3. **Model Accuracy**
   
   ![Model Accuracy](https://github.com/user-attachments/assets/e9fe98e8-8947-42da-abbf-68225e304f28)  

4. **Testing Loss and Accuracy**
   
   ![Testing Loss and Accuracy](https://github.com/user-attachments/assets/e67efdeb-0c3c-4d30-83a4-63d66c3128d8)  

---

## **Output Examples**

- **Real Video**:
  
  ![Real Video](https://github.com/user-attachments/assets/24b7f3ff-160d-49f4-b07f-a9bb4c28a7d9)  

- **Fake Video**:
  
  ![Fake Video](https://github.com/user-attachments/assets/508690fe-2d59-4067-81a3-9fb1453b65fe)  

---
### **License**
This project is licensed under the MIT License. Feel free to modify and enhance it!





   
   

