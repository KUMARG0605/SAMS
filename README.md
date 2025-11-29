# 📚 Student Attendance Management System 

A web-based attendance management system built with Flask and SQL Server for managing student and faculty attendance at **Rajiv Gandhi University of Knowledge Technologies (RGUKT), Andhra Pradesh**.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2025-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 👨‍🎓 Student Portal
- **User Registration** - Students can register with ID, email, and select their subjects
- **Secure Login** - Password-protected authentication with hashed passwords
- **Dashboard** - View attendance statistics with interactive pie charts
- **Profile Management** - View and update profile information
- **Subject-wise Attendance** - Track attendance for each enrolled subject
- **Password Reset** - Email-based password recovery system

### 👨‍🏫 Faculty Portal
- **Faculty Registration** - Register with faculty ID and select teaching subjects
- **Attendance Management** - Mark student attendance by subject and date
- **Bulk Operations** - Mark multiple students absent/present at once
- **Branch-wise Management** - Manage students by department/branch

### 🔐 Security Features
- Password hashing using Werkzeug security
- SQL injection prevention with parameterized queries
- Session management for user authentication
- Secure password reset via email tokens

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python, Flask |
| Database | Microsoft SQL Server 2025 Express |
| Frontend | HTML5, CSS3, Bootstrap 4 |
| Charts | Plotly, Matplotlib, Seaborn |
| Authentication | Werkzeug Security |

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- Microsoft SQL Server 2019/2022/2025 Express
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/KUMARG0605/SAMS.git
   cd SAMS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database Connection**
      Edit `app.py` and update the connection strings

5. **Setup Database**
   ```bash
   python setup_db.py
   ```
6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 🎯 Usage

### For Students
1. Register with your university ID and email
2. Select your semester, branch, and subjects
3. Login to view your attendance dashboard
4. Check subject-wise attendance with visual charts

### For Faculty
1. Register with your faculty ID
2. Select the subjects you teach
3. Login to access the attendance portal
4. Mark attendance by selecting subject, date, and absent students
## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**KUMAR G**
- GitHub: [@KUMARG0605](https://github.com/KUMARG0605)

## 🙏 Acknowledgments

- Rajiv Gandhi University of Knowledge Technologies (RGUKT-AP)
- Plotly for interactive charts

## 📞 Contact

For any queries or support:
- 📧 Email: kumar03.rkvalley@gmail.com
- 📱 Phone: +91 9392513416

---

⭐ **Star this repository if you found it helpful!**
