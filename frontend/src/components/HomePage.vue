<template>
    <div class="home-2">
      <div class="welcome-container">
      <span class="welcome-text">Welcome to the </span>
      <span class="homepage-text">Home Page</span>
    </div>

      <p class="tagline">Manage tournaments and keep your card game community 
        organized. </p>
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

        background-image: url('@/assets/Homepage_bg.jpeg');
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        min-height: 60vh; /* Ensure the section stretches to fit the viewport */
  
      }

      .home-2 {
        text-align: center;
        margin-top: 250px;
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
        box-shadow: 0 8px 16px 0 rgba(10, 8, 8, 0.2), 
        0 6px 20px 0 rgba(119, 119, 119, 0.19);

       }

      
      .buttons button:hover {
        background-color: #af4820;
      }

      .welcome-container {
        text-align: center; /* Center the text */
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
      }

      .welcome-text {
        font-family: 'Roboto';
        font-size: 2.9rem;
        font-weight: bold;
        color: #333; /* Default text color */
      }

      .homepage-text {
        font-family: 'Roboto';
        font-size: 2.9rem;
        font-weight: bold;
        color: #ffffff; /* Text color for "Homepage" */
        background-color: rgb(152, 176, 204); /* 2nd choice : #ff830e
        padding: 0 10px; /* Padding around "Homepage" */
        border-radius: 5px; /* Optional: Add rounded corners */
      }


    </style>
  