<template>
    <div>
      <h1>Tournament Page</h1>
      <p>This is the Tournament page where you can view and manage tournament data.</p>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Date</th>
            <th>Card Game</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tournament in tournaments" :key="tournament.id">
            <td>{{ tournament.id }}</td>
            <td>{{ tournament.t_name }}</td>
            <td>{{ tournament.date }}</td>
            <td>{{ tournament.cardgame }}</td>
          </tr>
        </tbody>
      </table>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "TournamentPage",
    data() {
      return {
        tournaments: [], // Array to store tournament data
        errorMessage: "", // Error message in case the API call fails
      };
    },
    methods: {
      fetchTournaments() {
        axios
          .get("http://127.0.0.1:8000/Records/Tournament/") // Replace with your actual API URL
          .then((response) => {
            this.tournaments = response.data; // Store data in the tournaments array
          })
          .catch((error) => {
            console.error("Error fetching tournament data:", error);
            this.errorMessage = "Failed to fetch tournament data. Please try again later.";
          });
      },
    },
    created() {
      this.fetchTournaments(); // Fetch tournament data when the component is created
    },
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  th {
    background-color: #f4f4f4;
  }
  
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  