# TATCHUM DEFO MICHEL ULRICH MASTER2 IA DIT
import os


class Dossier_Fichier:

    def __init__(self, project_root):
        self.project_root = project_root
       

    def create_dossier(self, name,  name_dossier=""):
        src_dir = os.path.join(self.project_root+""+ name_dossier, name)
        os.makedirs(src_dir, exist_ok=True)
    



