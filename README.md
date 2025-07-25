# Safe Sphere - Crime Awareness Platform

Safe Sphere is a comprehensive crime awareness and safety platform designed to help users stay informed about local crime statistics, report incidents, and access emergency services. The platform combines a modern React frontend with a robust Flask backend to provide a seamless user experience.

## 🌟 Features

### 🎯 Core Functionality
- **Real-time Crime Monitoring**: Track and visualize crime data in your area
- **Emergency SOS Services**: Quick access to emergency contacts and police services
- **FIR Registration**: Online First Information Report filing system
- **AI-Powered Chatbot**: Get instant assistance and crime-related information
- **User Authentication**: Secure login and profile management
- **Crime Analytics**: Detailed statistics and trend analysis

## 🚀 Technology Stack

### Frontend (Client)
- **React.js**: Modern component-based UI framework
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework for responsive design
- **JavaScript/JSX**: Interactive user interface components
- **MapBox Integration**: Interactive maps for crime visualization

### Backend (Server)
- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **RESTful APIs**: Clean and scalable API architecture
- **AI Integration**: ChatBot with retrieval-augmented generation
- **Python**: Core backend logic

## 📱 User Interface Overview

### 🏠 Home Page
*[Space for Home Page Screenshot]*

The landing page provides an overview of the platform features with intuitive navigation to different sections. Users can quickly access emergency services, view recent crime statistics, and navigate to various features.

Key Elements:
- Hero section with platform introduction
- Quick access buttons for emergency services
- Recent crime statistics dashboard
- Navigation menu for all features

### 🔐 Authentication System

#### Sign In Page
*[Space for Sign In Screenshot]*

Secure user authentication with:
- Email/username login
- Password authentication
- Remember me functionality
- Forgot password option

#### Sign Up Page
*[Space for Sign Up Screenshot]*

User registration with:
- Personal information collection
- Email verification
- Password strength validation
- Terms and conditions acceptance

### 👤 User Profile Dashboard
*[Space for Profile Dashboard Screenshot]*

Personalized user interface featuring:
- User profile information
- Recent activities
- Saved locations
- Emergency contacts management
- Preference settings

### 🚨 SOS Emergency Services

#### Emergency Dashboard
*[Space for SOS Dashboard Screenshot]*

Critical emergency features including:
- One-click emergency buttons
- Nearest police station locator
- Emergency contact quick dial
- Location sharing with authorities

#### Police Services Map
*[Space for Police Map Screenshot]*

Interactive map showing:
- Nearby police stations
- Real-time location tracking
- Distance and route information
- Contact details for each station

### 📊 Crime Statistics & Analytics

#### Crime Data Visualization
*[Space for Crime Analytics Screenshot]*

Comprehensive crime data display:
- Interactive charts and graphs
- Crime type categorization
- Temporal trend analysis
- Geographic crime mapping

#### Crime Clusters Map
*[Space for Crime Clusters Screenshot]*

Advanced mapping features:
- Crime hotspot identification
- Cluster analysis visualization
- Safety level indicators
- Time-based filtering

### 📝 FIR Registration System

#### FIR Form Selection
*[Space for FIR Selection Screenshot]*

Multiple FIR types available:
- Theft complaints
- Cybercrime reports
- Missing person reports
- Domestic violence cases
- Motor vehicle theft
- Other criminal activities

#### FIR Form Interface
*[Space for FIR Form Screenshot]*

Detailed form interface with:
- Step-by-step guidance
- Document upload capability
- Progress tracking
- Form validation
- Draft saving functionality

### 🤖 AI Chatbot Assistant

#### Chat Interface
*[Space for Chatbot Screenshot]*

Intelligent chatbot features:
- Natural language processing
- Crime-related query handling
- Emergency guidance
- Legal information assistance
- 24/7 availability

### ℹ️ About Us Page
*[Space for About Us Screenshot]*

Information about the platform:
- Mission and vision
- Team information
- Platform objectives
- Safety commitment

### 📞 Contact Page
*[Space for Contact Screenshot]*

