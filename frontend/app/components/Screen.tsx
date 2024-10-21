import React from "react";
import { SafeAreaView, ViewStyle, StyleSheet } from "react-native";
import Constants from "expo-constants";
import defaultStyles from "../config/styles";

interface Props {
  children: any;
  style?: ViewStyle;
}

const Screen = ({ children, style }: Props) => {
  return <SafeAreaView style={[styles.screen, style]}>{children}</SafeAreaView>;
};

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    paddingTop: Constants.statusBarHeight,
    backgroundColor: defaultStyles.colors.white,
  },
});
export default Screen;
