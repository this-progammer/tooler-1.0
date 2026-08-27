"""
# Tooler-1.0 — Proprietary Code License

**Copyright © 2026 Aether. All rights reserved.**

Tooler-1.0 is proprietary software written by **Aether**. The source code and all associated materials are protected by applicable copyright and intellectual-property laws.

## Restrictions

Without explicit prior written permission from Aether, **nobody is permitted to:**

1. Copy, steal, or reproduce any portion of the Tooler-1.0 source code.
2. Modify, alter, adapt, or create derivative works based on the source code.
3. Redistribute, republish, or share the source code or modified versions.
4. Sell, sublicense, or otherwise distribute the source code or any derivative work.
5. Claim ownership or authorship of any portion of the Tooler-1.0 source code.

## Permission

No rights or permissions are granted except those explicitly provided in writing by **Aether**.

Any unauthorized copying, modification, or redistribution of Tooler-1.0 is prohibited.

## No Warranty

Tooler-1.0 is provided **"as is"**, without warranties of any kind, express or implied. Aether shall not be liable for any damages arising from the use or inability to use the software, to the maximum extent permitted by applicable law.

## Ownership

All rights, title, and interest in Tooler-1.0 and its source code remain with **Aether**.

**Tooler-1.0 is proprietary software. All rights reserved.**
"""
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
    TOOLER_PATH = '\0'

  """*tooler_env_source_clear*"""
  def tooler_env_source_clear():
    TOOLER_SOURCE_FILES = '\0'

  """*clear*"""
  def clear( self ):
    self.tooler_env_path_clear()
    self.tooler_env_source_clear()
