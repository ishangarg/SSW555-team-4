import type { Config } from "@jest/types";

// We can use `Partial` to make options like `maxWorkers` and `rootDir` optional
const config: Partial<Config.InitialOptions> = {
  preset: "jest-expo",
  setupFilesAfterEnv: ["@testing-library/jest-native/extend-expect"],
  transformIgnorePatterns: [
    "node_modules/(?!react-native|@react-native|expo|@expo|@unimodules)",
  ],
  testPathIgnorePatterns: ["/node_modules/", "/android/", "/ios/"],
  rootDir: ".", // Set the root directory for tests
};

export default config;
