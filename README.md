# 📦 Smart Logistics System 🚚

## 🔍 Overview

The **Smart Logistics System** is a web-based application that uses AI-based decision logic to recommend the most efficient transport method for delivering goods.

It helps users choose the best option based on:

* Distance 📍
* Weight ⚖️
* Priority ⏱️

The system also provides cost comparison and route visualization.

---

## 🚀 Features

* ✅ Multiple delivery support
* 🤖 AI-based transport recommendation
* 💰 Cost comparison using charts
* 🗺️ Route visualization using Google Maps
* 📊 Interactive UI for better decision-making
* 🔄 Dynamic form generation using JavaScript

---

## 🧠 How It Works

1. User selects a **start city**
2. Adds one or more deliveries
3. Enters:

   * Product type
   * Destination city
   * Weight
   * Priority
4. System:

   * Calculates distance (Haversine formula)
   * Recommends transport method (AI logic)
   * Shows cost comparison
5. User selects transport
6. Final output shows:

   * Delivery plan
   * Total cost
   * Route on map

---

## 🤖 AI Logic Used

The system uses a **rule-based AI model**:

* High priority → Flight ✈️
* Distance > 1200 km → Flight ✈️
* Heavy goods → Train 🚆
* Medium → Truck 🚚
* Local → Bike 🏍

This ensures a balance between **speed, cost, and efficiency**.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **Maps:** Google Maps API
* **Deployment:** Render

---

## 📁 Project Structure

```
smart-logistics-system/
│
├── app.py
├── Procfile
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── choose.html
│   ├── result.html
│
├── static/
│   └── style.css
```

---
## 🌐 Live Demo

👉 (Add your Render link here after deployment)

---

## ⚠️ Note

* Google Maps requires a valid API key to display routes
* Replace `YOUR_API_KEY` in the code before deployment

---

## 🔮 Future Improvements

* 📡 Real-time traffic integration
* 🤖 Machine learning-based prediction
* 📦 Warehouse and inventory integration
* 📍 Live shipment tracking
* 💳 Payment integration

---

## 📌 Use Cases

* Logistics companies (DHL, Amazon, etc.)
* Supply chain optimization
* Delivery planning systems
* E-commerce platforms

---

## 👨‍💻 Authors

* Srirama Manaswin Nanda Vardhan
* Nellimarla Bhavesh

---

## ⭐ Conclusion

This project demonstrates how AI-based decision-making can improve logistics efficiency by optimizing cost, time, and resource usage.

---
