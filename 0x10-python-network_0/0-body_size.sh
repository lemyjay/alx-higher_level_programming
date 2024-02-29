#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body response.

touch /tmp/response_body
curl -s -o /tmp/response_body "$1"

# Use the "wc" command to count the number of bytes in the response body
# The "-c" option specifies that we want to count bytes
response_size=$(wc -c < /tmp/response_body)

# Print the size of the response body in bytes
echo $response_size

# Remove the temporary file
rm /tmp/response_body
