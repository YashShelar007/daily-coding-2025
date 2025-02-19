import { isValidBracketString } from "./App"; // We'll slightly refactor so we can export the function alone

// If you'd like to test the internal function, you can export it separately in App.js:
//
// export function isValidBracketString(str) { ... }
// export default function App() { ... }

describe("isValidBracketString", () => {
  it("should return true for ()", () => {
    expect(isValidBracketString("()")).toBe(true);
  });

  it("should return true for ()[]{}", () => {
    expect(isValidBracketString("()[]{}")).toBe(true);
  });

  it("should return false for (]", () => {
    expect(isValidBracketString("(]")).toBe(false);
  });

  it("should return true for {[]}", () => {
    expect(isValidBracketString("{[]}")).toBe(true);
  });

  it("should return false for (abc)", () => {
    expect(isValidBracketString("(abc)")).toBe(false);
  });
});
