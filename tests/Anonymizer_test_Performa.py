import unittest
import time
import tempfile

from main import main
from utils import remove_accents
from pii_detection import identify_pii
from redaction import redact_text


class AnonimyzerTests(unittest.TestCase):
    """
    A class containing unit tests for the PII anonymizer functions.
    """
    # Unit Tests

    def test_remove_accents(self):
        """
        Tests the `remove_accents` function that removes accents from a string.

        Args:
            text (str): The text with accents to be removed.

        Returns:
            str: The text with accents removed.
        """
        self.assertEqual(remove_accents('café'), 'cafe')
        self.assertEqual(remove_accents('àguila'), 'aguila')
        self.assertEqual(remove_accents('Mercè'), 'Merce')
        self.assertEqual(remove_accents('Heràldica'), 'Heraldica')

    def test_identify_pii(self):
        """
        Tests the `identify_pii` function that identifies PII entities in a text.

        Args:
            text (str): The text to be scanned for PII entities.

        Returns:
            list: A list of tuples where each tuple represents a PII entity:
                (start_index, end_index, entity_type)
        """
        text = "Mercè Doe uses the email address merce.doe@example.com and his ID number is 234564."
        expected = [(0, 9, 'PERSON'), (76, 82, 'CARDINAL'), (33, 54, 'EMAIL')]
        self.assertEqual(identify_pii(text), expected)


    def test_redact_text(self):
        """
        Tests the `redact_text` function that redacts PII entities in a text.

        Args:
            text (str): The text containing PII entities.
            pii_entities (list): A list of tuples representing PII entities,
                                 same format as returned by `identify_pii`.

        Returns:
            str: The redacted text with PII entities replaced with placeholders.
        """
        text = "Mercè Doe's email is mercè.doe@example.com."
        pii_entities = [(0, 9, 'PERSON'), (21, 42, 'EMAIL')]
        expected = "[PERSON]'s email is [EMAIL]."
        self.assertEqual(redact_text(text, pii_entities), expected)

    def test_performance(self):
        """
        Tests the performance of the entire anonymization process by measuring
        the execution time for a large document. Approx 0.5 s per page.

        Args:
            large_doc_path(str): The path to the document to be redacted.

        Raises:
            AssertionError: If the execution time exceeds the specified threshold.
        """
        large_doc_path = 'Sworn1.docx'

        start_time = time.time()
        output_file = tempfile.mktemp(suffix='.docx')
        # output_file = 'Sworn1_C.docx'
        main(large_doc_path, output_file)
        end_time = time.time()

        execution_time = end_time - start_time
        # Time threshold based on number of pages. 0.5s/page.
        self.assertLess(execution_time, 0.6, "Redaction took too long")


if __name__ == '__main__':
    unittest.main()
