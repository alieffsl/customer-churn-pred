from flask import Flask, jsonify
import pandas as pd
import firebase_admin
from firebase_admin import credentials
import os
from google.cloud import firestore
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./vps-cc-firebase-adminsdk-bel2b-6d712e79bc.json"
db = firestore.Client()

customer_ref = db.collection('customers')
segmented_full_ref = db.collection('segmentation full')
segmented_ref = db.collection('segmentation')
rules_ref = db.collection('rules')

def grab_df(collection):
    users = list(db.collection(collection).stream())
    users_dict = list(map(lambda x: x.to_dict(), users))
    df = pd.DataFrame(users_dict)
    return df

customer_df = grab_df('customers')
customer_df = customer_df[['Customer ID', 'Tenure Months', 'Location', 'Device Class', 'Games Product', 'Music Product', 'Education Product', 'Call Center', 'Video Product', 'Use MyApp', 'Payment Method', 'Monthly Purchase (Thou. IDR)', 'Churn Label', 'Longitude', 'Latitude', 'CLTV (Predicted Thou. IDR)']]
customer_df = customer_df.sort_values(by=['Customer ID'], ascending=True)

segmented_full_df = grab_df('segmentation full')
segmented_full_df = segmented_full_df[['Model', 'Churn Label', 'Segment', 'Characteristics', 'Marketing']]

segmented_df = grab_df('segmentation')
segmented_df = segmented_df[['Model', 'Churn Label', 'Segment', 'Characteristics', 'Marketing']]

rules_df = grab_df('rules')
rules_df = rules_df[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

def refresh_dataframes():
    global customer_df, segmented_full_df, segmented_df, rules_df
    customer_df = grab_df('customers')
    customer_df = customer_df[['Customer ID', 'Tenure Months', 'Location', 'Device Class', 'Games Product', 'Music Product', 'Education Product', 'Call Center', 'Video Product', 'Use MyApp', 'Payment Method', 'Monthly Purchase (Thou. IDR)', 'Churn Label', 'Longitude', 'Latitude', 'CLTV (Predicted Thou. IDR)']]
    customer_df = customer_df.sort_values(by=['Customer ID'], ascending=True)

    segmented_full_df = grab_df('segmentation full')
    segmented_full_df = segmented_full_df[['Model', 'Churn Label', 'Segment', 'Characteristics', 'Marketing']]

    segmented_df = grab_df('segmentation')
    segmented_df = segmented_df[['Model', 'Churn Label', 'Segment', 'Characteristics', 'Marketing']]

    rules_df = grab_df('rules')
    rules_df = rules_df[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

def on_snapshot(col_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == 'ADDED' or change.type.name == "MODIFIED" or change.type.name == 'REMOVED':
            refresh_dataframes()

customer_watch = customer_ref.on_snapshot(on_snapshot)
segmented_full_watch = segmented_full_ref.on_snapshot(on_snapshot)
segmented_watch = segmented_ref.on_snapshot(on_snapshot)
rules_watch = rules_ref.on_snapshot(on_snapshot)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/customers')
def get_customers_json():
    return jsonify(customer_df.to_json(orient='records')) 

@app.route('/segmentfull')
def get_segmented_full_json():
    return jsonify(segmented_full_df.to_json(orient='records')) 

@app.route('/segment')
def get_segmented_json():
    return jsonify(segmented_df.to_json(orient='records')) 

@app.route('/rules')
def get_rules_json():
    return jsonify(rules_df.to_json(orient='records')) 

if __name__ == "__main__":
    app.run(debug=True)