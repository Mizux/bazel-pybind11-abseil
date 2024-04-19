include(FetchContent)
set(FETCHCONTENT_QUIET OFF)
set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
set(BUILD_SHARED_LIBS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_TESTING OFF)
set(CMAKE_Fortran_COMPILER OFF)

# ##############################################################################
# ZLIB
# ##############################################################################
if(BUILD_ZLIB)
  message(CHECK_START "Fetching ZLIB")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  FetchContent_Declare(
    zlib
    GIT_REPOSITORY "https://github.com/madler/ZLIB.git"
    GIT_TAG "v1.2.13"
    PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/ZLIB.patch")
  FetchContent_MakeAvailable(zlib)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

# ##############################################################################
# ABSEIL-CPP
# ##############################################################################
if(BUILD_absl)
  message(CHECK_START "Fetching Abseil-cpp")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  set(ABSL_ENABLE_INSTALL ON)
  set(ABSL_USE_SYSTEM_INCLUDES ON)
  set(ABSL_PROPAGATE_CXX_STD ON)
  set(ABSL_BUILD_TESTING OFF)
  FetchContent_Declare(
    abseil-cpp
    GIT_REPOSITORY "https://github.com/abseil/abseil-cpp.git"
    GIT_TAG "20240116.1"
    PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/abseil-cpp-20240116.1.patch"
  )
  FetchContent_MakeAvailable(abseil-cpp)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

# ##############################################################################
# pybind11
# ##############################################################################
# Find Python 3
find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

# ##############################################################################
# RE2
# ##############################################################################
if(BUILD_re2)
  message(CHECK_START "Fetching re2")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  set(RE2_BUILD_TESTING OFF)
  FetchContent_Declare(
    re2
    GIT_REPOSITORY "https://github.com/google/re2.git"
    GIT_TAG "2024-03-01"
    #PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/re2-2024-03-01.patch"
  )
  FetchContent_MakeAvailable(re2)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

if(BUILD_pybind11)
  message(CHECK_START "Fetching pybind11")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  set(PYBIND11_FINDPYTHON ON)
  set(PYBIND11_INSTALL ON)
  set(PYBIND11_TEST OFF)
  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY "https://github.com/pybind/pybind11.git"
    GIT_TAG "v2.12.0"
    #PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/pybind11.patch"
  )
  FetchContent_MakeAvailable(pybind11)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

if(BUILD_pybind11_abseil)
  message(CHECK_START "Fetching pybind11_abseil")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  FetchContent_Declare(
    pybind11_abseil
    GIT_REPOSITORY "https://github.com/pybind/pybind11_abseil.git" # 2024/04/01
    GIT_TAG "01171e9dfff80a43bbeb52020a4628267614f275"
    PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/pybind11_abseil.patch"
  )
  FetchContent_MakeAvailable(pybind11_abseil)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

###############
##  TESTING  ##
###############
if(BUILD_googletest)
  message(CHECK_START "Fetching googletest")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.14.0)
  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
  set(INSTALL_GTEST OFF)
  set(GTEST_HAS_ABSL ON)
  FetchContent_MakeAvailable(googletest)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()
