import React, { useState } from "react";
import { Button, StyleSheet, Text, View } from "react-native";
import { MaterialIcons } from "@expo/vector-icons";

import Screen from "../components/Screen";
import CentralButton from "../components/CentralButton";
import defaultStyles from "../config/styles";
import Navigation from "../components/Navigation";
import { useAudioRecorder } from "../hooks/useAudioRecorder";
import { recordingOptions } from "../config/audioRecordingOptions";

const HomeScreen = () => {
  const {
    recording,
    recordingUri,
    startRecording,
    stopRecording,
    playSound,
    uploadRecording,
  } = useAudioRecorder(recordingOptions);

  const [text, setText] = useState<string | undefined>();

  const handleUpload = async () => {
    // This method will submit the voice recording to the backend to convert the audio to text
    // Should receive the text as a response

    // Below will be integrated when the Endpoint is complete

    // const endpoint = "https://your-backend-service.com/upload"; // Replace with your backend URL

    // try {
    //   const textFromSpeech = await uploadRecording(endpoint);

    //   if (textFromSpeech) {
    //     setText(textFromSpeech);
    //     console.log("Text received from speech:", textFromSpeech);
    //   } else {
    //     console.log("No text received from the server.");
    //     setText("No text could be extracted from the audio.");
    //   }
    // } catch (error) {
    //   console.error("Error during speech processing:", error);
    //   setText(
    //     `Error processing speech: ${
    //       error instanceof Error ? error.message : String(error)
    //     }`
    //   );
    // }

    console.log("Audio processing complete");
    setText("This is what the text will look like");
  };

  return (
    <Screen style={styles.screen}>
      <Text style={styles.recordingText}>
        {recording ? "Stop Recording" : "Start Recording"}
      </Text>
      <View style={styles.buttonContainer}>
        <CentralButton
          onPress={async () => {
            if (recording) {
              await stopRecording(); // Stop recording and get URI
              handleUpload(); // Upload after stopping
            } else {
              startRecording(); // Start recording
            }
          }}
        />
      </View>

      {recordingUri && (
        // Once the speech to text is implemented we will
        // Not need the play recording button because people can see what they said
        <View
          style={{
            position: "absolute",
            bottom: 200,
            backgroundColor: defaultStyles.colors.primary,
            padding: 10,
            borderRadius: 10,
          }}
        >
          <Button
            title="Play Recording"
            color={defaultStyles.colors.white}
            onPress={playSound}
          />
        </View>
      )}
      <Text>{text}</Text>
      <Navigation />
    </Screen>
  );
};

const styles = StyleSheet.create({
  buttonContainer: {
    position: "absolute",
    top: 100,
  },

  recordingText: {
    position: "absolute",
    top: "35%",
    fontWeight: "600",
    fontSize: 28,
  },
  screen: {
    justifyContent: "center",
    alignItems: "center",
  },
});

export default HomeScreen;
