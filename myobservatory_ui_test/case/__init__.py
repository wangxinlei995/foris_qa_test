import os
import sys

file_dir=os.path.abspath(__file__)
project_dir=file_dir[:file_dir.find('xc_ui_text')]+'xc_ui_text'
sys.path.append(project_dir)