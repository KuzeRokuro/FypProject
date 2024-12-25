<template>
    <div class="container mt-5">
      <h1>Tournament Rankings</h1>

      <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
      <div v-if="matches.length" class="mt-4">
        <h2>Matches</h2>
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Match ID</th>
              <th>Player 1</th>
              <th>Player 2</th>
              <th>Winner</th>
              <th>Accept</th>
              <th>Round</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in matches" :key="match.id">
              <td>{{ match.id }}</td>
              <td>{{ match.player1 }}</td>
              <td>{{ match.player2 }}</td>
              <td>
                <select 
                  v-model="editableWinners[index]" 
                  class="form-control"
                >
                  <option disabled value="">Select a winner</option>
                  <option :value="match.player1">{{ match.player1 }}</option>
                  <option :value="match.player2">{{ match.player2 }}</option>
                </select>
              </td>
              <td>
                <button 
                  class="btn btn-success" 
                  @click="updateWinner(match.id, editableWinners[index])"
                >
                  Accept
                </button>
              </td>
              <td>{{ match.round }}</td>
            </tr>
          </tbody>
        </table>
  
        <h2 class="mt-5">Player Rankings</h2>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Player</th>
              <th>Wins</th>
              <th>Matches Played</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(player, index) in rankings" :key="player.name">
              <td>{{ index + 1 }}</td>
              <td>{{ player.name }}</td>
              <td>{{ player.wins }}</td>
              <td>{{ player.matches }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "RankingPage",
    props: ["tournamentId"], // Receive tournamentId as a prop
    data() {
      return {
        matches: [], // List of matches for the tournament
        rankings: [], // Calculated rankings
        editableWinners: [], // Editable winners for each match
        error: null,
      };
    },
    created() {
      if (this.$route.params.id) {
        this.fetchMatches();
      } else {
        this.error = "Tournament ID is missing.";
      }
    },
    methods: {
      async fetchMatches() {
        try {
          this.error = null; // Reset error state
          const response = await axios.get(
            `http://127.0.0.1:8000/Records/Match/?tournament=${this.tournamentId}`
          );
          this.matches = response.data;
          this.editableWinners = this.matches.map((match) => match.winner || ""); // Initialize winners
          this.calculateRankings();
        } catch (error) {
          this.error = "Failed to load matches. Please try again.";
          console.error(error);
        }
      },
      calculateRankings() {
        const playerStats = {};
  
        this.matches.forEach((match) => {
          const { player1, player2, winner } = match;
  
          // Initialize stats for player1 and player2 if not already done
          if (!playerStats[player1]) playerStats[player1] = { name: player1, wins: 0, matches: 0 };
          if (!playerStats[player2]) playerStats[player2] = { name: player2, wins: 0, matches: 0 };
  
          // Increment matches played for both players
          playerStats[player1].matches += 1;
          playerStats[player2].matches += 1;
  
          // Increment wins for the winner
          if (winner) {
            playerStats[winner].wins += 1;
          }
        });
  
        // Convert stats object to an array and sort by wins descending
        this.rankings = Object.values(playerStats).sort((a, b) => b.wins - a.wins);
      },
      async updateWinner(matchId, winner) {
        if (!winner) {
          alert("Please select a winner.");
          return;
        }
  
        try {
          this.error = null; // Reset error state
          const response = await axios.patch(`http://127.0.0.1:8000/Records/Match/${matchId}/`, {
            winner,
          });
          alert("Winner updated successfully!");
          this.fetchMatches(); // Refresh matches to reflect changes
        } catch (error) {
          this.error = "Failed to update winner. Please try again.";
          console.error(error);
        }
      },
    },
  };
  </script>
  
  <style>
  .container {
    max-width: 800px;
    margin: auto;
  }

  h1, h2 {
    text-align: center;
  }

  h2 {
    color: #333;
    background-color:rgb(248, 197, 46) ;
    margin-top:30px;
  }
  </style>
  