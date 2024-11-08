import React from "react";
import { View, StyleSheet, Text } from "react-native";
import { TouchableWithoutFeedback } from "react-native-gesture-handler";

import { contacts } from "../tests/testingData";
import Screen from "../components/Screen";
import defaultStyles from "../config/styles";

const ContactsScreen = () => {
  const handleEmergency = () => {
    console.log("Emergency Clicked");
  };

  const handleAddContact = () => {
    console.log("Add Contact Clicked");
  };
  return (
    <Screen style={styles.container}>
      <View>
        <Text style={[styles.header, { textAlign: "center" }]}>
          Emergency Contacts
        </Text>
        <TouchableWithoutFeedback
          style={styles.emergency}
          onPress={handleEmergency}
        >
          <Text style={[styles.emergencyText, styles.text]}>
            Contact Emergency Services
          </Text>
        </TouchableWithoutFeedback>
      </View>

      <View style={styles.contactContainer}>
        <View>
          {contacts.map((contact, index) => (
            <View key={index} style={styles.contactCard}>
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
              Add a Contact
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
  contactCard: {
    backgroundColor: colors.off_white,
    padding: 20,
    borderRadius: "20%",
    marginBottom: 20,
  },
  contactContainer: {
    flex: 1,
    justifyContent: "space-between",
  },
  container: {
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
