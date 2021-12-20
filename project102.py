import dropbox
import groceryList
import random

def createList():
    number=random.randint(0,100)
    createGroceryList=listCapture(0)
    result=true
    while(result):
        ret, frame=groceryListCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=false

def upload_file(img_name): 
    access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN" 
    file =list_name 
    file_from = file 
    file_to="/testFolder/"+(img_name) 
    dbx = dropbox.Dropbox(access_token) 
    
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded") 
    
    def main():
         while(True): 
             if ((items.items() - list_items) >= 5): 
                 name = create_list() 
                 upload_file(name) 
                 main()