import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import PlayersPage from "../components/PlayersPage.vue";
import TournamentsPage from "../components/TournamentsPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/players",
    name: "Players",
    component: PlayersPage, // Replace with your actual Players page component
  },
  {
    path: "/tournaments",
    name: "Tournaments",
    component: TournamentsPage, // Replace with your actual Tournaments page component
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
