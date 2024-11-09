import React from "react";
import { View, StyleSheet, Text } from "react-native";
import { TouchableWithoutFeedback } from "react-native-gesture-handler";

import { contacts } from "../tests/testingData";
import Screen from "../components/Screen";
import defaultStyles from "../config/styles";
import { useNavigation } from "@react-navigation/native";
import { NavigationProp } from "../config/navigation";

const ContactsScreen = () => {
  const navigation = useNavigation<NavigationProp>();

  const handleEmergency = () => {
    console.log("Emergency Clicked");
  };

  const handleAddContact = () => {
    navigation.replace("AddContact");
  };
  return (
    <Screen style={styles.screen}>
      <View>
        <Text style={[styles.header, { textAlign: "center" }]}>
          Emergency Contacts
        </Text>
        <TouchableWithoutFeedback
          style={styles.emergency}
          onPress={handleEmergency}
        >
          <Text style={[styles.emergencyText, styles.text]}>
            EMERGENCY SERVICES
          </Text>
        </TouchableWithoutFeedback>
      </View>

      <View style={styles.container}>
        <View>
          {contacts.map((contact, index) => (
            <View key={index} style={styles.contact}>
              <Text style={[styles.text, { marginBottom: 10 }]}>
                {contact.contact_name}
              </Text>
              <Text style={styles.text}>{contact.phone_number}</Text>
            </View>
          ))}
        </View>

        {contacts.length < 3 && (
          <TouchableWithoutFeedback
            style={styles.addButton}
            onPress={handleAddContact}
          >
            <Text
              style={[
                styles.text,
                { textAlign: "center", color: colors.white },
              ]}
            >
              ADD CONTACT
            </Text>
          </TouchableWithoutFeedback>
        )}
      </View>
    </Screen>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  addButton: {
    backgroundColor: colors.primary,
    padding: 20,
    borderRadius: "20%",
    marginBottom: 20,
  },
  contact: {
    backgroundColor: colors.off_white,
    padding: 20,
    borderRadius: "20%",
    marginBottom: 20,
  },
  container: {
    flex: 1,
    justifyContent: "space-between",
  },
  screen: {
    padding: 50,
    justifyContent: "space-between",
  },
  emergency: {
    backgroundColor: "#E3242B",
    padding: 20,
    borderRadius: "20%",
    marginVertical: 50,
  },
  emergencyText: {
    color: colors.white,
    textAlign: "center",
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
