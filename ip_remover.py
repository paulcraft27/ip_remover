import re

# Ask the user to enter the input file name
input_file_name = input("Enter the name of the input file: ")

# Open the input file for reading
with open(input_file_name, "r") as input_file:
  # Read the file contents
    file_contents = input_file.read()
 
# Define a regular expression pattern to match IP addresses
ip_pattern = r"http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
 
# Use the re module to find all matches of the IP address pattern in the file contents
ip_matches = re.findall(ip_pattern, file_contents)
 
# Loop through each IP address match and remove it from the file contents
for ip_address in ip_matches:
    file_contents = file_contents.replace(ip_address, "")
 
# Ask the user to enter the output file name
output_file_name = input("Enter the name of the output file: ")
 
# Open the output file for writing and write the updated file contents
with open(output_file_name, "w") as output_file:
     output_file.write(file_contents)
