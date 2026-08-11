import unittest

from src.mortgage import calculate_five_year_mortgage


class MortgageBehaviorTest(unittest.TestCase):
    def test_standard_five_year_loan(self):
        result = calculate_five_year_mortgage(300000, 0.06)
        self.assertAlmostEqual(result["monthly_payment"], 5799.84, places=2)
        self.assertAlmostEqual(result["total_interest"], 47990.49, places=2)
        self.assertEqual(len(result["schedule"]), 60)
        self.assertAlmostEqual(result["schedule"][0]["interest"], 1500.00, places=2)
        self.assertAlmostEqual(result["schedule"][-1]["balance"], 0.00, places=2)

    def test_zero_interest_loan(self):
        result = calculate_five_year_mortgage(120000, 0.0)
        self.assertEqual(result["monthly_payment"], 2000.00)
        self.assertEqual(result["total_paid"], 120000.00)
        self.assertEqual(result["total_interest"], 0.00)

    def test_payment_breakdown_conserves_each_month(self):
        result = calculate_five_year_mortgage(100000, 0.05)
        for row in result["schedule"]:
            self.assertAlmostEqual(
                row["payment"], row["principal"] + row["interest"], places=2
            )

    def test_rejects_invalid_terms(self):
        with self.assertRaises(ValueError):
            calculate_five_year_mortgage(0, 0.05)
        with self.assertRaises(ValueError):
            calculate_five_year_mortgage(100000, -0.01)
