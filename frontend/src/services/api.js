import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5500"; // ton backend Flask

export const getRouterData = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/router_analysis.csv`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des données :", error);
    throw error;
  }
};
