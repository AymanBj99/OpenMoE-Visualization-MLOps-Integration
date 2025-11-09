import React, { useEffect, useState } from "react";
import axios from "axios";
import DataTable from "react-data-table-component";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [data, setData] = useState([]);

  // Charger le CSV
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/router_analysis.csv") // 👉 Adapter selon ton backend
      .then((response) => {
        const rows = response.data
          .split("\n")
          .slice(1)
          .map((row) => {
            const cols = row.split(",");
            return {
              layer_name: cols[0],
              token_index: Number(cols[1]),
              expert_index: Number(cols[2]),
              logit: parseFloat(cols[3]),
              probability: parseFloat(cols[4]),
            };
          });
        setData(rows);
      })
      .catch((err) => console.error("Erreur chargement CSV:", err));
  }, []);

  const columns = [
    { name: "Layer", selector: (row) => row.layer_name, sortable: true },
    { name: "Token", selector: (row) => row.token_index },
    { name: "Expert", selector: (row) => row.expert_index },
    { name: "Logit", selector: (row) => row.logit.toFixed(3) },
    { name: "Probability", selector: (row) => row.probability.toFixed(3) },
  ];

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">📊 Router Analysis Dashboard</h2>

      <div className="card p-3 mb-4 shadow">
        <h5>Distribution des probabilités</h5>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data.slice(0, 50)}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="token_index" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="probability" stroke="#007bff" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="card p-3 shadow">
        <h5>Détails des activations</h5>
        <DataTable
          columns={columns}
          data={data}
          pagination
          highlightOnHover
          striped
        />
      </div>
    </div>
  );
}

export default App;
