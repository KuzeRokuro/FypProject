<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <div>
    <h1>Player Page</h1>
    <div class="search-bar">
      <input type="text" v-model="searchTerm" placeholder="Search Player..." />
    </div>
    <button @click="navigateToAddPlayer" class="add-player-button">Add Player</button>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Phone Number</th>
          <th>Total Win</th>
          <th>Total Match</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in filteredPlayers" :key="player.id">
          <td>{{ player.id }}</td>
          <td>{{ player.name }}</td>
          <td>0{{ player.phone }}</td>
          <td>{{ player.totalwins }}</td>
          <td>{{ player.totalmatch }}</td>
          <td>
            <button class="btn-action" @click="editPlayer(player.id)">
              Edit
            </button>
          </td>
        </tr>
      </tbody>
    </table>

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
      searchTerm: "", // To store the search term
    };
  },
  mounted() {
    this.fetchPlayers(); // Fetch data when the component is mounted
  },
  computed: {
    filteredPlayers() {
      return this.players.filter((player) =>
        player.name.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
  },
  methods: {
    async fetchPlayers() {
      try {
        const response = await axios.get("https://kuzerokuro.pythonanywhere.com/Records/Player/?format=json"); // Replace with your API URL
        this.players = response.data; // Assign the fetched data to 'players'
      } catch (err) {
        this.error = "Failed to fetch player data. Please try again later.";
        console.error(err);
      }
    },
    navigateToAddPlayer() {
      // Navigate to the Player page
      this.$router.push("/addplayer");
    },
    editPlayer(playerId) {
      // Navigate to an edit page
      this.$router.push(`/edit-player/${playerId}`);
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

  th,
  td {
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

  .add-player-button {
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
    background-color: #ffc107;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 55%;

  }

  .btn-action:hover {
    background-color: rgb(252, 127, 44);

  }

  .search-bar {
    text-align: center;
  }

  .search-bar input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 300px;
  }
  @media (max-width: 768px) {
  table {
    display: block;
    overflow-x: auto;
    width: 100%;
    border: none; /* Remove borders for a cleaner look */
  }}
</style>