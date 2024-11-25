import React from "react";
import Screen from "../components/Screen";
import { Text, StyleSheet, View } from "react-native";
import defaultStyles from "../config/styles";
import { ScrollView } from "react-native-gesture-handler";
import { logs } from "../tests/testingData";

const AnalyticsScreen = () => {
  const calculateScore = (): number => {
    if (logs.length === 0) return 0;
    let sum = 0;
    logs.map((element) => (sum += element.score));

    const average = sum / logs.length;
    return Number(average.toFixed(1));
  };

  return (
    <Screen style={styles.screen}>
      <Text style={[styles.header, { textAlign: "center" }]}>
        Wellness Tracking
      </Text>
      <View style={styles.average}>
        <View style={styles.scoreContainer}>
          <Text style={styles.averageScore}>{calculateScore()}</Text>
        </View>
      </View>
      <Text style={[styles.header, { textAlign: "center" }]}>History</Text>
      <ScrollView style={{ paddingHorizontal: 15, marginBottom: 20 }}>
        <View style={styles.log}>
          <Text style={styles.logText}>Day</Text>
          <Text style={styles.logText}>Score</Text>
        </View>
        {logs.map((element, index) => (
          <View key={index} style={styles.log}>
            <Text style={{ fontSize: text.fontSize }}>{element.date}</Text>
            <Text style={{ fontSize: text.fontSize }}>{element.score}</Text>
          </View>
        ))}
      </ScrollView>
    </Screen>
  );
};

const { colors, text, subText } = defaultStyles;

const styles = StyleSheet.create({
  average: {
    flexDirection: "row",
    justifyContent: "center",
    marginBottom: 40,
  },
  averageScore: {
    fontSize: 128,
    textAlign: "center",
    fontWeight: "700",
    color: colors.secondary,
  },
  header: {
    fontSize: text.fontSize,
    fontWeight: text.fontWeight,
    marginBottom: 20,
  },
  log: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 10,
  },
  logText: {
    fontSize: text.fontSize,
    color: colors.primary,
    fontWeight: subText.fontWeight,
  },
  scoreContainer: {
    borderColor: colors.primary,
    borderWidth: 20,
    height: 250,
    width: 250,
    borderRadius: 200,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  screen: {
    padding: 50,
  },
});

export default AnalyticsScreen;
