import os

curr = os.getcwd()

new_folder = os.path.join(curr,f"Modules_in_Python/Os_Module/new_folder")
# print(os.listdir(new_folder))

def create_req_folders(dir_name):
    dir_folder = os.path.join(new_folder,dir_name)
    if not os.path.exists(dir_folder):
        os.makedirs(dir_folder)
        
    return dir_folder
    

for dir_path, dir_name, filename in os.walk(new_folder):
    for file in filename:
        if os.path.splitext(file)[-1] == ".txt":
            dir_name = "text_only"
            dir_folder = create_req_folders(dir_name)
            os.rename(os.path.join(new_folder,file),f"{dir_folder}/{file}")
        
        if os.path.splitext(file)[-1] == ".docx":
            dir_name = "Docx_only"
            dir_folder = create_req_folders(dir_name)
            os.rename(os.path.join(new_folder,file),f"{dir_folder}/{file}")
        
        if os.path.splitext(file)[-1] == ".jpg":
            dir_name = "Jpg_only"
            dir_folder = create_req_folders(dir_name)
            os.rename(os.path.join(new_folder,file),f"{dir_folder}/{file}")