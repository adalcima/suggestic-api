import os

from flask import Flask, jsonify, request


app = Flask(__name__)


def flatten_nested_sequence(items):
    flattened = []
    for element in items:
        if isinstance(element, (list, tuple)):
            flattened.extend(flatten_nested_sequence(element))
        else:
            flattened.append(element)
    return flattened


@app.route('/flatten', methods=['POST'])
def flatten_api():
    try:
        payload = request.get_json()
        return jsonify({'result': flatten_nested_sequence(payload['items'])})

    except KeyError:
        return jsonify({'message': 'ERROR: Incorrect input data'}), 400

    except TypeError:
        return jsonify({'message': 'ERROR: Unexpected error'}), 500

    except Exception as error:
        return jsonify({'message': f'ERROR: {error}'}), 500


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get('DEBUG', False)
    app.run(host='0.0.0.0', port=5000, debug=ENVIRONMENT_DEBUG)
