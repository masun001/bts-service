from bitshares import BitShares

bitshares = BitShares()
is_created = bitshares.wallet.created()

if not is_created:
    bitshares.wallet.create("morningtechwallet")


def transfer():
    bitshares.wallet.unlock("morningtechwallet")
    bitshares.wallet.addPrivateKey("5HqvJmhCjSpQWY2nJkXApCw3Ph5wr7fTzsdT8Pf42tmy51M3xD3")


    return