import { GestureHandlerRootView } from "react-native-gesture-handler";
import HomeScreen from "./app/screens/HomeScreen";
import AddContactScreen from "./app/screens/AddContactScreen";

export default function App() {
  return (
    <GestureHandlerRootView>
      <AddContactScreen />
    </GestureHandlerRootView>
  );
}
