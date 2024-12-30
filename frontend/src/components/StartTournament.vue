<template>
    <div class="container mt-5">
      <h1 class ="form-title">Start Tournament</h1>
      <form @submit.prevent="startTournament">
        <!-- Number of Players -->
        <div class="form-box">
          <label for="numPlayers" class="form-label">Number of Players Joining</label>
          <input 
            id="numPlayers" 
            type="number" 
            class="form-control" 
            v-model.number="numPlayers" 
            @change="generatePlayerFields" 
            required 
          />
          <button class="btn-submit" type="submit">Start Tournament</button>
        </div>
  
        <!-- Player Dropdown Fields -->
        <div v-for="(player, index) in selectedPlayers" :key="index" class="mb-3">
          <label :for="'player_' + index" class="form-label">Player {{ index + 1 }}</label>
          <select 
            :id="'player_' + index" 
            class="form-control" 
            v-model="selectedPlayers[index]" 
          >
            <option disabled value="">Select a player</option>
            <option v-for="player in players" :key="player.id" :value="player.id">
              {{ player.name }}
            </option>
          </select>
        </div>
      </form>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
  </template>
  
  <script>
    import axios from "axios";

    export default {
    name: "EditTournament",
    data() {
        return {
        numPlayers: 0, // Number of players
        players: [], // List of players from the database
        selectedPlayers: [], // Selected player IDs
        error: null,
        tournament: {}, // Tournament details
        };
    },
    created() {
        this.fetchTournamentDetails();
        this.fetchPlayers();
    },
    methods: {
        async fetchTournamentDetails() {
        const tournamentId = this.$route.params.id;
        try {
            const response = await axios.get(`https://kuzerokuro.pythonanywhere.com/Records/Tournament/${tournamentId}/`);
            this.tournament = response.data;
        } catch (error) {
            this.error = "Failed to fetch tournament details. Please try again later.";
            console.error(error);
        }
        },
        async fetchPlayers() {
        try {
            const response = await axios.get("https://kuzerokuro.pythonanywhere.com/Records/Player/");
            this.players = response.data;
        } catch (error) {
            this.error = "Failed to fetch player list. Please try again later.";
            console.error(error);
        }
        },
        generatePlayerFields() {
        // Create an array with empty values for the number of players
        this.selectedPlayers = Array(this.numPlayers).fill("");
        },
        async startTournament() {
        const tournamentId = this.$route.params.id;

        try {
            // Generate random seeds and pair players
            const shuffledPlayers = this.selectedPlayers.slice().sort(() => Math.random() - 0.5);
            const matchPayloads = [];

            for (let i = 0; i < shuffledPlayers.length; i += 2) {
            if (i + 1 >= shuffledPlayers.length) {
                this.error = "Odd number of players. Cannot create complete matches.";
                return;
            }

            const player1Id = shuffledPlayers[i];
            const player2Id = shuffledPlayers[i + 1];
            const player1 = this.players.find((p) => p.id === player1Id);
            const player2 = this.players.find((p) => p.id === player2Id);

            matchPayloads.push({
                tournament: `https://kuzerokuro.pythonanywhere.com/Records/Tournament/${tournamentId}/`,
                player1id: `https://kuzerokuro.pythonanywhere.com/Records/Player/${player1Id}/`,
                player1: player1.name,
                player2id: `https://kuzerokuro.pythonanywhere.com/Records/Player/${player2Id}/`,
                player2: player2.name,
                winner: null, // No winner initially
                round: 1, // Set round to 1 for now
            });
            }

            // Send matches to the backend
            for (const match of matchPayloads) {
            await axios.post("https://kuzerokuro.pythonanywhere.com/Records/Match/", match);
            }

            alert("Tournament started successfully!");
            this.$router.push("/tournaments");
        } catch (error) {
            this.error = "Failed to start tournament. Please try again later.";
            console.error(error);
        }
        },
    },
    };
    </script>

  
  <style>
  .container {
    max-width: 600px;
    margin: auto;
  }
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  </style>
  