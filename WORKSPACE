workspace(name = "org_mizux_bazelpybind11abseil")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")

# Bazel Extensions
## Bazel Skylib rules.
git_repository(
    name = "bazel_skylib",
    tag = "1.5.0",
    remote = "https://github.com/bazelbuild/bazel-skylib.git",
)
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()

## Bazel rules.
git_repository(
    name = "platforms",
    tag = "0.0.8",
    remote = "https://github.com/bazelbuild/platforms.git",
)

git_repository(
    name = "rules_cc",
    tag = "0.0.9",
    remote = "https://github.com/bazelbuild/rules_cc.git",
)

git_repository(
    name = "rules_python",
    tag = "0.31.0",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

# Dependencies
## Abseil-cpp
git_repository(
    name = "com_google_absl",
    tag = "20240116.1",
    patches = ["//patches:abseil-cpp-20240116.1.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/abseil/abseil-cpp.git",
)

## Python
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:repositories.bzl", "python_register_multi_toolchains")
DEFAULT_PYTHON = "3.11"
python_register_multi_toolchains(
    name = "python",
    default_version = DEFAULT_PYTHON,
    python_versions = [
      "3.12",
      "3.11",
      "3.10",
      "3.9",
      "3.8"
    ],
)

# Create a central external repo, @pip_deps, that contains Bazel targets for all the
# third-party packages specified in the requirements.txt file.
load("@rules_python//python:pip.bzl", "pip_parse")
pip_parse(
   name = "pip_deps",
   requirements_lock = "//:requirements.txt",
)

load("@pip_deps//:requirements.bzl", install_pip_deps="install_deps")
install_pip_deps()

## `pybind11_bazel`
git_repository(
    name = "pybind11_bazel",
    tag = "v2.12.0",
    remote = "https://github.com/pybind/pybind11_bazel.git",
)

new_git_repository(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11-BUILD.bazel",
    tag = "v2.12.0",
    remote = "https://github.com/pybind/pybind11.git",
)

new_git_repository(
    name = "pybind11_abseil",
    commit = "01171e9dfff80a43bbeb52020a4628267614f275", # 2024/04/01
    patches = ["//patches:pybind11_abseil.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_abseil.git",
)

## Testing
git_repository(
    name = "com_google_googletest",
    tag = "v1.14.0",
    remote = "https://github.com/google/googletest.git",
)
