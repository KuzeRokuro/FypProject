<template>
    <div id="app">
      <header>
        <nav>

          <div class="nav-logo">
          <img src="@/assets/Hobby_Outpost-dark.png" alt="Logo" class="logo" />
          </div>
          
          <div class="nav-links">
          <router-link to="/">Home</router-link>
          <router-link to="/players">Players</router-link>
          <router-link to="/tournaments">Tournaments</router-link>
          </div>

        </nav>
      </header>
      <!-- Render the routed component -->
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name: "App",
  };
  </script>
  
  
  <style>
    /* Add some basic styling (optional) */
    /* Header and Navbar Styles */
    #app {
      background: #ffffff ; /* aolid orange bg*/
      min-height: 100vh; /* Make sure it covers the full viewport height */
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif; 
    }

    header {
      background-color: #272727;
      color: #333(0, 0, 0);
    }

    nav {
      display: flex; /* Flexbox for horizontal layout */
      align-items: center; /* Center items vertically */
      padding: 0.5rem; 
    }

    .nav-logo {
      flex-shrink: 0; /* Prevent the logo from shrinking */
      margin-right: 20px;
    }

    .logo {
      width: 150px; /* Adjust size for a larger logo */
      height: auto; /* Maintain aspect ratio */
    }

    .nav-links {
      display: flex; 
      gap: 40px; /* Add space between links */
      align-items: center;
    }

    .nav-links a {
      color: rgb(255, 255, 255);
      text-decoration: none;
      font-size: 1.2rem; 
    }

    .nav-links a.router-link-active {
      font-weight: bold;
    }

    a:hover {
      background-color: rgb(100, 100, 100); /* Yellow highlight */
      padding: 5px 10px; /* Add padding to increase the size of the highlight */
      border-radius: 5px; /* Optional: Add rounded corners for a nicer look */
      transition: background-color 0.3s ease, padding 0.3s ease; /* Smooth transition */
    }

    </style>
      