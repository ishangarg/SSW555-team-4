import { useState, useEffect } from "react";
import { Audio } from "expo-av";

export const useAudioRecorder = (recordingOptions: Audio.RecordingOptions) => {
  const [recording, setRecording] = useState<Audio.Recording | null>(null);
  const [recordingUri, setRecordingUri] = useState<string | null>(null);
  const [sound, setSound] = useState<Audio.Sound | null>(null);

  // Start recording
  const startRecording = async () => {
    try {
      const permission = await Audio.requestPermissionsAsync();
      if (permission.status === "granted") {
        await Audio.setAudioModeAsync({
          allowsRecordingIOS: true,
          playsInSilentModeIOS: true,
        });

        const { recording } = await Audio.Recording.createAsync(
          recordingOptions
        );
        setRecording(recording);
        console.log("Recording started");
      } else {
        console.log("Permission to access microphone not granted");
      }
    } catch (err) {
      console.error("Failed to start recording", err);
    }
  };

  // Stop recording and get the URI
  const stopRecording = async () => {
    if (!recording) return;

    try {
      await recording.stopAndUnloadAsync();
      const uri = recording.getURI();
      setRecordingUri(uri || null);
      console.log("Recording stopped and stored at", uri);
    } catch (error) {
      console.error("Error stopping recording", error);
    }

    setRecording(null);
  };

  // Play the recorded audio
  const playSound = async () => {
    if (!recordingUri) return;

    try {
      const { sound } = await Audio.Sound.createAsync({ uri: recordingUri });
      setSound(sound);
      await sound.playAsync();
      console.log("Playing sound");
    } catch (error) {
      console.error("Error playing sound", error);
    }
  };

  // Upload recording to a backend service
  const uploadRecording = async (
    endpoint: string
  ): Promise<string | undefined> => {
    if (!recordingUri) return;

    const formData = new FormData();
    formData.append("audio", {
      uri: recordingUri,
      name: "recording.m4a", // Change this as needed
      type: "audio/m4a", // Ensure this matches what the server expects
    } as any);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        body: formData,
        headers: {
          "Content-Type": "multipart/form-data", // Important for file uploads
        },
      });

      if (response.ok) {
        console.log("Upload successful!");
        return await response.text(); // This will get the text response from the endpoint
      } else {
        console.error("Upload failed:", await response.text()); // This will get the response's error message if the endpoint encounters a problem
      }
    } catch (error) {
      console.error("Error uploading recording:", error); // This will display the error if there is a problem connecting with the endpoint
    }
    return undefined;
  };

  // Cleanup sound when component unmounts
  useEffect(() => {
    return () => {
      if (sound) {
        sound.unloadAsync();
      }
    };
  }, [sound]);

  return {
    recording,
    recordingUri,
    startRecording,
    stopRecording,
    playSound,
    uploadRecording,
  };
};
