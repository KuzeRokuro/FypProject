<template>
    <div class="container">
      <h1 class="form-title" >Edit Tournament</h1>
      <form @submit.prevent="updateTournament">
        <div class="form-box">
          <label for="t_name" class="form-label">Name</label>
          <input 
            id="t_name" 
            type="text" 
            class="form-control" 
            v-model="tournament.t_name" 
            required 
          />
          <label for="date" class="form-label">Date</label>
          <input 
            id="date" 
            type="date" 
            class="form-control" 
            v-model="tournament.date" 
            required 
          />
          <label for="cardgame" class="form-label">Card Game</label>
          <input 
            id="cardgame" 
            type="text" 
            class="form-control" 
            v-model="tournament.cardgame" 
            required 
          />
          <button class="btn-submit" type="submit">Update Tournament</button>
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
          tournament: {
            t_name: "",
            date: "",
            cardgame: "",
          },
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
        async updateTournament() {
          const tournamentId = this.$route.params.id;
          try {
            const updatedData = {
              ...this.tournament,
              players: this.selectedPlayers, // Send selected player IDs
            };
            await axios.put(`https://kuzerokuro.pythonanywhere.com/Records/Tournament/${tournamentId}/`, updatedData);
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
  