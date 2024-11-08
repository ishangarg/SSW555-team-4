import React from "react";
import { TextInput, StyleSheet, View, Platform } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import defaultStyles from "../config/styles";

interface Props {
  icon?: string;
  [key: string]: any; // Allows us to Spread Props with TypeScrip
}

const AppInputField = ({ icon, ...otherProps }: Props) => {
  return (
    <View style={styles.container}>
      {icon && (
        <MaterialCommunityIcons
          name={icon as any}
          size={25}
          color={defaultStyles.colors.secondary}
          style={styles.icon}
        />
      )}
      <TextInput style={styles.text} {...otherProps} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: defaultStyles.colors.off_white,
    borderRadius: 25,
    flexDirection: "row",
    width: "100%",
    padding: 15,
    marginVertical: 10,
    alignItems: "center",
    marginBottom: 20,
  },
  icon: { marginRight: 10 },
  text: {
    color: defaultStyles.colors.black,
    flex: 1,
    fontSize: defaultStyles.subText.fontSize,
    fontWeight: defaultStyles.subText.fontWeight,
  },
});

export default AppInputField;
