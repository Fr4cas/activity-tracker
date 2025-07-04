import "../css/Heatmap.css";

function Heatmap({ data }) {
  const today = new Date();
  const daysToShow = 90;
  const startDate = new Date(today);
  startDate.setDate(today.getDate() - daysToShow);

  const allDates = []
  const current = new Date(startDate);

  while (current <= today) {
    const dateStr = current.toISOString().slice(0, 10);
    allDates.push(dateStr);
    current.setDate(current.getDate() + 1);
  }

  const sortedEntries = Object.entries(data).sort(([a], [b]) => a.localeCompare(b));

  const getColor = (count) => {
    if (count >= 5) return "level-4";
    if (count >= 3) return "level-3";
    if (count >= 1) return "level-2";
    return "level-1";
  };

  // sorting into columns by week
  const weeks = [];
  let week = [];

  for (let i = 0; i < allDates.length; i++) {
    const date = allDates[i];
    const dayOfWeek = new Date(date).getDay();

    if (i === 0 && dayOfWeek !== 0) {
      for (let j = 0; j < dayOfWeek; j++) {
        week.push(null);
      }
    }

    week.push(date);

    if (week.length === 7) {
      weeks.push(week);
      week = [];
    }
  }

  if (week.length > 0) {
    weeks.push(week);
  }

  return (
    <div className="heatmap">
      {weeks.map((week, weekIndex) => (
        <div key={weekIndex}>
          {week.map((date, dayIndex) => {
            const count = date && data[date] ? data[date] : 0;

            return (
              <div
                key={dayIndex}
                className={`cell ${getColor(count)}`}
                title={date ? `${date}: ${count} commits` : ""}
              />
            );
          })}
        </div>
      ))}
    </div>
  );
}

export default Heatmap;