#!/usr/bin/env python3
"""Test APIs"""

import sys
import datetime
from absl.testing import absltest

print(sys.path)
#from pybind11_abseil.pybind11_abseil import status
import status
#from pybind11_abseil import status

import bp11.foo.python as fp
import bp11.foo.python.pyfoo as fpf
from bp11.foo.python.pyfoo import Foo

if __debug__:
    print(f"python path: {sys.path}")

    print(f"foo.python: ${dir(fp)}")
    print(f"foo.python.pyfoo: ${dir(fpf)}")
    print(f"foo.python.pyfoo.Foo: ${dir(fpf.Foo)}")


class TestFoo(absltest.TestCase):
    """Test Foo"""
    message_regex = 'Status module has not been imported.*'

    def test_absl_function(self):
        self.assertIsNone(fpf.absl_function("good"))

        with self.assertRaises(status.StatusNotOk) as cm:
          fpf.absl_function("error")
        self.assertEqual(cm.exception.status.code(), status.StatusCode.INTERNAL)
        self.assertEqual(cm.exception.status.message(), 'error')
        self.assertEqual(cm.exception.code, int(status.StatusCode.INTERNAL))
        self.assertEqual(cm.exception.message, 'error')

    def test_absl_duration(self):
        duration = fpf.make_duration(3600)
        self.assertEqual(duration.days, 0)
        self.assertEqual(duration.seconds, 3600)
        self.assertEqual(duration.microseconds, 0)

        duration = fpf.make_infinite_duration()
        self.assertEqual(duration, datetime.timedelta.max)
        self.assertTrue(fpf.is_infinite_duration(duration))
        self.assertFalse(fpf.is_infinite_duration(fpf.make_duration(123)))

    def test_absl_time(self):
        time = fpf.make_time(3600);
        self.assertTrue(fpf.check_datetime(time, 3600))

    def test_absl_status(self):
        self.assertIsNone(fpf.return_status(status.StatusCode.OK))

        # The return_status function should convert a non-ok status to an exception.
        with self.assertRaises(status.StatusNotOk) as cm:
          fpf.return_status(status.StatusCode.CANCELLED, 'test')
        self.assertEqual(cm.exception.status.code(), status.StatusCode.CANCELLED)
        self.assertEqual(cm.exception.status.message(), 'test')
        self.assertEqual(cm.exception.code, int(status.StatusCode.CANCELLED))
        self.assertEqual(cm.exception.message, 'test')

    def test_free_function(self):
        fpf.free_function(2147483647)  # max int
        fpf.free_function(2147483647 + 1)  # max int + 1

    def test_string_vector(self):
        self.assertEqual(4, fpf.string_vector_input(["1", "2", "3", "4"]))

        self.assertEqual(5, fpf.string_vector_ref_input(["1", "2", "3", "4", "5"]))

        res = fpf.string_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_string_jagged_array(self):
        self.assertEqual(
            3, fpf.string_jagged_array_input([["1"], ["2", "3"], ["4", "5", "6"]])
        )

        self.assertEqual(
            4,
            fpf.string_jagged_array_ref_input(
                [["1"], ["2", "3"], ["4", "5", "6"], ["7"]]
            ),
        )

        v = fpf.string_jagged_array_output(5)
        self.assertEqual(5, len(v))
        for i in range(5):
            self.assertEqual(i + 1, len(v[i]))

    def test_pair_vector(self):
        self.assertEqual(3, fpf.pair_vector_input([(1, 2), (3, 4), (5, 6)]))

        self.assertEqual(3, fpf.pair_vector_ref_input([(1, 2), (3, 4), (5, 6)]))

        res = fpf.pair_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_pair_jagged_array(self):
        self.assertEqual(2, fpf.pair_jagged_array_input([[(1, 1)], [(2, 2), (2, 2)]]))

        self.assertEqual(
            2, fpf.pair_jagged_array_ref_input([[(1, 1)], [(2, 2), (2, 2)]])
        )

        res = fpf.pair_jagged_array_output(5)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(5, len(res))
        for i in range(5):
            self.assertEqual(i + 1, len(res[i]))

    def test_Foo_static_methods(self):
        f = Foo()
        if __debug__:
            print(f"class Foo: ${dir(f)}")
        f.static_function(1)
        f.static_function(2147483647)
        f.static_function(2147483647 + 1)

    def test_Foo_int_methods(self):
        f = Foo()
        f.int = 13
        self.assertEqual(13, f.int)
        f.int = 17
        self.assertEqual(17, f.int)

    def test_Foo_int64_methods(self):
        f = Foo()
        f.int64 = 31
        self.assertEqual(31, f.int64)
        f.int64 = 42
        self.assertEqual(42, f.int64)


if __name__ == "__main__":
    absltest.main(verbosity=2)
