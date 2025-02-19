# Bracket Matcher (React Component)

A simple React app that checks if a string of brackets is valid in real-time. This project demonstrates front-end integration for the "Valid Parentheses" problem.

## Overview

- **Core Logic**: Uses a stack-based approach to validate bracket strings (similar to the Python solution).
- **Live Feedback**: Displays "Valid" or "Invalid" as you type.

## File Structure

```
bracket-matcher/
├── package.json
├── webpack.config.js       # If you're using a custom Webpack setup
├── src/
│   ├── App.js             # Main React component
│   ├── App.test.js        # Optional Jest tests for bracket validation
│   └── index.js           # App entry point
└── README.md
```

## How to Run Locally

1. **Install Dependencies**:
   ```bash
   npm install
   ```
2. **Start the Dev Server**:
   ```bash
   npm start
   ```
3. **Open Your Browser**:
   - Go to `http://localhost:3000` (by default) to view the app.

## Testing

- **Run Tests**:
  ```bash
  npm test
  ```
  This uses Jest to run `App.test.js`.

## Next Steps

- **Expand UI**: Add color indicators or animations for valid/invalid states.
- **Refactor**: If needed, move the bracket validation logic into a shared library to keep code DRY across front-end and back-end.
- **Integration**: Potentially connect to a backend or serverless function that uses the Python solution for consistency in large-scale applications.