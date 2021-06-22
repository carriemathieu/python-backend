from flask import Flask, jsonify, request, json

app = Flask(__name__) 

employeeList = [
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

@app.route('/api/<int:id>', methods=['GET'])
def show(id):
    # loops over each dictionary in employeeList- if ID matches from url params, return JSON version of employee
    for employee in employeeList:
        if employee["id"] == id:
            return jsonify(employee)

@app.route('/api', methods=['GET'])
def index():
    # sorted- higher order function that takes function as argument (lambda)
    sortedEmployeeList = sorted(employeeList, key=lambda k: k['employee_salary'], reverse=True)
    # converts to json 
    return jsonify(sortedEmployeeList)

@app.route('/api/create', methods=['POST']) 
def create():
    # takes as input a JSON object containing the following fields:
    # - employee_name
    # - employee_salary
    # - employee_age
    # employeeArray.append{id: a, "employee_name": blah, "employee_salary": blah, "employee_age": blah}
    return {'201' : 'employee created successfully'}

if __name__ == '__main__':
    app.run(debug=True)