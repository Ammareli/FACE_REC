import cv2

# Replace 'path/to/your/video.mp4' with the actual path to your video file
video_path = r'C:\Users\DELL\Documents\Zapya\Video\Aftab.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open the video file.")
    exit()

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not read successfully, break the loop
    if not ret:
        break

    # Display the frame (you can perform further processing here)
    cv2.imshow('Video Frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
