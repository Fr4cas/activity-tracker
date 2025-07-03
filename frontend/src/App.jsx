import { useEffect, useState } from "react";
import Heatmap from "./components/Heatmap";

function App() {
  const [commitData, setCommitData] = useState({});

  useEffect(() => {
    fetch("/data.json")
      .then((res) => res.json())
      .then((data) => {
        setCommitData(data);
      })
      .catch((err) => {
        console.error("Failed to load commit data:", err);
      });
  }, []);

  return (
    <div>
      <h1>GitHub Activity Tracker</h1>
      <p>This app displays commit activity by date.</p>

      <Heatmap data={commitData} />
    </div>
  );
}

export default App;