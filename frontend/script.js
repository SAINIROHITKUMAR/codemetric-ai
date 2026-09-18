const API_URL = "http://127.0.0.1:5000/api/analyze";

document.getElementById("analyze").addEventListener("click", async () => {
  const code = document.getElementById("code").value;
  const message = document.getElementById("message");
  message.textContent = "Analyzing...";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({code})
    });

    const payload = await response.json();
    if (!response.ok) throw new Error(payload.message || "Analysis failed");

    const data = payload.data;
    document.getElementById("results").classList.remove("hidden");
    document.getElementById("score").textContent = data.quality_score;
    document.getElementById("loc").textContent = data.code.loc;
    document.getElementById("functions").textContent = data.code.functions;
    document.getElementById("classes").textContent = data.code.classes;
    document.getElementById("complexity").textContent = data.complexity.average_complexity;
    document.getElementById("maintainability").textContent = data.maintainability.score;

    const list = document.getElementById("suggestions");
    list.innerHTML = "";
    data.suggestions.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      list.appendChild(li);
    });
    message.textContent = "";
  } catch (error) {
    message.textContent = error.message;
  }
});
