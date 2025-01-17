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

      <!-- Start New Round Button -->
      <div class="text-center mt-4" v-if="canStartNewRound">
        <button class="btn btn-primary" @click="startNewRound">
          Start New Round
        </button>
      </div>
      </div>


      <!-- Predict Round Button -->
      <div class="text-center mt-4">
        <button class="btn btn-secondary" @click="predictRound">
          Predict Round </button>
      </div>


      <!-- Predicted Matches Table -->
       <div v-if="predictedMatches.length" class="mt-5">
        <div v-if="matches.length" class="form-box-2">
        <h2>Predicted Matches</h2>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Match ID</th>
              <th>Player 1</th>
              <th>Player 2</th>
              <th>Predicted Winner</th>
              <th>Round</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in predictedMatches" :key="index">
              <td>{{ match.id }}</td>
              <td>{{ match.player1 }}</td>
              <td>{{ match.player2 }}</td>
              <td>{{ match.predicted_winner }}</td>
              <td>{{ match.round }}</td>
            </tr>
          </tbody>
        </table>
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
          `https://kuzerokuro.pythonanywhere.com/Records/Match/?tournament=${this.tournamentId}`
        );
        this.matches = response.data.filter(
          (match) => match.tournament === `https://kuzerokuro.pythonanywhere.com/Records/Tournament/${this.tournamentId}/`
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
    checkIfNewRoundCanStart() {
      const currentRound = Math.max(...this.matches.map((match) => match.round));
      const matchesInCurrentRound = this.matches.filter(
        (match) => match.round === currentRound
      );
      this.canStartNewRound = matchesInCurrentRound.every(
        (match) => match.winner && match.winner.trim() !== ""
      );
    },
    async updateWinner(matchId, winner) {
      if (!winner) {
        alert("Please select a winner.");
        return;
      }
      try {
        this.error = null;
        await axios.patch(`https://kuzerokuro.pythonanywhere.com/Records/Match/${matchId}/`, { winner });
        alert("Winner updated successfully!");
        this.fetchMatches();
      } catch (error) {
        this.error = "Failed to update winner. Please try again later.";
        console.error(error);
      }
    },
    async startNewRound() {
      try {
        const currentRound = Math.max(...this.matches.map((match) => match.round));
        const players = this.players.map((player) => ({
          name: player.name,
          id: player.id,
          score: this.matches
            .filter((match) => match.winner === player.name)
            .length,
        }));

        // Sort players by score in descending order
        players.sort((a, b) => b.score - a.score);

        const newRound = currentRound + 1;
        const newMatches = [];

        if (!this.players || this.players.length === 0) {
          console.error("Players array is empty or not properly populated.");
          alert("Unable to start new round. No player data available.");
          return;
        }

        // Pair players with similar scores
        for (let i = 0; i < players.length; i += 2) {
          if (i + 1 < players.length) {
            const player1 = players[i];
            const player2 = players[i + 1];

            newMatches.push({
              tournament: `https://kuzerokuro.pythonanywhere.com/Records/Tournament/${this.tournamentId}/`,
              player1id: `https://kuzerokuro.pythonanywhere.com/Records/Player/${player1.id}/`,
              player1: player1.name,
              player2id: `https://kuzerokuro.pythonanywhere.com/Records/Player/${player2.id}/`,
              player2: player2.name,
              winner: null,
              round: newRound,
            });
          } else {
            // Handle the case where there is an odd number of players
            const player1 = players[i];

            newMatches.push({
              tournament: `https://kuzerokuro.pythonanywhere.com/Records/Tournament/${this.tournamentId}/`,
              player1id: `https://kuzerokuro.pythonanywhere.com/Records/Player/${player1.id}/`,
              player1: player1.name,
              player2id: null,
              player2: null,
              winner: null,
              round: newRound,
            });
          }
        }

        // Log the payload for debugging
        this.debugLog = JSON.stringify(newMatches, null, 2);
        console.log("New matches payload:", newMatches);

        // POST each new match individually to the backend
        for (const match of newMatches) {
          console.log("Posting match:", match); // Log each match before posting
          try {
            const response = await axios.post(`https://kuzerokuro.pythonanywhere.com/Records/Match/`, match);
            console.log("Response from backend:", response.data);
          } catch (postError) {
            console.error("Error posting match:", postError.response ? postError.response.data : postError.message);
          }
        }

        // Update player stats
        await this.updatePlayerStats();

        alert("New round started!");
        this.fetchMatches();
      } catch (error) {
        this.error = "Failed to start a new round. Please try again.";
        console.error("Error details:", error.response ? error.response.data : error.message);
      }
    },
    async updatePlayerStats() {
      try {
        // Get all matches for each player
        const allMatches = await axios.get("https://kuzerokuro.pythonanywhere.com/Records/Match/");

        for (const player of this.players) {
          let totalMatches = 0;
          let totalWins = 0;

          // Filter matches for the current player
          const playerMatches = allMatches.data.filter(
            (match) =>
              match.player1 === player.name ||
              match.player2 === player.name
          );

          playerMatches.forEach(match => {
            totalMatches++;
            if (match.winner === player.name) {
              totalWins++;
            }
          });

          player.totalmatch = totalMatches;
          player.totalwins = totalWins;

          // Update player data on the server
          const playerData = {
            totalmatch: totalMatches,
            totalwins: totalWins,
          };
          await axios.patch(`https://kuzerokuro.pythonanywhere.com/Records/Player/${player.id}/`, playerData);
        }
      } catch (updateError) {
        console.error("Error updating player data:", updateError.response ? updateError.response.data : updateError.message);
      }
    },
    getPlayerIdByName(playerName) {
      const player = this.rankings.find((p) => p.name === playerName);
      if (!player) {
        console.error(`Player not found: ${playerName}`);
      }
      return player ? player.id : null;
    },
    async fetchPlayers() {
      try {
        const response = await axios.get(`https://kuzerokuro.pythonanywhere.com/Records/PlayersByTournament/${this.tournamentId}/`);
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

        const response = await axios.post('https://kuzerokuro.pythonanywhere.com/predict/', inputpredictdata);
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
