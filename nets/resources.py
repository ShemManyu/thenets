from flask import request
from flask_restful import Resource

chatgroups = {
    'group1': {
        'message1': {'from': 'user1', 'message': 'Hey guys'},
        'message2': {'from': 'user2', 'message': 'Hey user1'}
    },
    'group2': {
        'message1': {'from': 'user1', 'message': 'Hey guys too'},
        'message2': {'from': 'user2', 'message': 'Hey user1 too'} 
    }
}

conversations = {
    'conversation1': {
        'message1': {'from': 'user2', 'message': 'Hey user1'},
        'message2': {'from': 'user2', 'message': 'Hey user1'}
    }
}

class ChatGroup(Resource):
    def get(self, group_id):
        #serialize group messages and return them here
        return chatgroups[group_id]
    
    def post(self, group_id):
        message = request.form['message']
        userid = request.form['user']
        message_id = int(max(chatgroups[group_id].keys()).lstrip('message')) + 1
        message_id = 'message%i' %message_id
        chatgroups[group_id][message_id] = {
            'from': userid,
            'message': message 
        }
        return chatgroups[group_id]

class Conversation(Resource):
    def get(self, conversation_id):
        return conversations[conversation_id]
    
    def post(self, conversation_id):
        message = request.form['message']
        userid = request.form['user']
        message_id = int(max(conversations[conversation_id].keys()).lstrip('message')) + 1
        message_id = 'message%i' %message_id
        conversations[conversation_id][message_id] = {
            'message': message,
            'from': userid
        }
        return conversations[conversation_id]
