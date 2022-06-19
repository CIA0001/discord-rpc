import os,json,time;from pypresence import *

class RPC:

    def __init__(self):
        self.cls = lambda: os.system('cls')
        self.file = open('config.json')
        self.data = json.load(self.file)

    def Main(self):
        os.system('title Discord RPC')
        RPC = Presence(client_id=self.data['Clientid'])
        RPC.connect()
        print(f'\033[1;32;40m RPC CONNECTED')
        time.sleep(1.5)

        while True:
            RPC.update(state=self.data['State'],
            details=self.data['Details'],
            large_image=self.data['LargeIMG'],
            small_image=self.data['SmallIMG'],
            large_text=self.data['LargeText'],
            buttons=[
            {'label':self.data['Button1Text'],'url':self.data['Button1Url']},
            {'label':self.data['Button2Text'],'url':self.data['Button2Url']}])
            self.cls()
            print(f'\033[1;33;40m RPC UPDATED')
            time.sleep(15)

if __name__ == "__main__":
    RPC().Main()
