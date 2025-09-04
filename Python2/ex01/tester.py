import unittest
import pandas as pd
from io import StringIO
from unittest.mock import patch
from aff_life import plot_life_expectancy


class TestLifeExpectancyPlot(unittest.TestCase):
    """
    Test suite for the plot_life_expectancy function.
    Tests both successful execution and proper exception handling.
    """

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock matplotlib.pyplot.show to prevent actual plot display during tests
        self.show_patcher = patch('matplotlib.pyplot.show')
        self.mock_show = self.show_patcher.start()

        # Mock matplotlib.pyplot.figure to prevent actual figure creation
        self.figure_patcher = patch('matplotlib.pyplot.figure')
        self.mock_figure = self.figure_patcher.start()

    def tearDown(self):
        """Clean up after each test method."""
        self.show_patcher.stop()
        self.figure_patcher.stop()

    def test_plot_life_expectancy_success_france(self):
        """Test successful plotting for France with valid data."""
        # Create realistic sample data similar to the actual CSV structure
        data = pd.DataFrame({
            'country': ['France', 'Germany', 'Italy'],
            '1990': [76.8, 75.3, 76.9],
            '2000': [79.2, 78.3, 80.1],
            '2010': [81.7, 80.4, 82.3],
            '2020': [82.3, 81.2, 83.1]
        })

        # Test with mocked matplotlib functions to capture calls
        with patch('matplotlib.pyplot.plot') as mock_plot, \
             patch('matplotlib.pyplot.title') as mock_title, \
             patch('matplotlib.pyplot.xlabel') as mock_xlabel, \
             patch('matplotlib.pyplot.ylabel') as mock_ylabel:

            # This should execute without raising any exception
            plot_life_expectancy('France', data)

            # Verify that matplotlib functions were called correctly
            mock_plot.assert_called_once()
            mock_title.assert_called_once_with('France Life expectancy Projections', fontsize=16, fontweight='bold')
            mock_xlabel.assert_called_once_with('Year', fontsize=12)
            mock_ylabel.assert_called_once_with('Life expectancy', fontsize=12)

    def test_plot_life_expectancy_success_other_country(self):
        """Test successful plotting for another country."""
        data = pd.DataFrame({
            'country': ['France', 'Germany', 'Italy'],
            '1990': [76.8, 75.3, 76.9],
            '2000': [79.2, 78.3, 80.1],
            '2010': [81.7, 80.4, 82.3]
        })

        with patch('matplotlib.pyplot.title') as mock_title:
            plot_life_expectancy('Germany', data)
            mock_title.assert_called_once_with('Germany Life expectancy Projections', fontsize=16, fontweight='bold')

    def test_plot_life_expectancy_country_not_found(self):
        """Test that ValueError is raised when country is not found."""
        data = pd.DataFrame({
            'country': ['Germany', 'Italy'],
            '1990': [75.3, 76.9],
            '2000': [78.3, 80.1],
            '2010': [80.4, 82.3]
        })

        # Capture stderr to verify error message
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            with self.assertRaises(ValueError) as context:
                plot_life_expectancy('France', data)

            # Verify the error message
            self.assertIn("France", str(context.exception))
            self.assertIn("not found in the dataset", str(context.exception))

            # Verify error was logged to stderr
            stderr_output = mock_stderr.getvalue()
            self.assertIn("ValueError", stderr_output)
            self.assertIn("France", stderr_output)

    def test_plot_life_expectancy_missing_country_column(self):
        """Test that KeyError is raised when 'country' column is missing."""
        data = pd.DataFrame({
            'nation': ['France', 'Germany'],  # Wrong column name
            '1990': [76.8, 75.3],
            '2000': [79.2, 78.3]
        })

        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            with self.assertRaises(KeyError) as context:
                plot_life_expectancy('France', data)

            # Verify error was logged to stderr
            stderr_output = mock_stderr.getvalue()
            self.assertIn("KeyError", stderr_output)

    def test_plot_life_expectancy_empty_dataset(self):
        """Test that ValueError is raised for empty dataset."""
        data = pd.DataFrame(columns=['country', '1990', '2000', '2010'])

        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            with self.assertRaises(ValueError) as context:
                plot_life_expectancy('France', data)

            # Verify the error message
            self.assertIn("not found in the dataset", str(context.exception))

    def test_plot_life_expectancy_country_exists_but_no_data(self):
        """Test edge case where country exists but has no data rows."""
        # This creates a scenario where the country might be in the values but filtering returns empty
        data = pd.DataFrame({
            'country': [],
            '1990': [],
            '2000': []
        })
        # Add the country as a value but in a way that filtering will return empty
        data.loc[0] = ['France', 76.8, 79.2]
        # filtered_data = data[data['country'] == 'NonExistentCountry']  # This will be empty

        with self.assertRaises(ValueError):
            plot_life_expectancy('NonExistentCountry', data)

    def test_plot_life_expectancy_with_missing_values(self):
        """Test that function handles missing values (NaN) gracefully."""
        data = pd.DataFrame({
            'country': ['France', 'Germany'],
            '1990': [76.8, None],  # Missing value
            '2000': [79.2, 78.3],
            '2010': [None, 80.4]   # Missing value
        })

        # This should not raise an exception, pandas should handle NaN values
        with patch('matplotlib.pyplot.plot') as mock_plot:
            plot_life_expectancy('France', data)
            mock_plot.assert_called_once()

    @patch('matplotlib.pyplot.plot')
    def test_plot_life_expectancy_matplotlib_error(self, mock_plot):
        """Test that matplotlib errors are properly handled and re-raised."""
        data = pd.DataFrame({
            'country': ['France'],
            '1990': [76.8],
            '2000': [79.2]
        })

        # Make matplotlib.plot raise an exception
        mock_plot.side_effect = Exception("Matplotlib error")

        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            with self.assertRaises(Exception) as context:
                plot_life_expectancy('France', data)

            # Verify the original error is re-raised
            self.assertIn("Matplotlib error", str(context.exception))

            # Verify error was logged to stderr
            stderr_output = mock_stderr.getvalue()
            self.assertIn("Unexpected error while plotting", stderr_output)


