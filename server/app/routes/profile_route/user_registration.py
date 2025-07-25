from flask import Blueprint, request, jsonify
from app.models import db, User
from datetime import datetime
import os
import requests

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()

        required_fields = ['name', 'email', 'phone', 'address', 'aadharNumber', 'role', 'dateOfBirth', 'emergencyContact', 'emergencyContactPhone', 'clerkUserId']

        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400

        clerk_user_id = data['clerkUserId']
        existing_user = User.query.filter_by(clerk_user_id=clerk_user_id).first()
        if existing_user:
            return jsonify({'error': 'User already registered'}), 400

        existing_aadhar = User.query.filter_by(aadhar_number=data['aadharNumber']).first()
        if existing_aadhar:
            return jsonify({'error': 'Aadhar number already registered'}), 400

        if len(data['aadharNumber']) != 12 or not data['aadharNumber'].isdigit():
            return jsonify({'error': 'Invalid Aadhar number. Must be 12 digits'}), 400

        if data['role'] not in ['civilian', 'police']:
            return jsonify({'error': 'Invalid role'}), 400

        try:
            dob = datetime.strptime(data['dateOfBirth'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format for date of birth'}), 400

        new_user = User(
            clerk_user_id=data['clerkUserId'],
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            aadhar_number=data['aadharNumber'],
            role=data['role'],
            date_of_birth=dob,
            emergency_contact_name=data['emergencyContact'],
            emergency_contact_phone=data['emergencyContactPhone'],
            registration_date=datetime.utcnow(),
            status='active'
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': 'User registered successfully',
            'user_id': new_user.id,
            'role': new_user.role
        }), 201

    except Exception as e:
        db.session.rollback()
        print("🔥 ERROR:", e)
        return jsonify({'error': f'Registration failed: {str(e)}'}), 500

@user_bp.route('/profile/check/<clerk_user_id>', methods=['GET'])
def check_user_profile(clerk_user_id):
    try:
        user = User.query.filter_by(clerk_user_id=clerk_user_id).first()

        if user:
            return jsonify({
                'exists': True,
                'profile_completed': True,
                'role': user.role,
                'user_data': {
                    'name': user.name,
                    'email': user.email,
                    'phone': user.phone,
                    'role': user.role,
                    'registration_date': user.registration_date.isoformat() if user.registration_date else None
                }
            }), 200
        else:
            return jsonify({
                'exists': False,
                'profile_completed': False
            }), 200

    except Exception as e:
        return jsonify({'error': f'Failed to check profile: {str(e)}'}), 500

@user_bp.route('/profile/update/<clerk_user_id>', methods=['PUT'])
def update_user_profile(clerk_user_id):
    try:
        user = User.query.filter_by(clerk_user_id=clerk_user_id).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.get_json()

        allowed_fields = ['name', 'phone', 'address', 'emergency_contact_name', 'emergency_contact_phone']

        for field in allowed_fields:
            if field in data:
                setattr(user, field, data[field])

        user.updated_at = datetime.utcnow()
        db.session.commit()

        return jsonify({
            'message': 'Profile updated successfully',
            'user_id': user.id
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Update failed: {str(e)}'}), 500

# NEW ROUTE TO UPDATE CLERK METADATA
@user_bp.route('/profile/update-metadata/<clerk_user_id>', methods=['POST'])
def update_clerk_metadata(clerk_user_id):
    try:
        CLERK_API_KEY = os.environ.get("CLERK_SECRET_KEY")
        if not CLERK_API_KEY:
            return jsonify({'error': 'Missing Clerk API Key'}), 500

        data = request.get_json()
        metadata = {
            "public_metadata": {
                "role": data.get("role"),
                "profileCompleted": True
            }
        }

        response = requests.patch(
            f"https://api.clerk.dev/v1/users/{clerk_user_id}",
            headers={
                "Authorization": f"Bearer {CLERK_API_KEY}",
                "Content-Type": "application/json"
            },
            json=metadata
        )

        if response.status_code != 200:
            return jsonify({"error": "Failed to update metadata"}), 400

        return jsonify({"message": "Metadata updated"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
