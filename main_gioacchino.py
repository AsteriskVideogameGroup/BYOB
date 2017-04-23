from src.domain.gamemanage.bob import BoBDescription

print(BoBDescription("classic"))
print(BoBDescription("classic"))
print(BoBDescription("ciao"))

print(BoBDescription("abba") == BoBDescription("ciao"))
print(BoBDescription("ciao") == BoBDescription("ciao"))
