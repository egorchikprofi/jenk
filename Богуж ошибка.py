import requests
def skin(content):
    return 'backpack_agentsherbert'.encode() in content

res= requests.get('https://fortnite-api.com/v2/cosmetics/br')
content = res.content

print('is skin? ' + str(skin(content)))