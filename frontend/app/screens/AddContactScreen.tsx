import React from "react";
import { StyleSheet, View } from "react-native";
import { zodResolver } from "@hookform/resolvers/zod";
import { FormProvider, useForm } from "react-hook-form";
import axios from "axios";

import Screen from "../components/Screen";
import AppFormField from "../components/AppFormField";
import { addContactSchema, ContactFormData } from "../schemas/ContactSchema";
import SubmitButton from "../components/AppSubmitButton";

const AddContactScreen = () => {
  const methods = useForm<ContactFormData>({
    resolver: zodResolver(addContactSchema),
    defaultValues: {
      name: "",
      number: "",
    },
  });

  const onSubmit = async (data: ContactFormData) => {
    const postingData = { userID: "", data };

    try {
      console.log(data);
      const response = await axios.post(
        "https://localhost:5000/add",
        postingData
      );
      console.log(response.data);
    } catch (error) {
      console.error("Error Posting data:", error);
    }
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
        <View>
          <SubmitButton title="Add Contact" onSubmit={onSubmit} />
        </View>
      </Screen>
    </FormProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 50,
    justifyContent: "space-between",
  },
});

export default AddContactScreen;
