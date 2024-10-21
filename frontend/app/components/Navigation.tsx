import React from "react";
import { View, StyleSheet } from "react-native";
import { MaterialCommunityIcons, MaterialIcons } from "@expo/vector-icons";

import defaultStyles from "../config/styles";

const Navigation = () => {
  return (
    <View style={styles.container}>
      <MaterialCommunityIcons
        name="apps"
        size={70}
        color={defaultStyles.colors.primary}
      />

      <View>
        <View testID="big-button" style={styles.bigButton} />
        <View testID="small-button" style={styles.smallButton} />
      </View>

      <MaterialIcons
        name="settings"
        size={70}
        color={defaultStyles.colors.primary}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    width: "100%",
    height: 70,
    position: "absolute",
    bottom: 20,
    borderTopColor: defaultStyles.colors.light,
    borderTopWidth: 2,
    paddingHorizontal: 20,
    justifyContent: "space-around",
    alignItems: "center",
    flexDirection: "row",
  },
  bigButton: {
    width: 60,
    height: 60,
    backgroundColor: defaultStyles.colors.secondary,
    borderRadius: 150,
    borderColor: defaultStyles.colors.primary,
    borderWidth: 10,
  },
  smallButton: {
    width: 20,
    height: 20,
    backgroundColor: defaultStyles.colors.accent,
    borderRadius: 50,
    position: "absolute",
    right: 10,
  },
});

export default Navigation;
