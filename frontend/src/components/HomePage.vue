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
        margin-top: 50px;
      }

      .home h1 {
        font-size: 3rem;
        color: #333;
        font-family: 'Roboto', sans-serif;
      }

      .buttons {
        display: flex;
        justify-content: center; /* Center the buttons horizontally */
        margin-top: 20px; /* Optional: Adjust spacing */
      }

      .buttons button {
        margin: 30px;
        padding: 20px 30px;
        font-size: 20px;
        cursor: pointer;
        border-radius: 5px; /* Optional: rounded corners */
        color: white;
        border: none; /* Remove button border */
      }

      /* Blue button */
      .blue {
        background-color: #4394eb; /* Blue */
      }

      .blue:hover {
        background-color: #0056b3; /* Darker blue on hover */
      }

      /* Red button */
      .red {
        background-color: #ff4a4a; /* Red */
      }

      .red:hover {
        background-color: #c13f1e; /* Darker red on hover */
      }

  </style>
  