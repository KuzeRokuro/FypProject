<template>
  <div id="app">
    <header>
      <nav>
        <div class="nav-logo">
          <img src="@/assets/Hobby_Outpost-dark.png" alt="Logo" class="logo" />
        </div>

        <button class="nav-toggle" @click="toggleNav">
          ☰
        </button>

        <div :class="['nav-links', { 'nav-links-show': isNavOpen }]">
          <router-link to="/">Home</router-link>
          <router-link to="/players">Players</router-link>
          <router-link to="/tournaments">Tournaments</router-link>
        </div>
      </nav>
    </header>
    <router-view />
  </div>
</template>

  <script>
  export default {
    name: "App",
    data() {
      return {
        isNavOpen: false,
      };
    },
    methods: {
      toggleNav() {
        this.isNavOpen = !this.isNavOpen;
      },
    },
  };
  </script>

  
  
  <style>
    /* General styles */
    #app {
      background-image: url('@/assets/Background_pattern.png');
      background-size: 500px;
      background-repeat: repeat;
      background-position: top left;
      min-height: 100vh;
    }

    header {
      background-color: #272727;
    }

    nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.5rem;
      position: relative; 
    }

    .nav-logo {
      flex-shrink: 0;
      margin-right: 20px;
    }

    .logo {
      width: 130px;
      height: auto;
    }

    /* Ensure links are visible on desktop */
    .nav-links {
      display: flex;
      gap: 20px; /* Space between links */
      align-items: center;
      flex-grow: 1;
    }

    /* Ensure hamburger menu is hidden on desktop */
    .nav-toggle {
      display: none;
      background: none;
      border: none;
      font-size: 1.5rem;
      color: white;
      cursor: pointer;
    }

    /* Mobile-specific styles */
    @media (max-width: 768px) {
      .nav-links {
        display: none; /* Hide links by default on mobile */
        flex-direction: column;
        background-color: #272727;
        position: absolute;
        top: 60px;
        right: 0;
        width: 100%;
        padding: 1rem 0;
      }

      .nav-links-show {
        display: flex; /* Show links when toggle is active */
      }

      .nav-toggle {
        display: block; /* Show toggle button on mobile */
      }
    }

    .nav-links a {
      color: white;
      text-decoration: none;
      font-size: 1.1rem;
      padding: 0.5rem 1rem; /* Add padding to make touch-friendly */
    }

    .nav-links a.router-link-active {
      font-weight: bold;
    }

    a:hover {
      background-color: rgb(100, 100, 100);
      padding: 5px 10px;
      border-radius: 5px;
      transition: background-color 0.3s ease, padding 0.3s ease;
    }

    </style>
      