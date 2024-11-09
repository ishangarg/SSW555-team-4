import React, { useState } from "react";
import { Button, StyleSheet, Text, View } from "react-native";

import Screen from "../components/Screen";
import CentralButton from "../components/CentralButton";
import defaultStyles from "../config/styles";
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
    const endpoint = "/transcribe_audio"; // Replace with your backend URL

    try {
      const textFromSpeech = await uploadRecording(endpoint);

      if (textFromSpeech) {
        setText(textFromSpeech);
        console.log("Text received from speech:", textFromSpeech);
      } else {
        console.log("No text received from the server.");
        setText("No text could be extracted from the audio.");
      }
    } catch (error) {
      console.error("Error during speech processing:", error);
      setText(
        `Error processing speech: ${
          error instanceof Error ? error.message : String(error)
        }`
      );
    }

    console.log("Audio processing complete");
    // setText("This is what the speech to text will look like.");
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
      <Text
      // Need to truncate the text so that it does not look too crazy
      >
        {text}
      </Text>
    </Screen>
  );
};

const styles = StyleSheet.create({
  buttonContainer: {
    position: "absolute",
    top: 50, // Sets the location of the central button
  },

  recordingText: {
    position: "absolute",
    top: "30%",
    fontSize: defaultStyles.text.fontSize,
    fontWeight: defaultStyles.text.fontWeight,
  },
  screen: {
    justifyContent: "center",
    alignItems: "center",
  },
});

export default HomeScreen;
