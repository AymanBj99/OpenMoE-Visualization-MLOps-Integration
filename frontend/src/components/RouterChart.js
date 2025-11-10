import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

const RouterChart = ({ data }) => {
  const chartData = data.slice(0, 20); // éviter surcharge

  return (
    <div style={{ width: "90%", margin: "auto" }}>
      <h2>📈 Distribution des probabilités</h2>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="expert_index" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="probability" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default RouterChart;
