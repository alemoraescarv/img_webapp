from flask import Flask, render_template, request
import sys
sys.path.append("tests")
import get_vm_list 




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    project = request.form.get('project')
    print(project)
    try:
        details=get_vm_list.list_all_instances(project)
        print(details)
    except:
        details = "Error: check the project ID - it might be wrong or the project doesnt exist in GCP"
        print("error")

    #print(project)

    return render_template('index.html', project=project, details=details)



if __name__ == '__main__':
    app.run()