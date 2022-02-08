from nltk.chat.util import Chat,reflections


ciftler = [
    ["Benim adım (.*)", ["Merhaba %1, nasılsın?"]],
    ['(merhaba|selam|hello|hey)',['merhaba, nasılsın',
                                           'hello','Heyy nasıl '
                                                          'gidiyor']],
    ['(.*) hava çok (.*)',['Evet sana katılıyorum.%1 hava %2, bence keyfini çıkarmaya bak']],
    ['En güzel şehir (.*)',['Sana katılıyorum, %1 nin yemekleri de '
                            'güzeldir.', '%1 nın doğası da güzeldir', '%1 in '
                                                                      'insanları da şahanedir' ]],
    ['Yaşın kaç?',['Yaşım yok ama 2021 yılında ütretildim']],
    ['(.*)(memleket|nerelisin|hangi şehir|hangi ülke)',['Ankara, Türkiye']],
    ['Semih',['He benim buyur kardeş!,Rahmet "i unutma :)']],
    [ 'Ben de iyiyim teşekkürler ne yapıyorsun?',['Ne yapayım ben de kendi işimi yapmaya çalışıyorum..']]

]
yansimalar={
    'merhaba': 'merhaba, nasılsın',
    'gittim':'gittin',
    'Selamünaleyküm':'Aleykümselam'
}

chat = Chat(ciftler, yansimalar)
chat.converse(quit='bitti')
#print(chat._substitute("merhaba"))
#print(reflections)