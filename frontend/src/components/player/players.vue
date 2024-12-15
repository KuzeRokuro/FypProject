<!-- fetch data from API (?) -->
<template>
    <h1> Player List </h1>
    <div v-for="player in players" :key="player.id" class="player">
    </div>
 </template>

 <script>
 export default {
    data(){
        return {
            players: [],
        }
    },
    mounted() {
        fetch('http://127.0.0.1:8000/player')
        .then(res => res.json)
        .then(data => this.players = data)
        .catch(err => console.log(err.massage))
    },

 } 
 
</script>
