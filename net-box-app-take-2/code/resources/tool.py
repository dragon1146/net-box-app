from flask_restful import Resource, reqparse, request
from flask import Flask, jsonify
from models.tool import ToolModel




class Tool(Resource):
    def get(self):
        data = request.get_json()
        tool_task = data['task']
        tool = ToolModel.find_tool_by_task(tool_task)
        return jsonify({'id':tool.id, 'manufacture':tool.manufacture, 'device':tool.device, 'task':tool.task, 'command':tool.command, 'notes':tool.notes})
       
        # return {'Tool': task}

    def post(self):
        data = request.get_json()
        new_tool_obj = ToolModel(data['manufacture'], data['device'], data['task'], data['command'], data['notes'])
        add_new_tool_to_db = new_tool_obj.add_tool_to_db()        
        return jsonify({'id':add_new_tool_to_db.id, 'manufacture':add_new_tool_to_db.manufacture, 'device':add_new_tool_to_db.device, 'task':add_new_tool_to_db.task, 'command':add_new_tool_to_db.command, 'notes':add_new_tool_to_db.notes})