import configparser

from bitshares import BitShares

bitshares = BitShares()
is_created = bitshares.wallet.created()

conf = configparser.ConfigParser()
conf.read('/config/bitshares/conf.ini', encoding="utf8")

password = conf.get('wallet', 'wallet_password')

# only for account operation, should be moved into function in the future.  mark.ma
online_account_private_key = conf.get('wallet', 'on_line_account_private_key')

print("online_account_private_key", online_account_private_key)

if not is_created:
    bitshares.wallet.create(password)


def transfer(to, amount, asset, memo, from_account):
    print("password:", password)
    # only for transfer use.on_line_account_private_key
    online_fund_private_key = conf.get('wallet', 'on_line_wallet_private_key')
    print("online_fund_private_key:", online_fund_private_key)

    bitshares.wallet.unlock(password)
    # need to read addPrivateKey from configuration shell.
    try:
        bitshares.wallet.addPrivateKey(online_fund_private_key)
    except Exception:
        pass

    bitshares.transfer(to, amount, asset, memo, account=from_account)

    # bitshares.wallet.lock(password)