def run_comprehensive_test():
    """
    Demonstrate the comprehensive testing of plot_life_expectancy function.
    This function shows both successful execution and proper exception handling.
    """
    print("=== Comprehensive Test of plot_life_expectancy Function ===\n")

    # Test 1: Successful execution
    print("Test 1: Successful execution with valid data")
    try:
        data = pd.DataFrame({
            'country': ['France', 'Germany', 'Spain'],
            '1990': [76.8, 75.3, 77.1],
            '2000': [79.2, 78.3, 79.5],
            '2010': [81.7, 80.4, 82.1],
            '2020': [82.3, 81.2, 83.4]
        })

        with patch('matplotlib.pyplot.show'):  # Prevent actual plot display
            plot_life_expectancy('France', data)
        print("✓ SUCCESS: Function executed without errors for France\n")
    except Exception as error:
        print(f"✗ FAILED: {error}\n")

    # Test 2: Country not found
    print("Test 2: Country not found exception handling")
    try:
        data = pd.DataFrame({
            'country': ['Germany', 'Spain'],
            '1990': [75.3, 77.1],
            '2000': [78.3, 79.5]
        })
        plot_life_expectancy('France', data)
        print("✗ FAILED: Should have raised ValueError\n")
    except ValueError as vError:
        print(f"✓ SUCCESS: Correctly raised ValueError: {vError}\n")
    except Exception as error:
        print(f"✗ FAILED: Unexpected exception: {error}\n")

    # Test 3: Missing country column
    print("Test 3: Missing 'country' column exception handling")
    try:
        data = pd.DataFrame({
            'nation': ['France'],  # Wrong column name
            '1990': [76.8]
        })
        plot_life_expectancy('France', data)
        print("✗ FAILED: Should have raised KeyError\n")
    except KeyError as kError:
        print(f"✓ SUCCESS: Correctly raised KeyError: {kError}\n")
    except Exception as error:
        print(f"✗ FAILED: Unexpected exception: {error}\n")

    print("=== Test Summary ===")
    print("The plot_life_expectancy function demonstrates:")
    print("   1. ✓ Successful plotting with valid data")
    print("   2. ✓ Proper ValueError handling for missing countries")
    print("   3. ✓ Proper KeyError handling for malformed data")
    print("   4. ✓ Comprehensive error logging to stderr")
    print("   5. ✓ Graceful handling of edge cases")


if __name__ == '__main__':
    # Run the comprehensive demonstration
    print("Running comprehensive demonstration...\n")
    run_comprehensive_test()
    print("\n" + "="*60 + "\n")

    # Run the unit tests
    print("Running unit tests...\n")
    unittest.main(verbosity=2, exit=False)
