import { GestureHandlerRootView } from "react-native-gesture-handler";
import HomeScreen from "./app/screen/HomeScreen";

export default function App() {
  return (
    <GestureHandlerRootView>
      <HomeScreen />
    </GestureHandlerRootView>
  );
}
