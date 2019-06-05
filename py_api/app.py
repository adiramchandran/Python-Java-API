from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd 
import numpy as np

app = Flask(__name__)

# add get, put, delete later
@app.route('/predict', methods=['POST'])
def predict():
	if lr:
		try:
			json_ = request.json
			print(json_)
			input = pd.get_dummies(pd.DataFrame(json_))
			input = input.reindex(columns=model_columns, fill_value=0)
			prediction = list(lr.predict(input))
			return jsonify({'predction': str(prediction)})
		except:
			return jsonify({'trace': traceback.format_exc()})
	else:
		print('model has not been trained yet')
		return ('empty model')


if __name__ == '__main__':
	try:
		port = int(sys.argv[1])
	except:
		port = 12345

	lr = joblib.load('model.pkl')
	print('loaded model')
	model_columns = joblib.load('model_columns.pkl')
	print('loaded columns')
	app.run(port=port, debug=True)



'''
USER REQUESTS:
----python----
url = 'insert_url'
params = {'input': 'enter input'}
response = requests.get(url, params)
response.json()
----terminal----
curl -X GET insert_url -d input='insert input'
'''

