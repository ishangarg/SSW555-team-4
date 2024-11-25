import React from "react";
import { View, StyleSheet, Touchable } from "react-native";
import { MaterialCommunityIcons, MaterialIcons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";

import defaultStyles from "../config/styles";
import { NavigationProp } from "../config/navigation";
import { TouchableWithoutFeedback } from "react-native-gesture-handler";

const Navigation = () => {
  const navigation = useNavigation<NavigationProp>();

  return (
    <View style={styles.container}>
      <TouchableWithoutFeedback
        onPress={() =>
          navigation.reset({ index: 0, routes: [{ name: "Analytics" }] })
        }
      >
        <MaterialCommunityIcons
          name="apps"
          size={70}
          color={defaultStyles.colors.primary}
        />
      </TouchableWithoutFeedback>

      <TouchableWithoutFeedback
        onPress={() =>
          navigation.reset({ index: 0, routes: [{ name: "Home" }] })
        }
      >
        <View testID="big-button" style={styles.bigButton} />
        <View testID="small-button" style={styles.smallButton} />
      </TouchableWithoutFeedback>
      <TouchableWithoutFeedback
        onPress={() =>
          navigation.reset({ index: 0, routes: [{ name: "Settings" }] })
        }
      >
        <MaterialIcons
          name="settings"
          size={70}
          color={defaultStyles.colors.primary}
        />
      </TouchableWithoutFeedback>
    </View>
  );
};

const styles = StyleSheet.create({
  bigButton: {
    width: 60,
    height: 60,
    backgroundColor: defaultStyles.colors.white,
    borderRadius: 150,
    borderColor: defaultStyles.colors.primary,
    borderWidth: 10,
  },
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
  smallButton: {
    width: 20,
    height: 20,
    backgroundColor: defaultStyles.colors.accent,
    borderColor: defaultStyles.colors.white,
    borderWidth: 1,
    borderRadius: 50,
    position: "absolute",
    right: 10,
  },
});

export default Navigation;
