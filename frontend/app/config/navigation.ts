import { StackNavigationProp } from "@react-navigation/stack";

export type RootStackParamList = {
  Home: undefined;
  AddContact: undefined;
  Contacts: undefined;
};

export type NavigationProp = StackNavigationProp<RootStackParamList>;
