from datetime import datetime
import os

def create_timestamped_file():
    # Get the current timestamp
    current_timestamp = datetime.now()
    # Format the current timestamp as a string
    timestamp_string = current_timestamp.strftime('%Y-%m-%d_%H-%M-%S')
    
    # Create a filename with the current timestamp
    filename = f"timestamped_file_{timestamp_string}.txt"
    
    # Create and open the file in write mode
    with open(filename, 'w') as file:
        # Write the current timestamp as the content of the file
        file.write(f"Current Timestamp: {timestamp_string}")
    
    # Print a message indicating the file has been created
    print(f"File '{filename}' has been created with the content of the current timestamp.")

# Call the function to create a timestamped file
create_timestamped_file()



from datetime import datetime
import os

def create_timestamped_file():
    # Get the current timestamp
    current_timestamp = datetime.now()
    # Format the current timestamp as a string
    timestamp_string = current_timestamp.strftime('%Y-%m-%d_%H-%M-%S')
    
    # Create a filename with the current timestamp
    filename = f"timestamped_file_{timestamp_string}.txt"
    
    # Create and open the file in write mode
    with open(filename, 'w') as file:
        # Write the current timestamp as the content of the file
        file.write(f"Current Timestamp: {timestamp_string}")
    
    # Print a message indicating the file has been created
    print(f"File '{filename}' has been created with the content of the current timestamp.")
    return filename  # Return the filename so it can be used for reading

def read_and_display_file_content(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Display the content of the file in the console
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        # Handle other possible exceptions
        print(f"An error occurred while reading the file '{filename}': {e}")

# Main script
if __name__ == '__main__':
    # Create a timestamped file
    filename = create_timestamped_file()
    
    # Print the current working directory and list of files for troubleshooting
    print("Current working directory:", os.getcwd())
    print("Files in current directory:", os.listdir())
    
    # Read and display the content of the created file
    read_and_display_file_content(filename)
