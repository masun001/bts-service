# -*- coding: utf-8 -*-
from bitshares.exceptions import WrongMasterPasswordException
from flask import Flask, jsonify
from flask import request

from com.morningtech.bts.adapter import wallet

app = Flask(__name__)
app.config["JSON\_AS\_ASCII"] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Welcome to BTS Service</h1>'


@app.route("/ok", methods=['GET'])
def ok():
    return "ok"


@app.route("/captial/withdraw", methods=['POST'])
def withdraw():
    data = request.json

    to = data['to']
    amount = data['amount']
    asset = data['asset']
    memo = data['memo']
    print("data:", data)

    result_msg = {
        "code": 0,
        "msg": "操作成功"
    }

    try:
        wallet.transfer(to, amount, asset, memo, data['from'])
    except WrongMasterPasswordException:
        # pdb.set_trace()
            result_msg = {
                "code": 999,
                "msg": "WrongMasterPasswordException"
            }

    return jsonify(result_msg)


if __name__ == '__main__':
    app.run(debug=True)
