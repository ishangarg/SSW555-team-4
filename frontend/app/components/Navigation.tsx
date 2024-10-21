import React from "react";
import { View, StyleSheet } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";

import defaultStyles from "../config/styles";

const Navigation = () => {
  return (
    <View style={styles.container}>
      <MaterialCommunityIcons
        name="home"
        size={70}
        color={defaultStyles.colors.accent}
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
    justifyContent: "center",
    alignItems: "center",
  },
});

export default Navigation;
