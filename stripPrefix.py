import re

def extract_youtube_urls(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            match = re.search(r'(https?://www\.youtube\.com/watch\S*)', line)
            if match:
                outfile.write(match.group(1) + '\n')

# Example usage
input_filename = 'in.md'  # Replace with your actual input file
output_filename = 'outputnoprefix.md'  # Replace with your desired output file
extract_youtube_urls(input_filename, output_filename)
print(f'Extracted URLs saved to {output_filename}')

