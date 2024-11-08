import { GestureHandlerRootView } from "react-native-gesture-handler";
import HomeScreen from "./app/screens/HomeScreen";
import AddContactScreen from "./app/screens/AddContactScreen";
import ContactsScreen from "./app/screens/ContactsScreen";

export default function App() {
  return (
    <GestureHandlerRootView>
      <ContactsScreen />
    </GestureHandlerRootView>
  );
}
