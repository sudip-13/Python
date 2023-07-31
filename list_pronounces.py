import win32com.client
lst=["Rohit Sharma","Virat kohli"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
for i in range(len(lst)):
    speaker.Speak(f"Shoutout to {lst[i]}")