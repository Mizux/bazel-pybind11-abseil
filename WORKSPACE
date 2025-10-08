workspace(name = "bazel-pybind11-abseil")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

################################################################################
#
# WORKSPACE is being deprecated in favor of the new Bzlmod dependency system.
# It will be removed at some point in the future.
#
################################################################################

# Bazel Extensions
## Needed for Abseil.
git_repository(
    name = "bazel_skylib",
    commit = "56a2abbaf131332835ab2721a258ea3c763a7178",
    #tag = "1.8.1",
    remote = "https://github.com/bazelbuild/bazel-skylib.git",
)
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()

git_repository(
    name = "bazel_features",
    commit = "3f23ff44ff85416d96566bee8e407694cdb6f1f8",
    #tag = "v1.32.0",
    remote = "https://github.com/bazel-contrib/bazel_features.git",
)
load("@bazel_features//:deps.bzl", "bazel_features_deps")
bazel_features_deps()

## Bazel rules.
git_repository(
    name = "platforms",
    commit = "ab99943ab6bed53cff461a3afa99fc79d31e4351",
    #tag = "1.0.0",
    remote = "https://github.com/bazelbuild/platforms.git",
)

git_repository(
    name = "rules_cc",
    commit = "cbee84ad7f583049823f3d1497aab1264cf94f26",
    #tag = "0.1.4",
    remote = "https://github.com/bazelbuild/rules_cc.git",
)

git_repository(
    name = "rules_python",
    commit = "38f2679fcc6c23a72e4c6309b7fdecb4eafcccf0",
    #tag = "1.6.3",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

DEFAULT_PYTHON = "3.12"

#load("@rules_python//python:repositories.bzl", "python_register_toolchains")
#python_register_toolchains(
#    name = "python",
#    # Available versions are listed in @rules_python//python:versions.bzl.
#    # We recommend using the same version your team is already standardized on.
#    python_version = DEFAULT_PYTHON,
#)
#load("@rules_python//python:pip.bzl", "pip_parse")
#pip_parse(
#    name = "pypi",
#    python_interpreter_target = "@python_host//:python",
#    requirements_lock = "//bazel:requirements_lock_3_12.txt",
#)

load("@rules_python//python:repositories.bzl", "python_register_multi_toolchains")
python_register_multi_toolchains(
    name = "python",
    default_version = DEFAULT_PYTHON,
    python_versions = [
      "3.12",
      "3.11",
      "3.10",
      "3.9",
    ],
    ignore_root_user_error=True,
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

# Load the starlark macro, which will define your dependencies.
load("@pypi//:requirements.bzl", "install_deps")
# Call it to define repos for your requirements.
install_deps()

## `pybind11_bazel`
git_repository(
    name = "pybind11_bazel",
    commit = "2b6082a4d9d163a52299718113fa41e4b7978db5",
    #tag = "v2.13.6", # 2024/04/08
    #patches = ["//patches:pybind11_bazel.patch"],
    #patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_bazel.git",
)

## `pybind11`
# https://github.com/pybind/pybind11
new_git_repository(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11-BUILD.bazel",
    commit = "a2e59f0e7065404b44dfe92a28aca47ba1378dc4",
    #tag = "v2.13.6",
    remote = "https://github.com/pybind/pybind11.git",
)

new_git_repository(
    name = "pybind11_abseil",
    commit = "70f8b693b3b70573ca785ef62d9f48054f45d786",
    #tag = "v202402.0",
    patches = ["//patches:pybind11_abseil.patch"],
    patch_args = ["-p1"],
    remote = "https://github.com/pybind/pybind11_abseil.git",
    repo_mapping = {"@com_google_absl": "@abseil-cpp"},
)

## Abseil-cpp
git_repository(
    name = "abseil-cpp",
    commit = "987c57f325f7fa8472fa84e1f885f7534d391b0d",
    #tag = "20250814.0",
    remote = "https://github.com/abseil/abseil-cpp.git",
)

## Re2
git_repository(
    name = "re2",
    commit = "6dcd83d60f7944926bfd308cc13979fc53dd69ca",
    #tag = "2024-07-02",
    remote = "https://github.com/google/re2.git",
    #repo_mapping = {"@abseil-cpp": "@com_google_absl"},
)

#http_archive(
#    name = "abseil-py",
#    sha256 = "8a3d0830e4eb4f66c4fa907c06edf6ce1c719ced811a12e26d9d3162f8471758",
#    strip_prefix = "abseil-py-2.1.0",
#    urls = [
#        "https://github.com/abseil/abseil-py/archive/refs/tags/v2.1.0.tar.gz",
#    ],
#)

# Testing
## Googletest
git_repository(
    name = "googletest",
    commit = "52eb8108c5bdec04579160ae17225d66034bd723",
    #tag = "v1.17.0",
    remote = "https://github.com/google/googletest.git",
)
