from flask import Flask, Blueprint, jsonify, request, render_template
import logging
import pandas as pd
import sys
import json
import time
import boto3
import decouple
from io import StringIO

logging.basicConfig(level=logging.DEBUG)

flask_app = Flask(__name__)

tables = Blueprint('tables', __name__, url_prefix='/tables')

# df with the number of cells of each label in each dataset
df = pd.read_csv(flask_app.open_resource('df.csv'))

# convert df to dict for sending as json to datatables
dict_df = df.to_dict(orient='records')

# convert column names into dict for sending as json to datatables
columns = [{"data": item, "title": item} for item in df.columns]


@tables.route("/clientside_table", methods=['GET'])
def clientside_table_content():
    return jsonify({'data': dict_df, 'columns': columns})


flask_app.register_blueprint(tables)


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/clientside_table")
def clientside_table():
    return render_template("clientside_table.html")


@flask_app.route('/submit', methods=['POST', 'GET'])
def receive_submission():
    print('buuu')
    # answer is a dict of json strings containing selected row and column index numbers
    answer = request.form.to_dict(flat=False)
    print(answer)

    # need to convert the json strings to dict, then to a data frame
    # data1 is the selection for the first group, data2 for the second
    data1 = json.loads(answer['data1'][0])
    data1_df = pd.DataFrame.from_dict(data1[0])

    print(data1_df)
    data2 = json.loads(answer['data2'][0])
    data2_df = pd.DataFrame.from_dict(data2[0])

    # now map the index number to experiment name and cell type name
    group1_df = pd.DataFrame()
    group1_df['cell_type1'] = data1_df['row'].map(df['Cell type label'])
    group1_df['experiment1'] = data1_df['column'].map(pd.Series(df.columns.values))
    print(group1_df)

    group2_df = pd.DataFrame()
    group2_df['cell_type2'] = data2_df['row'].map(df['Cell type label'])
    group2_df['experiment2'] = data2_df['column'].map(pd.Series(df.columns.values))
    print(group2_df)

    email = answer['email'][0].strip()
    print(email)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)

    s3filename = 'submissions/' + email + '%' + timestr + '.csv'

    selected_groups_df = pd.concat([group1_df, group2_df], axis=1)
    print(selected_groups_df)

    AWS_S3_ACCESS_KEY = decouple.config('AWS_S3_ACCESS_KEY')
    AWS_S3_SECRET = decouple.config('AWS_S3_SECRET')

    csv_buffer = StringIO()
    selected_groups_df.to_csv(csv_buffer)

    client = boto3.client('s3',
                          aws_access_key_id=AWS_S3_ACCESS_KEY,
                          aws_secret_access_key=AWS_S3_SECRET
                          )
    client.put_object(
        Body=csv_buffer.getvalue(),
        Bucket='scvi-differential-expression',
        Key=s3filename,
        ACL='public-read'
    )
    print('the objeoct has been put')
    print(s3filename)

    ec2 = boto3.resource('ec2')

    user_data = '''#!/bin/bash
    echo 'test' > /tmp/hello'''

    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0fc20dd1da406780b',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        UserData=user_data,
        KeyName='ec2-keypair'
    )

    print('the instance has been created')


    return 'derpderp'
