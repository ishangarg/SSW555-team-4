import React from "react";
import { StyleSheet, Text, ViewStyle } from "react-native";
import { TouchableOpacity } from "react-native-gesture-handler";
import defaultStyles from "../config/styles";

interface Props {
  onPress: () => any;
  title: string;
  color?: string;
  style?: ViewStyle;
}

const AppButton = ({ onPress, title, color = "primary", style }: Props) => {
  return (
    <TouchableOpacity
      onPress={onPress}
      style={[
        styles.button,
        { backgroundColor: defaultStyles.colors[color] },
        style,
      ]} // Using the [] to find the color
    >
      <Text style={styles.text}>{title}</Text>
    </TouchableOpacity>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  button: {
    backgroundColor: colors.primary,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    width: "100%",
    borderRadius: "20%",
  },
  text: {
    color: colors.white,
    fontSize: subText.fontSize,
    textTransform: "uppercase",
    fontWeight: "bold",
  },
});

export default AppButton;
