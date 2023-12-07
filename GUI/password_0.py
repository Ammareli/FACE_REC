import hashlib
import pickle
import os

USERNAME = "admin"
PASSWORD = "admin"

def encode(username,password,):
 
    pass_encode = hashlib.sha256(password.encode()).hexdigest()
    return [username,pass_encode] 

def pickle_(list_,path = "encodings"):
    if not os.path.exists(path):
        os.makedirs(path)
    
    file = open(os.path.join(path,"pas.p"),"wb")
    pickle.dump(list_,file)
    file.close()

def update(new_username, new_pass):
    list_ = encode(new_username,new_pass)
    pickle_(list_)


def allow_login(username,password):
    file = open("\encodings\pas.p","rb")
    list_ = pickle.load(file)
    pass_encode = hashlib.sha256(password.encode()).hexdigest()
    if username == list_[0] and pass_encode == list_[1]:
        return True
    else:
        return False


# list_ = encode(USERNAME,PASSWORD)
# print(list_)

# pickle_(list_)
