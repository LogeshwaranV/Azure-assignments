from flask import Flask, render_template
from azure.storage.blob import ContainerClient,BlobClient
import os

app = Flask(__name__)

def listfolders():
    folder = {}
    tempfol = []
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=logeshmletraining;AccountKey=7V5Xqpca289aWcmcBnuzVYxjwdsCpqQ5Yt7WI/SLKbC5HAVOY8gqU5DLDy7RIWBqMoRiwhu9dQVe+AStBHIRQg==;EndpointSuffix=core.windows.net'
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="assigmnent1")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        temp = str(blob.name)
        fol, fil = temp.split('/')
        if fol not in tempfol:
            tempfol.append(fol)
            folder[fol] = []
        folder[fol].append(fil)
    files=list(folder.values())
    print(tempfol,files)
    return tempfol,files


@app.route('/')
def home():
    folderlist,filelist = listfolders()
    return render_template('home.html', folder=folderlist,file=filelist)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
