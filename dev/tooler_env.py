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

  """*set_tooler_env_path*"""
  def set_tooler_env_path( path : str ):
    TOOLER_PATH = path

  """*set_tooler_source_files*"""
  def set_tooler_source_files( files : str, ext : str ):
    TOOLER_SOURCE_FILES = [files, ext]

  """*tooler_env_path_clear*"""
  def tooler_env_path_clear():
    TOOLER_PATH = ''

  """tooler_env_source_clear*"""
  def tooler_env_source_clear():
    TOOLER_SOURCE_FILES = ''
