from flask import Flask,jsonify,send_file,request
import logging as lg
import time
from db_query import get_path_details

lg.basicConfig(level="DEBUG")
app=Flask(__name__)

# @app.route("/get_tables/<string:table_name>", methods = ['GET'])
# def get_routes(table_name):
#     print(table_name)
#     return jsonify({"message":"getting tables"})


@app.route('/<path:path>', methods = ['GET'])
def get_routes(path):
    try:
        data = get_path_details(path)
    except Exception as e:
        data = "failed to retrive data"
    return jsonify({"message": data})

if(__name__== "__main__"):
    lg.debug("Starting Flask Server")
    app.run(host="0.0.0.0",port=9000,debug=True)
