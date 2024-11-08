import { Audio } from "expo-av";

export const recordingOptions: Audio.RecordingOptions = {
  android: {
    extension: ".mp4", // Was .m4a
    outputFormat: 2, // MPEG_4
    audioEncoder: 3, // AAC
    sampleRate: 44100,
    numberOfChannels: 2,
    bitRate: 128000,
  },
  ios: {
    extension: ".mp4", // Was .m4a
    audioQuality: 127, // AVAudioQuality.high
    sampleRate: 44100,
    numberOfChannels: 2,
    bitRate: 128000,
    linearPCMBitDepth: 16,
    linearPCMIsBigEndian: false,
    linearPCMIsFloat: false,
  },
  web: {
    mimeType: undefined,
    bitsPerSecond: undefined,
  },
};
