import { useState } from "react";

export default function Project() {
  const [inputValue, setInputValue] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    try {
      // Send the inputValue to Flask as a query parameter
      const res = await fetch(`http://localhost:5000/api/project-data?query=${inputValue}`);
      const data = await res.json();
      setResponse(data.message);
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to Flask backend.");
    }
  };

  return (
    <div style={{ textAlign: "center" }}>
      {/* Image of SPACE */}
      <img src="/public/LPOS.png" alt="My Image" style={{ width: "100%", height: "auto" }} />

      {/* Text field */}
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Distance to..."
        style={{ fontSize: "16px" }}
      />

      {/* Button to submit */}
      <button
        onClick={handleSubmit}
        style={{ marginLeft: "10px", padding: "8px 16px" }}
      >
        Send
      </button>

      {/* Show response */}
      {response && (
        <p style={{ marginTop: "20px", fontSize: "18px", color: "green" }}>
          {response}
        </p>
      )}
    </div>
  );
}
