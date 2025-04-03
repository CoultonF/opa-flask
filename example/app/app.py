from flask import Flask, request, jsonify, logging
import requests
import json

app = Flask(__name__)
OPA_URL = "http://opal_client:8181"  # When running in Docker


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_endpoint(subpath):
    # Prepare the input for OPA
    opa_input = {
        "input": {
            "method": request.method,
            "city_id": 1,
            "path": ['api', *subpath.split('/')],
            "user": request.headers.get('X-User', ''),  # Get user from header
        }
    }
    # curl --request GET 'http://opal_client:8181/v1/data/cities' --header 'Content-Type: application/json' | python -m json.tool
    # Query OPA for authorization decision
    opa_response = requests.post(
        f"{OPA_URL}/v1/data/example/allow",
        data=json.dumps(opa_input),
        headers={"Content-Type": "application/json"}
    )
    
    # Check if request is allowed
    if opa_response.status_code == 200:
        result = opa_response.json()
        if result.get("result", False):
            # Request is authorized
            return jsonify({
                "message": f"Access granted to {subpath}",
                "method": request.method,
                "user": request.headers.get('X-User', '')
            })
        else:
            # Request is not authorized
            return jsonify({
                "error": "Access denied",
                "reason": "Unauthorized"
            }), 403
    else:
        # Error communicating with OPA
        return jsonify({
            "error": "Authorization service error",
            "details": opa_response.text
        }), 500

# Example protected endpoints that match your policy
@app.route('/api/public', methods=['GET'])
def public_api():
    # This will be authorized for everyone according to your policy
    # But we'll still go through the authorization check
    return api_endpoint('public')

@app.route('/api/data', methods=['GET'])
def data_api():
    # This will only be authorized for admin users according to your policy
    return api_endpoint('data')