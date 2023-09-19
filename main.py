# TATCHUM DEFO MICHEL ULRICH MASTER2 IA DIT
import os
import nbformat

class Dossier_Fichier:

    def __init__(self, project_root):
        self.project_root = project_root
       

    def create_dossier(self, name,  name_dossier=""):
        src_dir = os.path.join(self.project_root+""+ name_dossier, name)
        os.makedirs(src_dir, exist_ok=True)

    def create_fichier(self, name, extension, name_dossier, code_content="""
        # Votre code d'analyse de données ici"""):

        if(extension == ".py" or extension == ".md" or 
           extension == ".txt"):
            path = os.path.join(self.project_root+''+name_dossier, name+""+extension)
            with open(path, 'w') as code_file:
                code_file.write(code_content)

        else:
            notebook = nbformat.v4.new_notebook()
            code_cell = nbformat.v4.new_code_cell(source='print("Hello, World!")')
            notebook.cells.append(code_cell)
            code_file_path = os.path.join(self.project_root+""+name_dossier, name+''+extension)
            with open(code_file_path, 'w') as code_file:
                nbformat.write(notebook, code_file)
  
    



