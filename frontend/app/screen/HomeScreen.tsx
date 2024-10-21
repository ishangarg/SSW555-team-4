import React from "react";
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

  const handleUpload = async () => {
    // const endpoint = "https://your-backend-service.com/upload"; // Replace with your backend URL
    // await uploadRecording(endpoint);
    console.log("Now would be when the sound is sent to the backend");
  };

  return (
    <Screen style={styles.screen}>
      <Text style={styles.recordingText}>
        {recording ? "Stop Recording" : "Start Recording"}
      </Text>
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
      {recordingUri && (
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
      <Navigation />
    </Screen>
  );
};

const styles = StyleSheet.create({
  recordingText: {
    position: "absolute",
    top: "30%",
    fontWeight: "600",
    fontSize: 28,
  },
  screen: {
    justifyContent: "center",
    alignItems: "center",
  },
  settings: {
    position: "absolute",
    top: 60,
    right: 20,
  },
});

export default HomeScreen;
