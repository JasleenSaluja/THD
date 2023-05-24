import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import firestore

cred = credentials.Certificate('serviceAccountKey.json')
print(cred)
bucket = 'thd-game.appspot.com'
app = firebase_admin.initialize_app(cred, {
    'storageBucket': bucket
})

db = firestore.client()
bucket = storage.bucket()

def upload_file(name='level1', filepath='levels/level_1.game'):
    # bucket.blob(filepath).upload_from_filename(filepath)
    # doc_ref = db.collection(u'levels').document(name)
    # doc_ref.set({
    #     u'level': name,
    #     u'path': filepath
    # })
    pass



def fetch_all_levels():
    levels_ref = db.collection(u'levels')
    docs = levels_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def download_file(name='level1', filepath='levels/level_1.game'):
    blob = bucket.blob(name)
    blob.download_to_filename(filepath)

def download_all_levels():
    levels_ref = db.collection(u'levels')
    docs = levels_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        download_file(doc.id, doc.to_dict()['path'])

if __name__ == '__main__':
    # upload_file()
    download_all_levels()