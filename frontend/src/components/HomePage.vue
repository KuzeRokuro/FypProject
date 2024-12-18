<template>
    <div class="home">
      <h1>Welcome to the Home Page</h1>
      <div class="buttons">
        <button @click="goToPlayers">Player</button>
        <button @click="goToTournaments">Tournament</button>
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
    margin-top: 50px;
  }
  
  .buttons button {
    margin: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>
  