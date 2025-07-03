import { useEffect, useState } from "react";

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

      <h2>Commits per Day:</h2>
      <ul>
        {Object.entries(commitData).map(([date, count]) => (
          <li key={date}>
            {date}: {count} commits
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;