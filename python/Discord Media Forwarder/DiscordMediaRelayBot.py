import requests
import json
import random
import time

# Define the IDs of the source and destination channels
SOURCE_CHANNEL_ID = #SOURCE_CHANNEL_ID
DESTINATION_CHANNEL_ID = #DESTINATION_CHANNEL_ID

# Define the headers for the API requests
headers = {
 'Authorization': 'AUTH-ID'
}

# Initialize the ID of the last message processed
last_message_id = None

# Initialize the counters for the number of messages sent and the total time elapsed
num_sent = 0
total_time = 0

# Ask the user what type of media they want to send
print("Select the type of media to send:")
print("1. Images only")
print("2. Videos only")
print("3. Both images and videos")
choice = input("Enter your choice (1-3): ")

# Based on the user's choice, define the file types to process
if choice == '1':
 file_types = ['.jpg', '.jpeg', '.png', '.gif']
elif choice == '2':
 file_types = ['.mp4', '.mov']
else:
 file_types = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov']

# Start the main loop
while True:
 # Define the parameters for the API request
 query_parameters = f'limit=100'
 if last_message_id is not None:
     query_parameters += f'&before={last_message_id}'

 # Send a GET request to the API to fetch the messages
 r = requests.get(
     f'https://discord.com/api/v9/channels/{SOURCE_CHANNEL_ID}/messages?{query_parameters}', headers=headers
 )

 # Parse the JSON response
 jsonn = json.loads(r.text)

 # If there are no more messages to process, break the loop
 if len(jsonn) == 0:
     break

 # Process each message
 for value in jsonn:
     # If the message has attachments
     if 'attachments' in value:
         # Process each attachment
         for attachment in value['attachments']:
             # If the attachment is of the selected file type
             if attachment['filename'].endswith(tuple(file_types)):
               # Get the URL of the file
               file_url = attachment['url']
               # Send the URL to the destination channel
               payload = {"content": file_url}
               res = requests.post(f'https://discord.com/api/v9/channels/{DESTINATION_CHANNEL_ID}/messages', headers=headers, data=payload)
               print(f"Message #{num_sent + 1} sent. URL: {file_url}")
               num_sent += 1
               # Pause for a random amount of time between 25 and 40 seconds
               pause_duration = random.randint(25, 40)
               print(f"\nPausing for {pause_duration} seconds...")
               time.sleep(pause_duration)
               total_time += pause_duration
               # If this is the 7-15th message sent, pause for a random amount of time up to 2 minutes
               if num_sent % 10 == 0:
                  pause_duration = random.randint(0, 120)
                  print(f"\nPausing for {pause_duration} seconds...")
                  time.sleep(pause_duration)
                  total_time += pause_duration
                  # Print the statistics
                  print(f"\nStatistics after sending {num_sent} messages:")
                  print(f"Total time elapsed: {total_time / 60} minutes")

 # Update the ID of the last message processed
 last_message_id = value['id']

# Print the final statistics
print(f"\nFinal statistics:")
print(f"Sent {num_sent} messages over a total of {total_time / 60} minutes.")
