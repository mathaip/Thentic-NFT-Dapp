import requests, webbrowser, json
from flask import Flask, jsonify, request  # Press ⌃R to execute it or replace it with your code.
import string
import random

app = Flask(__name__)


def id_generator():
    return ''.join(random.choices(string.digits, k=6))


@app.route("/create", methods=["GET"])
def create():
    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'QzdSl7ShD9DsqnXPeXjR4lySU2mBNpvD',
            'chain_id': '97',
            'name': 'CryptoCrooks',
            'short_name': 'CRC'}

    # creates NFT contract on BNB testnet
    r = requests.post(url, json=data, headers=headers)
    print(r.text)
    return "200"


@app.route("/mint", methods=['POST'])
def main():
    minteraddress = request.form["address"]
    image_url = request.form["image"]
    img_data = requests.get(image_url).content
    nft_id = id_generator()
    with open('NFT.jpg', 'wb') as handler:
        handler.write(img_data)
    print(nft_id)
    url = 'https://thentic.tech/api/nfts/mint'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'QzdSl7ShD9DsqnXPeXjR4lySU2mBNpvD',
            'chain_id': '97',
            'contract': '0x9008D350F1887Cb14B6c64FdFeE8dFd38d9aA1a3',
            'nft_id': nft_id,
            'to': minteraddress,
            "nft_data": image_url,
            "redirect_url": image_url
            }
    r = requests.post(url, json=data, headers=headers)
    response = r.text
    print(response)
    response_url = json.loads(response)
    transaction_url = response_url['transaction_url']
    webbrowser.open(transaction_url)
    return "successfully minted NFT id" + nft_id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
