import React from "react";
import { GestureHandlerRootView } from "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import { RootStackParamList } from "./app/config/navigation";

import HomeScreen from "./app/screens/HomeScreen";
import AddContactScreen from "./app/screens/AddContactScreen";
import ContactsScreen from "./app/screens/ContactsScreen";
import Navigation from "./app/components/Navigation";
import SettingsScreen from "./app/screens/SettingsScreen";

// Defines any parameters that these components need to render

const Stack = createStackNavigator<RootStackParamList>();

export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName="Home"
          screenOptions={{
            headerShown: false, // Removes a header containing the screen name
          }}
        >
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="AddContact" component={AddContactScreen} />
          <Stack.Screen name="Contacts" component={ContactsScreen} />
          <Stack.Screen name="Settings" component={SettingsScreen} />
        </Stack.Navigator>
        <Navigation />
      </NavigationContainer>
    </GestureHandlerRootView>
  );
}
