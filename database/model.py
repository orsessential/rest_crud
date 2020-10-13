#author -- orsessential
from .db import db

class Ordering(db.Document):
    transaction_id = db.StringField(required=True, max_length=50)
    customer_name = db.StringField(required=True, max_length=100)
    customer_code = db.StringField(required=True)
    transaction_amount = db.StringField(required=True)
    transaction_discount = db.StringField(required=True)
    transaction_payment_type = db.StringField(required=True)
    transaction_additional_field = db.StringField(required=True)
    transaction_state = db.StringField(required=True)
    transaction_code = db.StringField(required=True)
    transaction_order = db.IntField(required=True)
    location_id = db.StringField(required=True)
    organization_id = db.IntField(required=True, max_length=50)
    created_at = db.StringField(required=True)
    updated_at = db.StringField(required=True)
    transaction_payment_type_name = db.StringField(required=True)
    transaction_cash_amount = db.IntField(required=True)
    transaction_cash_change = db.IntField(required=True)
    customer_attribute = db.DictField(required=True)
    connote = db.DictField(required=True)
    connote_id = db.StringField(required=True, max_length=50)
    origin_data = db.DictField(required=True)
    destination_data = db.DictField(required=True)
    koli_data = db.ListField(required=True)
    custom_field = db.DictField(required=False)
    currentLocation = db.DictField(required=True)




