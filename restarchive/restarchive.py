from flask import Flask
from flask import request
from flask import make_response
from archiveManager import ArchiveManager
import json

app = Flask(__name__)


@app.route('/')
def usage():
    return 'USAGE: Issue a POST with JSON data to /{postID}/archive'

@app.route('/<postID>/archive', methods=['GET', 'POST'])
def archive(postID):
    if request.method == 'POST':
        archiveManager = ArchiveManager()
        dic = request.get_json(True)
        if archiveManager.archiveData(postID, json.dumps(dic)):
            return make_response('SUCCESS')
        else:
            return make_response('Failed to archive data')
    else:
        return 'GET not yet supported'


if __name__ == '__main__':
    app.run(debug=True)
