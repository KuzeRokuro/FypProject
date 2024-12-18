<template>
    <div id="app">
      <header>
        <nav>
          <router-link to="/">Home</router-link>
          <router-link to="/players">Players</router-link>
          <router-link to="/tournaments">Tournaments</router-link>
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
  header {
    background-color: #333;
    color: white;
    padding: 0.5rem;
    text-align: center;
  }
  nav {
    margin-top: 1rem;
  }
  nav a {
    margin: 0 10px;
    color: white;
    text-decoration: none;
  }
  nav a.router-link-active {
    font-weight: bold;
    text-decoration: underline;
  }
  </style>
  