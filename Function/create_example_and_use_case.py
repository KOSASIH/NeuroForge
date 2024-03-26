# Import necessary libraries
import os
import sqlite3
import frontmatter
import sqlite3
import openai

# Define paths and API key
path_neuroforge = "~/Documents/neuroforge_software"
path_documentation = "~/Documents/neuroforge_documentation"
openai.api_key = "your_openai_api_key"

# Connect to SQLite database
conn = sqlite3.connect("examples.db")

# Define SQL query
query = "SELECT * FROM examples WHERE type='use_case'"

# Parse markdown files
def parse_markdown(file):
    """
    Parses a markdown file using frontmatter
    """
    with open(file, "r") as f:
        markdown_file = f.read()

    parsed_file = frontmatter.parse(markdown_file)
    if parsed_file:
        return parsed_file

# Compute embedding of a file
def compute_embedding(file):
    """
    Compute the embedding vector of a file
    """
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=file
    )

    return response["data"][0]["embedding"]

# Iterate over use cases
use_cases = []
for row in conn.execute(query):
    use_case_path = os.path.join(path_ documentation, "use_cases", row["filename"])

    if os.path.exists(use_case_path):
        use_cases.append((row["title"], compute_embedding(open(use_case_path, "r").read())))

# Create examples and use cases markdown files
with open(os.path.join(path_neuroforge, "README.md"), "r") as neuroforge_file:
    neuroforge_file_data = neuroforge_file.read()

    neuroforge_parsed = frontmatter.parse(neuroforge_file_data)

    if "examples_and_use_cases" not in neuroforge_parsed:
        neuroforge_parsed["examples_and_use_cases"] = {
            "examples": [],
            "use_cases": []
        }

    for use_case in use_cases:
        neuroforge_parsed["examples_and_use_cases"]["use_cases"].append({
            "title": use_case[0],
            "embedding": use_case[1],
            "path": os.path.basename(use_case_path)
        })

    with open(os.path.join(path_documentation, "examples_and_use_cases.md"), "w") as examples_and_use_cases_file:
        examples_and_use_cases_file.write(frontmatter.dumps(neuroforge_parsed))

# Close SQLite database
conn.close()
