#          Tooler-1.0

Tooler-1.0-Instructions:


# *.tooler File Configuration

-TOOLER_ENV      -*set the toolers environment*

-TOOLER_SOURCES      -*set the toolers source files to compile*

-TOOLER_VERSION     -*set the toolers version*

-TOOLER_IGNR    -*file extensions for tooler to ignore*

-TOOLER_IGNR_DIRECT    -*a certain file for tooler to ignore*

-TOOLER_COMPILER_CHAIN    -*set the compiler that your code uses to build*

-TOOLER_BUILD_OUTPUT    -*set the application name for the output after the code compiles*

-TOOLER_BUILD_ARCH    -*set the arch type of the build,  [x64, x86]*

-TOOLER_BUILD_INFO    -*set the build type info, [debug, release]*

-TOOLER_BUILD_MSG    -*print a message in a command window, after code builds*

-TOOLER_CRUSTIFY    -*zip a folder*

-TOOLER_DELETE      -*delete a file or folder*

-TOOLER_BIN        -*sets where the build file from source code goes*

-TOOLER_TOOLKIT      -*sets a toolkit that might be need, such as a GUI toolkit, or Graphics, etc...*

-TOOLER_BUILD_MAKE_DLL    -*makes all compiled sources a .DLL file*

-TOOLER_BUILD_MAKE_LIB    -*makes all compiled sources a .LIB file*

-TOOLER_SKIP_OVER    -*if a file is building and has a error, it does not stop the build process, but goes over the file, and goes to another file to build*


#      Tooler Terminal

To Began Tooler File Package Build:

# ~ -f .tooler  $[build_pkgs, build_info]

