module.exports = {
  testMatch: ["**/tests/unit/**/*.spec.[jt]s?(x)"],
  transform: {
    "^.+\\.vue$": "vue-jest",
    "^.+\\.[jt]sx?$": "babel-jest",
  },
  moduleFileExtensions: ["js", "jsx", "json", "vue"],
  testEnvironment: "jsdom",
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1",
  },
};
