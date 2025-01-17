<template>
    <div class="container mt-5">
      <h1>Tournament Rankings</h1>
  
      <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
      <div v-if="matches.length" class="form-box-2">
        <h2>Matches</h2>
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Match ID</th>
              <th>Player 1</th>
              <th>Player 2</th>
              <th>Winner</th>
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
              <td>{{ match.round }}</td>
            </tr>
          </tbody>
        </table>
  
        <!-- Start New Round Button -->
        <div class="text-center mt-4" v-if="canStartNewRound">
          <button class="btn btn-primary" @click="startNewRound">
            Start New Round
          </button>
        </div>
        </div>

        <div v-if="matches.length" class="form-box-2">
        <h2 >Player Rankings</h2>
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
    data() {
      return {
        tournamentId: null, // Dynamically set tournament ID
        matches: [],
        rankings: [],
        editableWinners: [],
        predictedMatches: [],
        predictedWinner: [],
        error: null,
        canStartNewRound: false,
        debugLog: null, // Debug log for JSON payload
      };
    },
    created() {
      this.tournamentId = this.$route.params.id; // Get the tournament ID from the route
      if (this.tournamentId) {
        this.fetchMatches();
      } else {
        this.error = "Tournament ID is missing.";
      }
      this.fetchPlayers();
    },
    methods: {
      async fetchMatches() {
        try {
          this.error = null;
          const response = await axios.get(
            `http://127.0.0.1:8000/Records/Match/?tournament=${this.tournamentId}`
          );
          this.matches = response.data.filter(
            (match) => match.tournament === `http://127.0.0.1:8000/Records/Tournament/${this.tournamentId}/`
          );
          this.editableWinners = this.matches.map((match) => match.winner || "");
          this.checkIfNewRoundCanStart();
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
          if (!playerStats[player1]) playerStats[player1] = { name: player1, wins: 0, matches: 0 };
          if (!playerStats[player2]) playerStats[player2] = { name: player2, wins: 0, matches: 0 };
          playerStats[player1].matches += 1;
          playerStats[player2].matches += 1;
          if (winner) {
            playerStats[winner].wins += 1;
          }
        });
        this.rankings = Object.values(playerStats).sort((a, b) => b.wins - a.wins);
      },
      async fetchPlayers() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/Records/PlayersByTournament/${this.tournamentId}/`);
          this.players = response.data;
          console.log("Players fetched:", this.players);
        } catch (error) {
          console.error("Error fetching players:", error);
        }
      },
      async predictRound() { 
        try { 
          // Find the highest round in the matches
          const highestRound = Math.max(...this.matches.map(match => match.round));
  
          // Prepare the data to send 
          const inputpredictdata = { 
            tournamentId: this.tournamentId, 
            highestRound: highestRound 
          };
  
          const response = await axios.post('http://127.0.0.1:8000/predict/', inputpredictdata); 
          const predictedMatches = response.data; 
  
          // Map the predicted matches to the corresponding matches 
          this.predictedMatches = this.matches.map(match => { 
            const predictedMatch = predictedMatches.find(pred => pred.match_id === match.id); 
            return { 
              ...match, 
              predicted_winner: predictedMatch ? predictedMatch.predicted_winner : null 
            }; 
          });
  
          console.log("Predicted Matches:", this.predictedMatches); 
        } catch (error) { 
          console.error("Error predicting round:", error); 
          this.error = "Failed to predict the round. Please try again."; 
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
  
  h1 {
    text-align: center;
    margin-top: 35px;
    margin-bottom: 35px;
   
  }
  
  h2 {
    font-family: 'Roboto';
    color: white;
    text-align: center;
    background-color: #438b82 ;
    padding: 2px;
  }
  
  
  </style>
  