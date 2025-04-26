#!/bin/bash

# Replace 'username' with the actual username
USERNAME="mm"

# Get the session ID of the user
SESSION_ID=$(loginctl list-sessions | grep "$USERNAME" | awk '{print $1}')

# Check if SESSION_ID is not empty
if [ -n "$SESSION_ID" ]; then
    # Schedule the logoff at 22:00 (10:00 PM)
    echo "loginctl terminate-session $SESSION_ID" | at 23:04
else
    echo "No session found for user $USERNAME"
fi