import React from "react";
import { View, StyleSheet, Text } from "react-native";
import { TouchableWithoutFeedback } from "react-native-gesture-handler";
import { MaterialCommunityIcons, MaterialIcons } from "@expo/vector-icons";

import { contacts } from "../tests/testingData";
import Screen from "../components/Screen";
import defaultStyles from "../config/styles";
import { useNavigation } from "@react-navigation/native";
import { NavigationProp } from "../config/navigation";
import AppButton from "../components/AppButton";

const ContactsScreen = () => {
  const navigation = useNavigation<NavigationProp>();

  const handleEmergency = () => {
    console.log("Emergency Clicked");
  };

  const handleAddContact = () => {
    navigation.replace("AddContact");
  };

  const handleCall = (contact: {
    contact_name: string;
    phone_number: string;
  }): void => {
    console.log(contact.contact_name, contact.phone_number);
  };

  return (
    <Screen style={styles.screen}>
      <View>
        <Text style={[styles.header, { textAlign: "center" }]}>
          Emergency Contacts
        </Text>
        <AppButton
          onPress={handleEmergency}
          title="Emergency Services"
          color="red"
          style={{ marginVertical: 50 }}
        />
      </View>

      <View style={styles.container}>
        <View>
          {contacts.map((contact, index) => (
            <View key={index} style={styles.contact}>
              <View>
                <Text style={[styles.text, { marginBottom: 10 }]}>
                  {contact.contact_name}
                </Text>
                <Text style={styles.text}>
                  {contact.phone_number.slice(0, 3) +
                    "-" +
                    contact.phone_number.slice(3, 6) +
                    "-" +
                    contact.phone_number.slice(6)}
                </Text>
              </View>
              <TouchableWithoutFeedback
                style={styles.callContainer}
                onPress={() => handleCall(contact)}
              >
                <MaterialCommunityIcons
                  color={colors.primary}
                  size={40}
                  name="phone"
                />
              </TouchableWithoutFeedback>
            </View>
          ))}
        </View>

        {contacts.length < 3 && (
          <AppButton
            onPress={handleAddContact}
            title="Add Contacts"
            style={{ marginBottom: 20 }}
          />
        )}
      </View>
    </Screen>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  callContainer: {
    borderColor: colors.accent,
    padding: 10,
    borderRadius: 25,
    borderWidth: 5,
  },

  contact: {
    backgroundColor: colors.off_white,
    padding: 20,
    borderRadius: "20%",
    marginBottom: 20,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  container: {
    flex: 1,
    justifyContent: "space-between",
  },
  screen: {
    padding: 50,
    justifyContent: "space-between",
  },

  header: {
    fontSize: text.fontSize,
    fontWeight: text.fontWeight,
  },
  text: {
    fontSize: subText.fontSize,
    fontWeight: subText.fontWeight,
  },
});
export default ContactsScreen;
