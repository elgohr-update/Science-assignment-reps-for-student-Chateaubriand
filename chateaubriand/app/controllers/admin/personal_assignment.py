from flask import request
from flask_restful import Resource

from chateaubriand.app.views.admin.personal_assignment import PersonalAssignmentView
from chateaubriand.app.util.token_checker import available_token
from chateaubriand.app.util.param_checker import param_validate, GET_ASSIGNMENT_JSON

class PersonalAssignment(Resource):
    @param_validate(GET_ASSIGNMENT_JSON)
    @available_token
    def get(self):
        print(request.args.keys())
        personal_assignment_view = PersonalAssignmentView(request.args.get('class'))
        view = personal_assignment_view.get_view()
        return view
