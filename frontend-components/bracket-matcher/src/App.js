import React, { useState } from "react";

export function isValidBracketString(str) {
  // This is the same logic as our Python solution, but in JavaScript.
  const mapping = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  const stack = [];

  for (let char of str) {
    if (mapping[char]) {
      // char is a closing bracket
      if (stack.length === 0 || stack[stack.length - 1] !== mapping[char]) {
        return false;
      }
      stack.pop();
    } else {
      // char is an opening bracket
      if (char === "(" || char === "[" || char === "{") {
        stack.push(char);
      } else {
        // if user types something else, ignore or handle it as invalid
        return false;
      }
    }
  }

  return stack.length === 0;
}

export default function App() {
  const [input, setInput] = useState("");
  const [isValid, setIsValid] = useState(null);

  function handleChange(e) {
    const newVal = e.target.value;
    setInput(newVal);
    setIsValid(isValidBracketString(newVal));
  }

  return (
    <div style={{ margin: "2rem" }}>
      <h1>Bracket Matcher</h1>
      <input
        type="text"
        placeholder="Type bracket string..."
        value={input}
        onChange={handleChange}
        style={{ width: "300px", padding: "0.5rem" }}
      />
      {isValid !== null && (
        <div style={{ marginTop: "1rem", fontWeight: "bold" }}>
          {isValid ? "Valid" : "Invalid"}
        </div>
      )}
    </div>
  );
}
