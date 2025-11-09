import { useState } from "react";

export default function Project() {
  const [inputValue, setInputValue] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    try {
      e.preventDefault(); // Prevents a reload
      // Send the inputValue to Flask as a query parameter
      const res = await fetch(
        `http://localhost:5000/api/project-data?query=${inputValue}`,
      );
      const data = await res.json();
      if (data && typeof data === "object") {
        setResponse(data);
      } else {
        setResponse({ message: "No data found for this planet." });
      }
    } catch (error) {
      // Ethier there was a connection error in the backend
      // or the entry does not exist
      console.error(error);
      setResponse("Error from Flask backend.");
    }
  };

  return (
    <div style={{ textAlign: "left" }}>
      {/* Submit form */}
      <form onSubmit={handleSubmit}>
        <input
          style={{
            padding: "10px",
            fontSize: "20px",
            borderRadius: "8px",
            border: "1px solid #ccc",
            width: "500px",
            margin: "30px",
          }}
          type="text"
          placeholder="Celestial Body..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
      </form>

      {/* Image from scrapper */}
      <div
        style={{
          margin: "30px",
        }}
      >
        <img src="/LPOS.png" alt="Planet" width="450" height="450" />
      </div>

      {/* JSON response box */}
      {response && (
        <div>
          {Object.entries(response).map(([key, value]) => (
            <div
              key={key}
              style={{
                display: "flex",
                justifyContent: "space-between",
                marginBottom: "8px",
              }}
            >
              <span style={{ fontWeight: "bold" }}>{key}:</span>
              <span>{value}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
