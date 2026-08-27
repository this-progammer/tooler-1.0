"""
File : *tooler_env.py*
Tool Version : Tooler-1.0
Programmer : Aether
"""

"""*Setting Toolers Compile Environment*"""

"""*Tooler Path*"""
TOOLER_PATH = str

"""*Tooler Source Files*"""
TOOLER_SOURCE_FILES = str

class ToolerEnvironment :
  def __init__( self ):
    return self

  def set_tooler_env_path( path : str ):
    TOOLER_PATH = path

  def set_tooler_source_files( files : str, ext : str ):
    TOOLER_SOURCE_FILES = [files, ext]
