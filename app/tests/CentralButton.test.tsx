import React from "react";
import { render, fireEvent } from "@testing-library/react-native";
import CentralButton from "../components/CentralButton"; // Adjust the path as necessary

test("renders CentralButton correctly", () => {
  const { getByTestId } = render(<CentralButton onPress={() => {}} />);

  expect(getByTestId("big-button")).toBeTruthy();
  expect(getByTestId("small-button")).toBeTruthy();
});

test("calls onPress when the button is pressed", () => {
  const mockOnPress = jest.fn();
  const { getByTestId } = render(<CentralButton onPress={mockOnPress} />);

  fireEvent.press(getByTestId("big-button"));
  expect(mockOnPress).toHaveBeenCalled();
});
