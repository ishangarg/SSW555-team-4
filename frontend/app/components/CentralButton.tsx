import React from "react";
import { View, StyleSheet } from "react-native";
import { TouchableWithoutFeedback } from "react-native-gesture-handler";

import defaultStyles from "../config/styles";

interface Props {
  onPress: () => void;
}

const CentralButton = ({ onPress }: Props) => {
  return (
    <TouchableWithoutFeedback onPress={onPress}>
      <View>
        <View testID="big-button" style={styles.bigButton} />
        <View testID="small-button" style={styles.smallButton} />
      </View>
    </TouchableWithoutFeedback>
  );
};

const styles = StyleSheet.create({
  bigButton: {
    width: 175,
    height: 175,
    backgroundColor: defaultStyles.colors.secondary,
    borderRadius: 150,
    borderColor: defaultStyles.colors.primary,
    borderWidth: 20,
  },
  smallButton: {
    width: 85,
    height: 85,
    backgroundColor: defaultStyles.colors.accent,
    borderRadius: 50,
    position: "absolute",
    right: 10,
  },
});

export default CentralButton;
