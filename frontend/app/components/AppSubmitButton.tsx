// SubmitButton.tsx
import React from "react";
import { useFormContext } from "react-hook-form";
import AppButton from "./AppButton";

interface Props {
  title: string;
  onSubmit: (data: any) => any;
}

const SubmitButton = ({ title, onSubmit }: Props) => {
  const { handleSubmit } = useFormContext();

  // Method to implement the submit function using react-hook-form's handleSubmit and the prop method
  const handlePress = handleSubmit((data) => {
    onSubmit(data);
  });

  return <AppButton title={title} onPress={handlePress} />;
};

export default SubmitButton;
