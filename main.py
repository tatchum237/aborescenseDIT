# TATCHUM DEFO MICHEL ULRICH MASTER2 IA DIT
import os
import nbformat
import subprocess

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
  
    def initialize_git_repository(self):
        try:
        # Vérifier si Git est installé et accessible
            subprocess.run(["git", "--version"], check=True)

        # Initialiser un dépôt Git dans le chemin spécifié
            subprocess.run(["git", "init", self.project_root], check=True)
            print(f"Le dépôt Git a été initialisé dans '{self.project_root}'.")

        except FileNotFoundError:
            print("Erreur : Git n'est pas installé sur votre système.")
        except subprocess.CalledProcessError:
            print("Une erreur s'est produite lors de l'exécution de la commande Git.")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
    

    def create_git_commit(self, commit_message):
        try:
        # Vérifier si Git est installé et accessible
            subprocess.run(["git", "--version"], check=True, cwd=self.project_root)

        # Ajouter tous les fichiers modifiés à l'index
            subprocess.run(["git", "add", "."], check=True, cwd=self.project_root)

        # Créer un commit avec le message spécifié
            subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=self.project_root)
            print(f"Commit créé avec succès avec le message : '{commit_message}'.")

        except FileNotFoundError:
            print("Erreur : Git n'est pas installé sur votre système.")
        except subprocess.CalledProcessError:
            print("Une erreur s'est produite lors de l'exécution de la commande Git.")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

        
    def main(self):
        dossier = Dossier_Fichier("monProject")
        dossier.create_git_commit('dossier créé')
        dossier.create_dossier('data')
        dossier.create_dossier('docs')
        dossier.create_dossier("models")
        dossier.create_dossier("notebooks")
        dossier.create_dossier("reports")
        dossier.create_dossier("src")
        dossier.create_git_commit('sous dossier créé')

        dossier.create_dossier('cleaned', "/data" )
        dossier.create_dossier('raw', "/data" )
        dossier.create_dossier('processed', "/data" )

        dossier.create_git_commit('sous sous dossier créé')

        dossier.create_fichier('utils','.y', '/src')
        dossier.create_fichier('process','.py', '/src')
        dossier.create_fichier('train','.py', '/src')
        dossier.create_fichier('main','.ipynb', '/notebooks')

        dossier.create_git_commit('fichier de code créé')

        dossier.create_fichier('LICENSE','', '')
        dossier.create_fichier('makefile','', '')
        dossier.create_fichier('readme','.md', '')
        dossier.create_fichier('requirements','.txt', '')
 

        dossier.initialize_git_repository()

        dossier.create_git_commit('fin du dit project')


if __name__ == "__main__":
    Dossier_Fichier("").main()


    
    


    