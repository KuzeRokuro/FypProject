<template>
    <div class="container mb-3">
      <h1 class="form-title">Create Tournament</h1>
      <form @submit.prevent="addTournament">
        <div class="form-box">
          <label for="t_name" class="form-label">Name</label>
          <input 
            id="t_name"
            type="text" 
            class="form-control"
            v-model="t_name"
          />
          <label for="date" class="form-label">Date</label>
          <input 
            id="date"
            type="date" 
            class="form-control"
            v-model="date"
          />
          <label for="cardgame" class="form-label">Card Game</label>
          <input 
            id="cardgame"
            type="text" 
            class="form-control"
            v-model="cardgame"
          />
          <button class="btn-submit" type="submit">
            Create Tournament
          </button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "AddTournament",
    data() {
      return {
        t_name: "",
        date: "",
        cardgame: "",
      };
    },
    methods: {
      async addTournament() {
        const newTournament = {
          t_name: this.t_name.trim(),
          date: this.date.trim(),
          cardgame: this.cardgame.trim(),
        };
  
        console.log("Payload being sent:", JSON.stringify(newTournament)); // Debug log for payload
  
        try {
          const response = await axios.post(
            "https://kuzerokuro.pythonanywhere.com/Records/Tournament/",
            newTournament,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          );
          console.log("Response from server:", response.data); // Debug log for server response
          alert("Tournament created successfully!");
        } catch (error) {
          console.error("Error adding tournament:", error); // Debug log for errors
          if (error.response) {
            console.error("Server responded with:", error.response.data); // Log server response error
          }
          alert("Failed to create tournament. Please try again.");
        }
      },
    },
  };
  </script>
  
  <style>
  .container {
    margin-top: 20px;
  }
  
  .btn-primary {
    background-color: #4CAF50;
    border: none;
  }
  
  .btn-primary:hover {
    background-color: #45a049;
  }
  </style>
  