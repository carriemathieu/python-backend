from flask import Flask, jsonify, request, json

app = Flask(__name__) 

employeeArray = [
    {
        "id":1, 
        "employee_name":"Tiger Nixon", 
        "employee_salary":320800, 
        "employee_age":61
    }, {
        "id":2, 
        "employee_name":"Garrett Winters", 
        "employee_salary":170750, 
        "employee_age":63
    }, {
        "id":3, 
        "employee_name":"Ashton Cox", 
        "employee_salary":86000, 
        "employee_age":66
}]

# *** GET endpoint ***
def show(id):
    # - takes as input an employee’s ID 
    # print('Name: ', person.get('id', id))
    return # the matching employee’s name, salary, and age in JSON.

# *** GET endpoint ***
@app.route('/', methods=['GET'])
def index():
    # sorted- higher order function that takes function as argument (lambda)
    sortedEmployeeArray = sorted(employeeArray, key=lambda k: k['employee_salary']) 
    return jsonify(sortedEmployeeArray)

# *** POST endpoint *** 
def create():
    # takes as input a JSON object containing the following fields:
    # - employee_name
    # - employee_salary
    # - employee_age
    # employeeArray.append{id: a, "employee_name": blah, "employee_salary": blah, "employee_age": blah}
    return {'201' : 'employee created successfully'}

if __name__ == '__main__':
    app.run(debug=True)