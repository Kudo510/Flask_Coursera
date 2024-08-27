from IBM_cloud_sentiment_analysis import analyze_sentiment
import unittest


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
    # Test case for positive sentiment
        result_1 = analyze_sentiment('I love working with Python')
        self.assertEqual(result_1["label"], 'positive')
        
        # Test case for negative sentiment
        result_2 = analyze_sentiment('I hate working with Python')
        self.assertEqual(result_2["label"], 'negative')
        
        # Test case for neutral sentiment
        result_3 = analyze_sentiment('I am neutral on Python')
        self.assertEqual(result_3["label"], 'neutral')

unittest.main()