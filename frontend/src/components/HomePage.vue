<template>
    <div class="home">
      <h1>Welcome to the Home Page </h1>
      <div class="buttons">
        <button class="blue" @click="goToPlayers">Player</button>
        <button class="red" @click="goToTournaments">Tournament</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomePage",
    methods: {
      goToPlayers() {
        // Navigate to the Player page
        this.$router.push("/players");
      },
      goToTournaments() {
        // Navigate to the Tournament page
        this.$router.push("/tournaments");
      },
    },
  };
  </script>
  
  <style>

      .home {
        text-align: center;
        margin-top: 70px;
      }

      .home h1 {
        font-size: 3rem;
        color: #333;
        font-family: 'Roboto', sans-serif;
      }

      .buttons {
        display: flex;
        justify-content: center; /* Center the buttons  */
        gap: 20px; /* Add space between buttons */
        margin-top: 20px; 
      }

      .buttons button {
        padding: 10px 20px;
        font-size: 1rem;
        color: #fff;
        background-color: #303031;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }

      .buttons button:hover {
        background-color: #444;
      }

    </style>
  