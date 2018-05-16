from pprint import pprint
from bitshares import BitShares
from bitshares.notify import Notify
import  threading
from bitshares.account import Account
from bitshares.memo import Memo

m = Memo()
m.unlock_wallet("secret-passphrase")

account = Account("morningtech-test")

def txcb(*argn,**args):
    pprint("txcb")  
    ret = (account.history(limit=1))
    for i in ret:
        tmp = (i['op'][1]['memo'])
        #pprint(tmp)
        de = m.decrypt(tmp)
        pprint(de)


def loop():
    notify = Notify(
        accounts=["morningtech-test"],
        #on_tx=txcb,
        on_account=txcb
    )
    notify.listen()

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()


