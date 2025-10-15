add_cxx_library(
  NAME
    foo
  HEADERS
    foo.h
  SOURCES
    foo.cc
  INSTALL_DIR
    bp11/foo
  LINK_LIBRARIES
    absl::strings
    absl::status
    absl::time
)

add_cpp_test(${CMAKE_CURRENT_SOURCE_DIR}/foo_test.cc)
