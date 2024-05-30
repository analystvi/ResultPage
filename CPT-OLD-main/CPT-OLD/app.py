from flask import Flask, render_template, request
import pandas as pd
import college_predictor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    marks = int(request.form['Cut-off'])
    course = request.form['course']
    caste = request.form['Community']
    
    # Load your dataset
    data = pd.read_csv('E:\\1_MAIN PROJECTS\\CPT-OLD\\Data_final_1.csv')
    
    # Process the data using your function from college_predictor.py
    filtered_colleges = college_predictor.list_of_colleges(marks, course, caste, data)
    
    # Pass the filtered colleges data to the results template
    return render_template('results.html', filtered_colleges=filtered_colleges.to_dict(orient='records'), caste=caste)

if __name__ == '__main__':
    app.run(debug=True)
