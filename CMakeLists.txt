cmake_minimum_required(VERSION 2.8.11 FATAL_ERROR)
if(CMAKE_VERSION VERSION_GREATER 3.0)
    CMAKE_POLICY(SET CMP0048 NEW)
endif()

project(flex-bison CXX)

# Build flex/bison from source.
# This is EXTREMELY ugly because it builds at configure-time. It's copypasta
# from jvanstraten/libcqasm, where this was necessary, because the rest of
# the CMakeLists required them to have been found by FindFLEX/FindBISON. It
# should probably be fixed, but ain't nobody got time for that.
set(FLEX_VERSION_REQUIRED 2.6.1)
set(BISON_VERSION_REQUIRED 3.0)
include(cmake/flex-bison.cmake)

# Make install target.
include(GNUInstallDirs)
install(
    FILES ${BISON_EXECUTABLE} ${FLEX_EXECUTABLE}
    DESTINATION ${CMAKE_INSTALL_BINDIR}
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
)
