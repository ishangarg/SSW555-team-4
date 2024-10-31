import React from "react";
import { Controller, useFormContext, FieldError, Field } from "react-hook-form";
import { StyleSheet, Text } from "react-native";
import AppInputField from "./AppInputField";

interface Props {
  name: string;
  icon?: string;
  [x: string]: any; // Allow any additional props
}

const AppFormField = ({ name, icon, ...otherProps }: Props) => {
  const {
    control,
    formState: { errors },
  } = useFormContext(); // Access control and errors from context

  return (
    <>
      <Controller
        control={control}
        name={name}
        render={({ field: { onChange, onBlur, value } }) => (
          <AppInputField
            {...otherProps}
            icon={icon}
            onChangeText={onChange}
            onBlur={onBlur}
            value={value}
          />
        )}
      />
      {errors[name] && (
        <Text style={styles.errorText}>
          {(errors[name] as FieldError).message}
        </Text>
      )}
    </>
  );
};

const styles = StyleSheet.create({
  errorText: {
    color: "red",
    fontSize: 14,
    marginBottom: 10,
  },
});

export default AppFormField;
