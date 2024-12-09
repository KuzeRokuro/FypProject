<template>
  <navbar
      :pages="pages"
      :active-page="activePage"
      :nav-link-click="(index) => activePage = index"
  ></navbar>
  
  <page-viewer 
      :page="pages[activePage]"
  ></page-viewer>
</template>

<script>
import Navbar from './components/Navbar.vue';
import PageViewer from './components/PageViewer.vue';

export default {
  components: {
      Navbar,
      PageViewer
  },
  data() {
      return {
          activePage: 0,
          pages: [
              {
                  link: {text: 'Home', url: 'index.html'},
                  pageTitle: 'Home Page',
                  content: 'This is the home content'
              },
              {
                  link: {text: 'Player', url: 'player.html'},
                  pageTitle: 'Player Page',
                  content: 'This is the player content'
              },
              {
                  link: {text: 'Tournament', url: 'tournament.html'},
                  pageTitle: 'Tourney Page',
                  content: 'This is the Tournament content'
              }
          ]
      };
  },
}
</script>