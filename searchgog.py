from googlesearch import search

try:
    import googlesearch
except ImportError:
    print("Malumot topilmadi")

query = "Python"
for i in search(query, tld='co.in', num=10, stop=10, pause=21):
    print(i)