<template>
    <div class="home">
      <h1>Welcome to the Home Page </h1>
      <p class="tagline">Manage tournaments and keep your card game community 
        organized, informed, and engaged. </p>
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
        margin-top: 200px;
      }

      .home h1 {
        font-family: sans-serif;
        font-size: 2.5rem;
        color: #333;
      }

      .tagline {
        font-size: 1.3rem;
        color: #555;
        margin-top: 10px;
      }

      .buttons {
        display: flex;
        justify-content: center; /* Center the buttons  */
        gap: 30px; /* Add space between buttons */
        margin-top: 50px; 
      }

      .buttons button {
        padding: 15px 37px;
        font-size: 1.2rem;
        color: #fff;
        background-color: #ff830e ;
        border: none;
        border-radius: 30px;
        cursor: pointer;
      }

      .buttons button:hover {
        background-color: #af4820;
      }

    </style>
  