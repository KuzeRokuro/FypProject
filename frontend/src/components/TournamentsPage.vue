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
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="tournament in tournaments" :key="tournament.id">
            <td>{{ tournament.id }}</td>
            <td>{{ tournament.t_name }}</td>
            <td>{{ tournament.date }}</td>
            <td>{{ tournament.cardgame }}</td>
            <td>
              <button class="btn-action" @click="editTournament(tournament.id)">
                Edit
              </button>
              <button class="btn-action" @click="startTournament(tournament.id)">
                Start
              </button>
              <button class="btn-action" @click="rankTournament(tournament.id)">
                See Ranking
              </button>
            </td>
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
          .get("https://kuzerokuro.pythonanywhere.com/Records/Tournament/?format=json") // Replace with your actual API URL
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
      editTournament(tournamentId) {
        // Navigate to an edit page
        this.$router.push(`/edit-tournament/${tournamentId}`);
      },
      startTournament(tournamentId) {
        // Navigate to an edit page
        this.$router.push(`/start-tournament/${tournamentId}`);
      },
      rankTournament(tournamentId) {
        // Navigate to an rank page
        this.$router.push(`/rank-tournament/${tournamentId}`);
      }
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

      .add-tournament-button {
        display: block; /* Make the button behave like a block element */
        margin: 20px auto; /* Center the button horizontally and add spacing */
        padding: 10px 20px; /* Add padding for better appearance */
        background-color: #303031; /* Button background color */
        color: #fff; /* Button text color */
        font-size: 1rem; /* Font size */
        border: none; /* Remove borders */
        border-radius: 5px; /* Round the button corners */
        cursor: pointer; /* Change cursor on hover */
      }

      .add-player-button:hover {
        background-color: #444; /* Slightly lighten background on hover */
      }

      .btn-action {
        
        padding: 10px 10px;
        font-size: 0.9rem;
        background-color: #ffc107 ;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 55%;
        margin-bottom:3px;

        }

       .btn-action:hover {
          background-color:rgb(252, 127, 44);

       }
      

  </style>
  