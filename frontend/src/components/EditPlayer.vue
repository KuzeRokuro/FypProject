<template>
    <div class="container">
      <h1 class="form-title">Edit Player</h1>
      <form @submit.prevent="updatePlayer">
        <div class="mb-3">
          <label for="name" class="form-label">
            Name
          </label>
          <input 
            id="name"
            type="text" 
            class="form-control"
            v-model="player.name"
            required
          />
        </div>
        <div class="mb-3">
          <label for="phone" class="form-label">
            Phone Number
          </label>
          <input 
            id="phone"
            type="text" 
            class="form-control"
            v-model="player.phone"
          />
        </div>
        <div class="mb-3">
          <button
            class="btn btn-primary"
            type="submit"
          >
             Player
          </button>
        </div>
      </form>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
  </template>

<script>
import axios from "axios";

export default {
  name: "EditPlayer",
  data() {
    return {
      player: {
        name: "",
        phoneNumber: "",
        totalwins: "",
        totalmatch: "",
      },
      error: null,
    };
  },
  created() {
    this.fetchPlayerDetails();
  },
  methods: {
    async fetchPlayerDetails() {
      const playerId = this.$route.params.id; // Retrieve player ID from route parameters
      try {
        const response = await axios.get(`http://127.0.0.1:8000/Records/Player/${playerId}/`);
        this.player = response.data;
      } catch (error) {
        this.error = "Failed to fetch player details. Please try again later.";
        console.error(error);
      }
    },
    async updatePlayer() {
      const playerId = this.$route.params.id;
      console.log("Payload being sent:", JSON.stringify(this.player));
      try {
        await axios.put(`http://127.0.0.1:8000/Records/Player/${playerId}/`, this.player);
        alert("Player updated successfully!");
        this.$router.push("/players"); // Redirect to players page
      } catch (error) {
        this.error = "Failed to update player. Please try again later.";
        console.error(error);
      }
    },
  },
};
</script>

<style>

    .form-title {
      font-size: 2.5rem;
      color: #303031;
      font-family: 'Roboto', sans-serif;
      text-align: center; 
      margin-bottom: 3rem; /* Space below title */
    }
    
    .form-label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
      color: #333;
    }

</style>