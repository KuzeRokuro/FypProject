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

    h1 {
      font-family: 'Roboto', sans-serif;
      text-align: center; /* Center align the heading */
      font-size: 2.5rem; /* Increase the font size */
      font-weight: bold; /* Make the text bold */
      margin-top: 30px; /* Add spacing above the heading */
      margin-bottom: 10px; /* Add spacing below the heading */
      color: #303031; /* Set a dark, clean color */
    }

    p {
      text-align: center;
      font-size: 1.2rem; /* Adjust font size slightly for better readability */
      color: #555; /* Use a softer color for the paragraph */
      margin-bottom: 30px; /* Add spacing below the paragraph */
    }

    table {
      width: 100%;
      max-width: 800px;
      margin: 20px auto;
      border-collapse: collapse;
      font-family: 'Roboto', sans-serif;
      background-color: #fff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    th, td {
      padding: 12px 15px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    
    th {
      background-color: #303031;
      color: #fff;
      text-transform: uppercase;
      font-weight: bold;
      letter-spacing: 0.5px;
    }
    
    td {
      color: #333;

    }

    tr:nth-child(even) {
      background-color: #f9f9f9;

    }

    tr:hover {
      background-color: #f1f1f1;
      cursor: pointer;
    }

  </style>
  