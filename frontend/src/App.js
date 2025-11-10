import React, { useEffect, useState } from "react";
import axios from "axios";
import Papa from "papaparse";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, Legend, PieChart, Pie, Cell } from "recharts";
import DataTable from "react-data-table-component";

const API_BASE_URL = "http://127.0.0.1:5500"; // ton backend Flask

function App() {
  const [data, setData] = useState([]);
  const [expertStats, setExpertStats] = useState([]);

  useEffect(() => {
    const fetchCSV = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/router_analysis.csv`);
        const parsedData = Papa.parse(response.data, { header: true }).data;
        setData(parsedData);

        // Agrégation : moyenne des probabilités par expert
        const grouped = {};
        parsedData.forEach(row => {
          const expert = row.expert_index;
          const prob = parseFloat(row.probability || 0);
          if (!grouped[expert]) grouped[expert] = { expert, sum: 0, count: 0 };
          grouped[expert].sum += prob;
          grouped[expert].count += 1;
        });

        const stats = Object.values(grouped).map(e => ({
          expert: e.expert,
          avgProbability: e.count > 0 ? e.sum / e.count : 0
        }));

        setExpertStats(stats);
      } catch (error) {
        console.error("Erreur lors du chargement du CSV :", error);
      }
    };

    fetchCSV();
  }, []);

  const COLORS = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc948", "#b07aa1", "#ff9da7"];

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>📊 Distribution des probabilités</h2>

      <div style={{ display: "flex", justifyContent: "space-around", flexWrap: "wrap" }}>
        {/* Bar Chart des probabilités globales */}
        <div style={{ marginTop: "20px" }}>
          <BarChart width={600} height={300} data={data.slice(0, 20)}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="expert_index" />
            <YAxis domain={[0, 1]} />
            <Tooltip />
            <Legend />
            <Bar dataKey="probability" fill="#8884d8" />
          </BarChart>
        </div>

        {/* Nouveau : graphique des experts dominants */}
        <div style={{ marginTop: "20px" }}>
          <h3>🔥 Experts dominants (moyenne des probabilités)</h3>
          <PieChart width={400} height={300}>
            <Pie
              data={expertStats}
              dataKey="avgProbability"
              nameKey="expert"
              cx="50%"
              cy="50%"
              outerRadius={100}
              label
            >
              {expertStats.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </div>
      </div>

      <h3 style={{ marginTop: "40px" }}>📈 Router Outputs</h3>
      <DataTable
        columns={[
          { name: "Layer", selector: row => row.layer_name, sortable: true },
          { name: "Token", selector: row => row.token_index, sortable: true },
          { name: "Expert", selector: row => row.expert_index, sortable: true },
          { name: "Logit", selector: row => row.logit, sortable: true },
          { name: "Probability", selector: row => row.probability, sortable: true }
        ]}
        data={data.slice(0, 50)}
        pagination
        highlightOnHover
      />
    </div>
  );
}

export default App;