Get in touch section:
- Contact form
- Office locations
- Phone and email details
- Social media links
- Support hours

## 🏗️ Project Structure

```
Safe-sphere/
├── README.md
├── .gitignore
├── client/                     # Frontend React Application
│   ├── public/
│   │   ├── crime_clusters.csv
│   │   └── crime_data.csv
│   ├── src/
│   │   ├── App.jsx            # Main application component
│   │   ├── main.jsx           # Application entry point
│   │   ├── index.css          # Global styles
│   │   ├── config.js          # Configuration settings
│   │   ├── assets/            # Images and static files
│   │   └── components/        # React components
│   │       ├── Home.jsx       # Home page component
│   │       ├── AboutUs.jsx    # About us page
│   │       ├── Contact.jsx    # Contact page
│   │       ├── FirRegister.jsx # FIR registration
│   │       ├── Satistical.jsx # Statistics page
│   │       ├── sos.jsx        # Emergency services
│   │       ├── pages/         # Page-specific components
│   │       │   ├── Chabot/    # AI chatbot components
│   │       │   ├── FIRS_Component/ # FIR-related components
│   │       │   ├── Home_Page_components/ # Home page sections
│   │       │   ├── profile_components/ # User profile components
│   │       │   ├── sos_components/ # Emergency service components
│   │       │   └── Statics_components/ # Analytics components
│   │       └── ui/            # Reusable UI components
│   ├── package.json           # Frontend dependencies
│   ├── vite.config.js         # Vite configuration
│   └── tailwind.config.js     # Tailwind CSS configuration
└── server/                    # Backend Flask Application
    ├── run.py                 # Application entry point
    ├── requirements.txt       # Python dependencies
    ├── package.json           # Node.js dependencies
    └── app/                   # Flask application
        ├── __init__.py        # App initialization
        ├── config.py          # Configuration settings
        ├── models.py          # Database models
        ├── utils.py           # Utility functions
        └── routes/            # API routes
            ├── app_bot/       # AI chatbot logic
            ├── fir_route_register/ # FIR registration APIs
            ├── profile_route/ # User profile APIs
            ├── sos_route/     # Emergency service APIs
            └── data/          # Data files and datasets
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- Git

### Frontend Setup
```bash
# Navigate to client directory
cd client

# Install dependencies
npm install

# Start development server
npm run dev
```

### Backend Setup
```bash
# Navigate to server directory
cd server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
```

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout

### Emergency Services
- `GET /api/sos/police-stations` - Get nearby police stations
- `POST /api/sos/emergency-alert` - Send emergency alert
- `GET /api/sos/crime-data` - Get crime data for area

### FIR Management
- `POST /api/fir/register` - Register new FIR
- `GET /api/fir/status/:id` - Check FIR status
- `GET /api/fir/forms` - Get available FIR forms

### Crime Analytics
- `GET /api/analytics/crime-stats` - Get crime statistics
- `GET /api/analytics/clusters` - Get crime clusters
- `GET /api/analytics/trends` - Get crime trends

### Chatbot
- `POST /api/bot/query` - Send query to AI chatbot
- `GET /api/bot/suggestions` - Get suggested queries

## 🛡️ Security Features

- **Data Encryption**: All sensitive data is encrypted
- **Secure Authentication**: JWT-based authentication system
- **Input Validation**: Comprehensive input sanitization
- **Rate Limiting**: API rate limiting to prevent abuse
- **CORS Protection**: Cross-origin request security

## 📊 Data Sources

- Crime statistics from public databases
- Police station information
- Emergency service contacts
- Geographic crime data
- User-generated reports

## 🤝 Contributing

We welcome contributions to make Safe Sphere better! Please read our contributing guidelines before submitting pull requests.

### Development Guidelines
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Contact our support team
- Check the documentation

## 🚀 Future Enhancements

- Mobile application development
- Real-time notifications
- Advanced AI features
- Multi-language support
- Integration with more emergency services
- Enhanced data visualization

---

*Safe Sphere - Making communities safer through technology and awareness.*
