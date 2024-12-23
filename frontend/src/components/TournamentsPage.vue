<template>
    <div>
      <h1>Tournament Page</h1>
      <button @click="navigateToAddTournament" class="add-tournament-button">Create Tournament</button>
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
      navigateToAddTournament() {
        // Navigate to the Tournament page
        this.$router.push("/addtournament");
      },
    },
    created() {
      this.fetchTournaments(); // Fetch tournament data when the component is created
    },
  };
  </script>
  
  <style scoped>
      table {
        width: 80%;
        max-width: 800px;
        margin: 20px auto;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
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
      .error {
        color: red;
        margin-top: 10px;
      }
  </style>
  