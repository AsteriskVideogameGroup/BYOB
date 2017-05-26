import Pyro4

from src.domain.gamemanage.player.ClientInfos import ClientInfos
from src.domain.gamemanage.player.Player import Player
from src.foundation.netmiddleware.NetworkObjectTranslator import NetworkObjectTranslator

NetworkObjectTranslator().init("localhost", 9090)

p1 = Player()
client1 = ClientInfos(p1)
NetworkObjectTranslator().register(client1, "ultimoarrivato1")
print("oh my god")
p2 = Player()
client2 = ClientInfos(p2)
NetworkObjectTranslator().register(client2, "ultimoarrivato2")
print("oh my god")
p3 = Player()
client3 = ClientInfos(p3)
NetworkObjectTranslator().register(client3, "ultimoarrivato3")
print("oh my god")
p4 = Player()
client4 = ClientInfos(p4)
NetworkObjectTranslator().register(client4, "ultimoarrivato4")
print("oh my god")

proxy = NetworkObjectTranslator().translate("game-handle")
print(proxy)

#proxy.sayHello()

# Pyro4.config.SERIALIZER = "pickle"

proxy.makeNewGame("ultimoarrivato1", "classic_debug", False)
proxy.makeNewGame("ultimoarrivato2", "classic_debug", False)
proxy.makeNewGame("ultimoarrivato3", "classic_debug", False)
proxy.makeNewGame("ultimoarrivato4", "classic_debug", False)


