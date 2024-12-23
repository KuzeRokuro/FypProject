<template>
    <div class="container mt-5">
      <h1>Edit Tournament</h1>
      <form @submit.prevent="updateTournament">
        <div class="mb-3">
          <label for="t_name" class="form-label">Name</label>
          <input 
            id="t_name" 
            type="text" 
            class="form-control" 
            v-model="tournament.t_name" 
            required 
          />
        </div>
        <div class="mb-3">
          <label for="date" class="form-label">Date</label>
          <input 
            id="date" 
            type="date" 
            class="form-control" 
            v-model="tournament.date" 
            required 
          />
        </div>
        <div class="mb-3">
          <label for="cardgame" class="form-label">Card Game</label>
          <input 
            id="cardgame" 
            type="text" 
            class="form-control" 
            v-model="tournament.cardgame" 
            required 
          />
        </div>
        <button class="btn btn-primary" type="submit">Update Tournament</button>
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
        error: null,
      };
    },
    created() {
      this.fetchTournamentDetails();
    },
    methods: {
      async fetchTournamentDetails() {
        const tournamentId = this.$route.params.id; // Retrieve tournament ID from route parameters
        try {
          const response = await axios.get(`http://127.0.0.1:8000/Records/Tournament/${tournamentId}/`);
          this.tournament = response.data;
        } catch (error) {
          this.error = "Failed to fetch tournament details. Please try again later.";
          console.error(error);
        }
      },
      async updateTournament() {
        const tournamentId = this.$route.params.id;
        try {
          await axios.put(`http://127.0.0.1:8000/Records/Tournament/${tournamentId}/`, this.tournament);
          alert("Tournament updated successfully!");
          this.$router.push("/tournaments"); // Redirect to tournaments page
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
  