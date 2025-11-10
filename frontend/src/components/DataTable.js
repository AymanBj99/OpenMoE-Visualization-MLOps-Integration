import React from "react";
import DataTable from "react-data-table-component";

const RouterDataTable = ({ data }) => {
  const columns = [
    { name: "Layer", selector: row => row.layer_name, sortable: true },
    { name: "Token", selector: row => row.token_index },
    { name: "Expert", selector: row => row.expert_index },
    { name: "Logit", selector: row => row.logit },
    { name: "Probability", selector: row => row.probability },
  ];

  return (
    <div style={{ margin: "20px" }}>
      <h2>📊 Router Outputs</h2>
      <DataTable columns={columns} data={data} pagination />
    </div>
  );
};

export default RouterDataTable;
