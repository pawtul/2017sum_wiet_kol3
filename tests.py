# source repository: https://github.com/AgnieszkaBacia/2017sum_wiet_kol1
import sys
import unittest

from kol1 import Plane, Simulation


class Mock(object):
    def __init__(self):
        self.was_called = False

    def __call__(self, *args, **kwargs):
        self.was_called = True


class SysStdOut(object):
    def __init__(self):
        self.history = []

    def write(self, msg):
        self.history.append(msg)

    def flush(self):
        pass


class PlaneTestCase(unittest.TestCase):
    def test_angle(self):
        plane = Plane(0)
        self.assertEqual(plane.angle, 0)

        plane = Plane(16)
        self.assertEqual(plane.angle, 16)

    def test_adjusting_tilt(self):
        plane = Plane(33)
        plane.adjust_tilt()
        self.assertEqual(plane.angle, 0)


class SimulationTestCase(unittest.TestCase):
    def test_initialization(self):
        plane = Plane(0)
        simulation = Simulation(plane)
        self.assertIs(simulation.plane, plane)

    def test_simulation_calls(self):
        plane = Plane(0)
        plane.adjust_tilt = Mock()
        plane.generate_tilt = Mock()
        simulation = Simulation(plane)
        self.assertIsNone(simulation.simulate())

        self.assertTrue(plane.generate_tilt)
        self.assertTrue(plane.adjust_tilt)

    def test_end_of_simulation(self):
        plane = Plane(0)
        simulation = Simulation(plane)

        old_stdout = sys.stdout
        sys.stdout = SysStdOut()
        self.assertIsNone(simulation.end_simulation())

        self.assertEqual(sys.stdout.history[0], "Simulation is ended!")
        sys.stdout = old_stdout

