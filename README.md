# mini-social-media
Starting step towards my Data Science career. A mini social media app made using pure Python.
# 🧠 Social Network Recommendation Engine

This Python project analyzes social network data and recommends:
- **People you may know** (based on mutual friends)
- **Pages you might like** (based on shared interests)

All data is processed from a JSON file representing users, their friends, and liked pages — like a simplified version of Facebook's recommendation system.

---

## 📂 Project Structure


---

## ⚙️ Features

✅ Cleans and preprocesses raw JSON data  
✅ Removes duplicate friends and pages  
✅ Filters out inactive users  
✅ Suggests new friends based on **mutual connections**  
✅ Suggests new pages based on **similar interests**

---

## 🔁 How It Works

### 🔍 people_user_may_know(user_id, data)
Returns a list of user IDs who are *not direct friends* but have the *most mutual friends* with the given user.

### 📄 pages_user_might_like(user_id, data)
Returns a list of page IDs that similar users liked but the current user hasn't, *ranked by interest overlap*.

---
