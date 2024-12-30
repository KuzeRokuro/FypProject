<template>
    <div class="container mb-3">
      <h1 class="form-title">Add Player</h1>
      <form @submit.prevent="addPlayer">
        <div class="form-box">
          <label for="name" class="form-label">
            Name
          </label>
          <input 
            id="name"
            type="text" 
            class="form-control"
            v-model="name"
          />
          <label for="phone" class="form-label">
            Phone Number
          </label>
          <input 
            id="phone"
            type="text" 
            class="form-control"
            v-model="phoneNumber"
          />
          <button
            class="btn-submit"
            type="submit"
          >
            Add Player
          </button>
        </div>
      </form>
    </div>
  </template>

<script>
import axios from "axios";

export default {
  name: "AddPlayer",
  data() {
    return {
      name: "", // Model for player name
      phoneNumber: "" // Model for player phone number
    };
  },
  methods: {
    addPlayer() {
      const newPlayer = {
        name: this.name, // Use 'this' to reference data properties
        phone: this.phoneNumber, // Use 'this' to reference data properties
        totalwins: 0, // Default value for totalwins
        totalmatch: 0 // Default value for totalmatch
      };

      axios
        .post("https://kuzerokuro.pythonanywhere.com/Records/Player/", newPlayer)
        .then((response) => {
          console.log("Player added successfully:", response.data);
          alert("Player added successfully!");
          this.name = ""; // Clear the form
          this.phoneNumber = ""; // Clear the form
        })
        .catch((error) => {
          console.error("Error adding player:", error);
          alert("Failed to add player. Please try again.");
        });
    },
  },
};
</script>
