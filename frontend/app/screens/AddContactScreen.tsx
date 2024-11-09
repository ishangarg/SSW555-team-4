import React from "react";
import { StyleSheet, View } from "react-native";
import { zodResolver } from "@hookform/resolvers/zod";
import { FormProvider, useForm } from "react-hook-form";
import axios from "axios";

import Screen from "../components/Screen";
import AppFormField from "../components/AppFormField";
import { addContactSchema, ContactFormData } from "../schemas/ContactSchema";
import SubmitButton from "../components/AppSubmitButton";
import { useNavigation } from "@react-navigation/native";
import { NavigationProp } from "../config/navigation";
import { contacts } from "../tests/testingData";

const AddContactScreen = () => {
  const navigation = useNavigation<NavigationProp>();

  const methods = useForm<ContactFormData>({
    resolver: zodResolver(addContactSchema),
    defaultValues: {
      name: "",
      number: "",
    },
  });

  const onSubmit = async (data: ContactFormData) => {
    contacts.push({ contact_name: data.name, phone_number: data.number });
    // try {
    //   console.log("test",data);
    //   let postObj = {
    //     user_id: "testerEmail1@gmail.com",
    //     contacts: [{
    //       contact_name: data.name,
    //       phone_number: data.number
    //     }]
    //   }
    //   const response = await axios.post('http://10.0.2.2:5000/emergencyContacts', postObj);
    //   console.log(response.data);
    // } catch (error) {
    //   console.error(error);
    // }
    navigation.replace("Contacts");
  };

  return (
    <FormProvider {...methods}>
      <Screen style={styles.container}>
        <View>
          <AppFormField
            name="name"
            placeholder="Contact's Name"
            icon="account-outline"
          />
          <AppFormField
            name="number"
            placeholder="Contact's Number"
            icon="phone"
            keyboardType="phone-pad"
          />
        </View>
        <View style={styles.btnContainer}>
          <SubmitButton title="Add Contact" onSubmit={onSubmit} />
        </View>
      </Screen>
    </FormProvider>
  );
};

const styles = StyleSheet.create({
  btnContainer: {
    marginBottom: 20,
  },
  container: {
    padding: 50,
    justifyContent: "space-between",
  },
});

export default AddContactScreen;
