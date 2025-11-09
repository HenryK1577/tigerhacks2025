import { useState } from "react";

export default function Project() {
  const [inputValue, setInputValue] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevents a reload
    setResponse(null);

    const query = inputValue && inputValue.trim();
    if (!query) {
      setResponse("Please enter a search term.");
      return;
    }

    setLoading(true);
    try {
      // Send the encoded inputValue to Flask as a query parameter
      const url = `http://localhost:5000/api/planet-data?query=${encodeURIComponent(
        query,
      )}`;
      const res = await fetch(url);

      if (!res.ok) {
        // Backend returned an error status
        const text = await res.text().catch(() => null);
        throw new Error(
          `Backend error: ${res.status} ${res.statusText}${text ? ` - ${text}` : ""}`,
        );
      }

      const data = await res.json().catch(() => null);
      if (data && typeof data === "object") {
        setResponse(data);
      } else if (data) {
        setResponse({ message: String(data) });
      } else {
        setResponse({ message: "No data found for this query." });
      }
    } catch (error) {
      console.error(error);
      setResponse(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  function renderValue(value) {
    if (value === null || value === undefined) return "-";
    if (typeof value === "object") return (
      <pre style={{ whiteSpace: "pre-wrap", margin: 0 }}>{JSON.stringify(value, null, 2)}</pre>
    );
    return String(value);
  }

  return (
    <div style={{ textAlign: "left" }}>
      {/* Submit form */}
      <form onSubmit={handleSubmit} style={{ margin: "30px" }}>
        <input
          style={{
            padding: "10px",
            fontSize: "20px",
            borderRadius: "8px",
            border: "1px solid #ccc",
            width: "380px",
            marginRight: "12px",
          }}
          type="text"
          placeholder="Celestial Body..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button
          type="submit"
          style={{ padding: "10px 16px", fontSize: "18px", borderRadius: "8px" }}
          disabled={loading}
        >
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

    
    <div style={{ display: "flex", alignItems: "flex-start", gap: "30px", margin: "30px" }}>

      {/* Image from scrapper */}
      <div style={{ margin: "30px" }}>
        <img src="/LPOS.png" alt="Planet" width="450" height="450" />
      </div>

      {/* Response area */}
      <div style={{ margin: "30px", maxWidth: "900px" }}>
        {loading && <div>Loading…</div>}

        {/* string responses (errors or simple messages) */}
        {response && typeof response === "string" && (
          <div style={{ color: "#b22222", fontWeight: 600 }}>{response}</div>
        )}

        {/* object or array responses */}
        {response && typeof response === "object" && (
          Array.isArray(response) ? (
            <div>
              {response.map((item, idx) => (
                <div key={idx} style={{ marginBottom: "12px", padding: "12px", border: "1px solid #eee", borderRadius: "6px" }}>
                  {renderValue(item)}
                </div>
              ))}
            </div>
          ) : (
            <div style={{ padding: "12px", border: "1px solid #eee", borderRadius: "6px" }}>
              {Object.entries(response).map(([key, value]) => (
                <div
                  key={key}
                  style={{ display: "flex", justifyContent: "space-between", marginBottom: "8px", gap: "12px" }}
                >
                  <div style={{ fontWeight: "bold", minWidth: "140px" }}>{key}:</div>
                  <div style={{ flex: 1 }}>{renderValue(value)}</div>
                </div>
              ))}
            </div>
          )
        )}
      </div>
    </div>
  </div>
  );
}
