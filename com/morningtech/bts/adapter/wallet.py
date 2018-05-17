import configparser

from bitshares import BitShares

bitshares = BitShares()
is_created = bitshares.wallet.created()

conf = configparser.ConfigParser()
conf.read('/Users/maxiaodong/privateChain/bts-service/conf.ini', encoding="utf8")

password = conf.get('wallet', 'wallet_password')
online_private_key = conf.get('wallet', 'on_line_wallet_private_key')
print("online_private_key:", online_private_key)

if not is_created:
    bitshares.wallet.create(password)


def transfer(to, amount, asset, memo, fromAccount):
    print("password:", password)

    bitshares.wallet.unlock(password)
    # need to read addPrivateKey from configuration shell.
    try:
        bitshares.wallet.addPrivateKey(online_private_key)
    except Exception:
        pass

    bitshares.transfer(to, amount, asset, memo, account=fromAccount)

    # bitshares.wallet.lock(password)


