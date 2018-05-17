from bitshares import BitShares

bitshares = BitShares()
# bitshares.wallet.newWallet("mark'swallet")
# bitshares.wallet.create("masun001")

isCreated = bitshares.wallet.created()

print(isCreated)

info = bitshares.info()
print(info)

if not isCreated:
    bitshares.wallet.create("morningtech")

bitshares.wallet.unlock("morningtech")
# capital private key
bitshares.wallet.addPrivateKey("5HqvJmhCjSpQWY2nJkXApCw3Ph5wr7fTzsdT8Pf42tmy51M3xD3")

iret = bitshares.wallet.getAccounts()
print(iret)

bitshares.transfer("gate-io-bts66", "10", "BTS", "2b4420ff4dfa4b52", account="masun001")

