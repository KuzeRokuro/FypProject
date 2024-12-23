<template>
    <div class="container mt-5">
      <h1>Edit Tournament</h1>
      <form @submit.prevent="startTournament">

        <!-- Number of Players -->
        <div class="mb-3">
          <label for="numPlayers" class="form-label">Number of Players Joining</label>
          <input 
            id="numPlayers" 
            type="number" 
            class="form-control" 
            v-model.number="numPlayers" 
            @change="generatePlayerFields" 
            required 
          />
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
        <button class="btn btn-primary" type="submit">Start Tournament</button>
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
            const response = await axios.get(`http://127.0.0.1:8000/Records/Tournament/${tournamentId}/`);
            this.tournament = response.data;
        } catch (error) {
            this.error = "Failed to fetch tournament details. Please try again later.";
            console.error(error);
        }
        },
        async fetchPlayers() {
        try {
            const response = await axios.get("http://127.0.0.1:8000/Records/Player/");
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
        async updateTournament() {
        const tournamentId = this.$route.params.id;
        try {
            const updatedData = {
            ...this.tournament,
            players: this.selectedPlayers, // Send selected player IDs
            };
            await axios.put(`http://127.0.0.1:8000/Records/Tournament/${tournamentId}/`, updatedData);
            alert("Tournament updated successfully!");
            this.$router.push("/tournaments");
        } catch (error) {
            this.error = "Failed to update tournament. Please try again later.";
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