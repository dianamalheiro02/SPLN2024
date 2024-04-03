from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_text_sentiment(filename, output_file):
    try:
        # Attempt to open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Initialize the VADER sentiment intensity analyzer
        analyzer = SentimentIntensityAnalyzer()
        
        # Analyze the sentiment of the text
        scores = analyzer.polarity_scores(text)
        
        # Prepare the results string
        results = f"Negative: {scores['neg']}\n" \
                  f"Neutral: {scores['neu']}\n" \
                  f"Positive: {scores['pos']}\n" \
                  f"Compound: {scores['compound']}\n"
        
        # Append the results to the output file
        with open(output_file, 'a', encoding='utf-8') as out_file:
            # Determine the analysis number
            analysis_number = sum(1 for line in open(output_file, 'r') if line.startswith('#')) + 1
            out_file.write(f"# Analysis #{analysis_number}\n{results}\n")
        
        print("Sentiment analysis results appended to:", output_file)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure the file exists and the path is correct.")

if __name__ == "__main__":
    # Prompt the user to enter the filename
    filename = input("Enter the name of the text file for sentiment analysis: ")
    output_file = "outVader.txt"  # Output file where results are appended
    analyze_text_sentiment(filename, output_file)
