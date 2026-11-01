"""
Unit tests for the ScholarQA Mechanistic Query Reframer (standard library unittest).
"""

import unittest
from scholarqa_reframer.models import ReframedInquiry
from scholarqa_reframer.engine import MechanisticReframer


class TestMechanisticReframer(unittest.TestCase):
    def setUp(self):
        self.reframer = MechanisticReframer()

    def test_q02_thermal_velocity(self):
        q = "Does solvent viscosity damp bacterial instantaneous thermal velocity according to Stokes' drag?"
        result = self.reframer.reframe(q)

        self.assertIsInstance(result, ReframedInquiry)
        self.assertIn("equipartition", result.scholarqa_mechanistic_query.lower())
        self.assertIn("relaxation", result.scholarqa_mechanistic_query.lower())
        self.assertGreaterEqual(len(result.decoupled_dimensions), 2)
        self.assertTrue(any("Instantaneous" in d.dimension_name for d in result.decoupled_dimensions))
        self.assertTrue(any("Relaxation" in d.dimension_name for d in result.decoupled_dimensions))
        self.assertGreaterEqual(len(result.retrieval_probes), 1)
        self.assertIn("Berg", result.retrieval_probes[0].target_corpus_anchor)

    def test_q03_acoustic_impedance(self):
        q = "Does sound speed determine acoustic boundary reflection?"
        result = self.reframer.reframe(q)

        self.assertIsInstance(result, ReframedInquiry)
        self.assertIn("impedance", result.scholarqa_mechanistic_query.lower())
        self.assertIn("Feynman", result.retrieval_probes[0].target_corpus_anchor)

    def test_q05_membrane_permeability(self):
        q = "Does passive diffusion across lipid bilayer require ATP transport?"
        result = self.reframer.reframe(q)

        self.assertIsInstance(result, ReframedInquiry)
        self.assertIn("diffusion", result.scholarqa_mechanistic_query.lower())
        self.assertIn("Alberts", result.retrieval_probes[0].target_corpus_anchor)

    def test_generic_fallback(self):
        q = "Does temperature increase the electrical conductivity of semiconductors?"
        result = self.reframer.reframe(q)

        self.assertIsInstance(result, ReframedInquiry)
        self.assertGreater(len(result.scholarqa_mechanistic_query), len(q))
        self.assertGreaterEqual(len(result.decoupled_dimensions), 1)
        self.assertNotEqual(result.avoided_failure_mode, "")

    def test_empty_query_raises(self):
        with self.assertRaises(ValueError):
            self.reframer.reframe("   ")


if __name__ == "__main__":
    unittest.main()
