add_library(foo)
target_sources(foo PRIVATE foo.hpp foo.cpp)
target_include_directories(foo
  PUBLIC
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>)
target_compile_features(foo PUBLIC cxx_std_17)
set_target_properties(foo PROPERTIES
  VERSION ${PROJECT_VERSION}
  PUBLIC_HEADER foo.hpp)
target_link_libraries(foo PUBLIC
  absl::strings
  absl::status
  absl::time
)
add_library(${PROJECT_NAMESPACE}::foo ALIAS foo)

# Test
if(BUILD_TESTING)
  add_cpp_test(${CMAKE_CURRENT_SOURCE_DIR}/foo_test.cpp)
endif()

# Install
install(TARGETS foo
  EXPORT ${PROJECT_NAME}Targets
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/bp11/foo)
