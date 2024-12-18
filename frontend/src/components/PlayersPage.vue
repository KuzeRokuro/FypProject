<template>
    <div>
      <h1>Player Page</h1>
      <p>This is the Player page where you can view and manage player data.</p>
  
      <!-- Table to display player data -->
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Phone Number</th>
            <th>Total Win</th>
            <th>Total Match</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="player in players" :key="player.id">
            <td>{{ player.id }}</td>
            <td>{{ player.name }}</td>
            <td>0{{ player.phone }}</td>
            <td>{{ player.totalwins }}</td>
            <td>{{ player.totalmatch }}</td>
          </tr>
        </tbody>
      </table>
  
      <!-- Error message -->
      <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "PlayersPage",
    data() {
      return {
        players: [], // To store player data
        error: null, // To store error messages
      };
    },
    mounted() {
      this.fetchPlayers(); // Fetch data when the component is mounted
    },
    methods: {
      async fetchPlayers() {
        try {
          const response = await axios.get("http://localhost:8000/Records/Player/"); // Replace with your API URL
          this.players = response.data; // Assign the fetched data to 'players'
        } catch (err) {
          this.error = "Failed to fetch player data. Please try again later.";
          console.error(err);
        }
      },
    },
  };
  </script>
  
  <style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  th {
    background-color: #f4f4f4;
  }
  
  p {
    margin-top: 20px;
  }
  </style>
  