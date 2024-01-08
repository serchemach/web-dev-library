<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Counter2 from './lib/Counter2.svelte';
  import { Router, Link, Route } from "svelte-routing";
  import LoginForm from './lib/LoginForm.svelte';
  import Home from './lib/Home.svelte';
</script>

<main>
  <Router>
    <nav>
      <Link to="/login">LoginForm</Link>
      <Link to="/">Home</Link>
    </nav>
    <div>
      <Route path="/login" component={LoginForm} />
      <Route path="/"><Counter /></Route>
      <Route path="/home"><Home /></Route>
    </div>
  </Router>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
