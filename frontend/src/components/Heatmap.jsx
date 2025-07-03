import "../css/Heatmap.css";

function Heatmap({ data }) {
  // Convert object to array and sort by date
  const sortedEntries = Object.entries(data).sort(([a], [b]) => a.localeCompare(b));

  // Helper: determine color class by count
  const getColor = (count) => {
    if (count >= 5) return "level-4";
    if (count >= 3) return "level-3";
    if (count >= 1) return "level-2";
    return "level-1";
  };

  return (
    <div className="heatmap">
      {sortedEntries.map(([date, count]) => (
        <div key={date} className={`cell ${getColor(count)}`} title={`${date}: ${count} commits`} />
      ))}
    </div>
  );
}

export default Heatmap;