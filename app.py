import json

# AWS SNS configuration
AWS_REGION = 'ap-south-1'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
SNS_TOPIC_ARN = ''

# Initialize AWS SNS client
sns_client = boto3.client('sns', region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Dash app initialization
app = dash.Dash(__name__)
server = app.server
# Define app layout
app.layout = html.Div([
    html.H1('Form App'),
    html.Div([
        html.Label('Name:'),
        dcc.Input(id='name-input', type='text'),
    ], style={'marginBottom': 10}),
    html.Div([
        html.Label('Email:'),
        dcc.Input(id='email-input', type='email'),
    ], style={'marginBottom': 10}),
    html.Div([
        html.Button('Submit', id='submit-button'),
    ]),
    html.Div(id='output-message')
])


# Callback function to send form data to SNS topic
@app.callback(Output('output-message', 'children'),
              [Input('submit-button', 'n_clicks')],
              [Input('name-input', 'value'), Input('email-input', 'value')])
def send_form_data_to_sns(n_clicks, name, email):
    if n_clicks is not None and name and email:
        # Construct message
        message = {"Name" : name, "Email": email}

        # Publish message to SNS topic
        response = sns_client.publish(TopicArn=SNS_TOPIC_ARN,
                                      Message= json.dumps(message))

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return html.Div('Form submitted successfully')
        else:
            return html.Div('Error submitting form.')
    else:
        return html.Div('Please fill in all form fields')
                                                                                                                                                                                                                                                          32,9          Bot
