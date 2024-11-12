import React from "react";
import Screen from "../components/Screen";
import { StyleSheet, Text } from "react-native";
import defaultStyles from "../config/styles";

const TermsOfUseScreen = () => {
  return (
    <Screen style={styles.screen}>
      <Text style={[styles.header, { textAlign: "center" }]}>Terms of Use</Text>
      <Text style={styles.text}>
        By using our platform, you accept the inherent risks of using an
        artificial intelligence assistant. By being a user of this app, you
        waive the right to hold its creators liable for any and all possible
        legal consequences resulting from action or inaction based on the
        assistant's recommendation. {"\n"}
        {"\n"}While the assistant is an artificial intelligence, it is open to
        possible failures and errors. As a result, it is important to seek
        medical advice from medical professionals. This service should not be in
        replacement of traditional services, but a supplemental effort.
      </Text>
    </Screen>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  header: {
    fontSize: text.fontSize,
    fontWeight: text.fontWeight,
    marginBottom: 20,
  },
  screen: {
    padding: 50,
  },
  text: {
    fontSize: subText.fontSize,
  },
});

export default TermsOfUseScreen;
