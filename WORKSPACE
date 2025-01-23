workspace(name = "mizux_bp11_absl")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")

# Bazel Extensions
## Bazel Skylib rules.
git_repository(
    name = "bazel_skylib",
    tag = "1.7.1",
    remote = "https://github.com/bazelbuild/bazel-skylib.git",
)
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()

## Bazel rules.
git_repository(
    name = "platforms",
    tag = "0.0.10",
    remote = "https://github.com/bazelbuild/platforms.git",
)

git_repository(
    name = "rules_cc",
    tag = "0.0.16",
    remote = "https://github.com/bazelbuild/rules_cc.git",
)

git_repository(
    name = "rules_python",
    tag = "0.34.0",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

# Dependencies
## Abseil-cpp
git_repository(
    name = "com_google_absl",
    tag = "20240116.2",
    patches = ["//patches:abseil-cpp-20240116.2.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/abseil/abseil-cpp.git",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")
py_repositories()

load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")
pip_install_dependencies()

DEFAULT_PYTHON = "3.11"

python_register_multi_toolchains(
    name = "python",
    default_version = DEFAULT_PYTHON,
    python_versions = [
      "3.12",
      "3.11",
      "3.10",
      "3.9",
    ],
)

load("@python//:pip.bzl", "multi_pip_parse")

multi_pip_parse(
    name = "pypi",
    default_version = DEFAULT_PYTHON,
    python_interpreter_target = {
        "3.12": "@python_3_12_host//:python",
        "3.11": "@python_3_11_host//:python",
        "3.10": "@python_3_10_host//:python",
        "3.9": "@python_3_9_host//:python",
    },
    requirements_lock = {
        "3.12": "//bazel:requirements_lock_3_12.txt",
        "3.11": "//bazel:requirements_lock_3_11.txt",
        "3.10": "//bazel:requirements_lock_3_10.txt",
        "3.9": "//bazel:requirements_lock_3_9.txt",
    },
)

load("@pypi//:requirements.bzl", "install_deps")
install_deps()

## `pybind11_bazel`
git_repository(
    name = "pybind11_bazel",
    tag = "v2.13.6", # 2024/04/08
    patches = ["//patches:pybind11_bazel.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_bazel.git",
)

new_git_repository(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11-BUILD.bazel",
    tag = "v2.13.6",
    remote = "https://github.com/pybind/pybind11.git",
)

new_git_repository(
    name = "org_pybind11_abseil",
    tag = "v202402.0",
    patches = ["//patches:pybind11_abseil.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_abseil.git",
)

## Testing
git_repository(
    name = "googletest",
    tag = "v1.14.0",
    remote = "https://github.com/google/googletest.git",
)
