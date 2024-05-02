# We will adjust the Python script to read the actual content from the uploaded text file.
# The file has been uploaded with the ID 'file-AtUeKT8FszeFJc6X29Uphr0M' and stored at '/mnt/data/'.
# First, we will read the content of the file.
import os
import re
import pandas as pd

# Path to the uploaded text file
file_path = "C:/Users/MrXam/Downloads/TMP.txt"


def process_course_file(filename):
    base_dir = "C:/Users/MrXam/Downloads/"

    # Complete file path
    file_path = os.path.join(base_dir, filename)
    # Function to parse the course data from the text content
    def parse_course_data(text_content):
        # Regular expression pattern to find the courses information
        course_pattern = re.compile(
            r'<span id=".*?_labelTitle">(.*?)</span>.*?'
            r'<span id=".*?_labelDescription">(.*?)</span>.*?'
            r'<span id=".*?_labelUnits">(.*?)</span>',
            re.DOTALL
        )

        # Find all courses using the regular expression pattern
        courses = course_pattern.findall(text_content)

        # Sort courses by title
        sorted_courses = sorted(courses, key=lambda x: x[0].strip())

        # Compile the sorted courses into a list with their details
        course_list = [
            {'title': title.strip(), 'description': description.strip(), 'units': units.strip()}
            for title, description, units in sorted_courses
        ]

        return course_list

    def clean_description(description):
        return re.sub(r'\s+', ' ', description)

    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Parse the course data from the file content
    course_data = parse_course_data(file_content)

    for course in course_data:
        course['description'] = clean_description(course['description'])

    # remove  duplicate
    course_data = {each['title']: each for each in course_data}.values()

    # Output the course data list
    # Adjusting the output format as requested by the user.

    # Defining a function to format the course details
    # def format_course_details(course_data):
    #    formatted_courses = []
    #   for course in course_data:
    #      formatted_course = f"Title: {course['title']}\nDescription: {course['description']}\nUnits: {course['units']}\n------"
    #     formatted_courses.append(formatted_course)
    # return "\n".join(formatted_courses)

    # Format the course details
    #formatted_course_output = format_course_details(course_data)  # Display the first 5 courses for brevity
    #output_file_path = 'C:/Users/MrXam/Downloads/formatted_course_details_tmp.txt'

    # Write the formatted course details to the file
    #with open(output_file_path, 'w') as output_file:
    #    output_file.write(formatted_course_output)

    # Provide the path to the saved file
    #output_file_path

    df_courses = pd.DataFrame(course_data)

    # Define the path for the Excel file
    base_name = os.path.splitext(file_path)[0]
    excel_file_path = base_name + '.xlsx'

    # Write the DataFrame to an Excel file
    df_courses.to_excel(excel_file_path, index=False)
    print(f"Excel file saved at: {excel_file_path}")

# List of file paths to process
filenames = ["tmp.txt", "econ.txt", "comm.txt", "cmpsc.txt"]

# Process each file in the list
for filename in filenames:
    process_course_file(filename)

