import os
import firebase_admin
from firebase_admin import credentials, firestore, auth

file_path = os.getenv("SERVICE_FILE")
cred = credentials.Certificate(file_path)
app = firebase_admin.initialize_app(cred)


def get_number_from_uid(uid):
    try:
        number = auth.get_user(uid).phone_number
        if number:
            return number
        else:
            ''
    except:
        return ''




def write_to_db(collection_name, data, doc_name=''):
    db = firestore.client()
    try:
        if doc_name:
            document_ref = db.collection(collection_name).document(doc_name)
        else:
            document_ref = db.collection(collection_name).document()
        document_ref.set(data)
        return document_ref.id
    except Exception as e:
        raise e


def read_doc_with_id(collection_name,doc_name):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name).document(doc_name)
        doc = doc_ref.get()
        return doc.to_dict()
    except Exception as e:
        raise e


def read_doc_with_filter(collection_name, filter_field, filter_with):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name)
        out = doc_ref.where(filter_field, u'==', filter_with).get()
        return out
    except Exception as e:
        raise e


def read_doc_with_2_filter(collection_name, filter_field, filter_with, filter_field_1, filter_with_1):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name)
        out = doc_ref.where(filter_field, u'==', filter_with).where(filter_field_1, u'==', filter_with_1).get()
        return out[0].to_dict()
    except Exception as e:
        print("Fetch error 1: ", e)
        raise e


def readDocWithOutDocName(collection_name):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name).stream()
        return doc_ref
    except:
        return 0


def read_doc_with_list(collection_name, filter_field, filter_list):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name)
        out = doc_ref.where(filter_field, u'in', filter_list).stream()
        return out
    except Exception as e:
        raise e


def update_db(collection_name, doc_name, dict_value):
    db = firestore.client()
    try:
        doc_ref = db.collection(collection_name).document(doc_name)
        doc_ref.update(dict_value)
        return 1
    except Exception as e :
        print(e)
        return 0

