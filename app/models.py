from app import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    id_no = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    account_type = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    middle_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    prefix = db.Column(db.String(5), nullable=True)
    suffix = db.Column(db.String(7), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_number = db.column(db.String(18), nullable=False)
    petitions = db.relationship('Petition', backref='user', lazy=True)

class Petition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    place_of_birth = db.Column(db.String(100), nullable=False)
    
    spouse_first_name = db.Column(db.String(50), nullable=False)
    spouse_middle_name = db.Column(db.String(50), nullable=False)
    spouse_last_name = db.Column(db.String(50), nullable=False)
    spouse_citizenship = db.Column(db.String(50), nullable=False)

    philippine_address = db.Column(db.String(200), nullable=False)
    residence_address = db.Column(db.String(200), nullable=False)
    home_telephone_no = db.Column(db.String(20))
    email_address = db.Column(db.String(100), nullable=False)
    work_telephone_no = db.Column(db.String(20))
    present_occupation = db.Column(db.String(100))
    work_address = db.Column(db.String(200))

    #other fields located the form_routes.py

    children = db.relationship('PetitionChild', backref='petition', lazy=True, cascade="all, delete-orphan")


class PetitionChild(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petition_id = db.Column(db.Integer, db.ForeignKey('petition.id'), nullable=False)
    
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))
    civil_status = db.Column(db.String(20))
    dob = db.Column(db.Date)
    pob = db.Column(db.String(100))
    cpa = db.Column(db.String(100))
    citizenship = db.Column(db.String(50))
    supporting_docs = db.Column(db.String(200))
    immigration_docs = db.Column(db.Sting(200))

class OverseasCitizenship(db.Model):
    entry_no = db.Column(db.Integer, db.ForeignKey('applicant.entry_no'), primary_key=True)
    foreign_citizenship_id = db.Column(db.Integer, primary_key=True)
    foreign_citizenship = db.Column(db.String(50), nullable=False)
    acquisition_foreign_citizenship = db.Column(db.String(100), nullable=False)
    date_acquisition = db.Column(db.Date, nullable=False)
    naturalization_numbers = db.Column(db.String(50))
    foreign_passport_no = db.Column(db.String(50))
    date_issuance = db.Column(db.Date)
    place_issuance = db.Column(db.String(100))
    foreign_acquisition_docs = db.Column(db.String(200))


class FamilyMember(db.Model):
    entry_no = db.Column(db.Integer, db.ForeignKey('applicant.entry_no'), nullable=False)
    family_id = db.Column(db.Integer, primary_key=True)
    relation = db.Column(db.String(50), nullable=False)
    family_name = db.Column(db.String(100), nullable=False)
    family_citizenship = db.Column(db.String(50), nullable=False)


class SpouseDetails(db.Model):
    family_id = db.Column(db.Integer, db.ForeignKey('family_member.family_id'), primary_key=True)
    spouse_address = db.Column(db.String(200), nullable=False)


class PhilippineCitizenship(db.Model):
    ph_citizenship_id = db.Column(db.Integer, db.ForeignKey('applicant.ph_citizenship_id'), primary_key=True)
    mode_ph_acquisition = db.Column(db.String(100), nullable=False)
    ph_docs = db.Column(db.String(200))
