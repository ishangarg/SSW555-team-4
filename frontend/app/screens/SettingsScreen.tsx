import React from "react";
import { Text, StyleSheet } from "react-native";
import { TouchableOpacity } from "react-native-gesture-handler";
import { useNavigation } from "@react-navigation/native";

import Screen from "../components/Screen";
import { NavigationProp } from "../config/navigation";
import defaultStyles from "../config/styles";

const SettingsScreen = () => {
  const navigation = useNavigation<NavigationProp>();

  const pages: { name: string; path: any }[] = [
    { name: "Contacts", path: "Contacts" },
  ];
  return (
    <Screen style={styles.screen}>
      {pages.map(({ path, name }, index) => (
        <TouchableOpacity
          key={index}
          onPress={() => navigation.navigate(path)}
          style={styles.options}
        >
          <Text style={styles.text}>{name}</Text>
        </TouchableOpacity>
      ))}
    </Screen>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  options: {
    borderBottomColor: colors.primary,
    borderBottomWidth: 2,
  },
  screen: {
    padding: 50,
    justifyContent: "space-between",
  },
  text: {
    fontSize: subText.fontSize,
    fontWeight: subText.fontWeight,
    marginBottom: 10,
  },
});

export default SettingsScreen;
