def get_media_type(filename):
    # Convert the filename to lowercase for case-insensitive comparison
    filename = filename.lower()

    # Define the mapping of file extensions to media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Check if the filename ends with any of the specified suffixes
    for suffix in media_types:
        if filename.endswith(suffix):
            return media_types[suffix]

    # If no matching suffix is found, return the default media type
    return 'application/octet-stream'

# Prompt the user for the filename
filename = input("Enter the filename: ")

# Get the media type of the file
media_type = get_media_type(filename)

# Output the media type
print("Media type:", media_type)