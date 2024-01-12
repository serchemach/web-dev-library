<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import { Router, Link, Route } from "svelte-routing";
  import LoginForm from './lib/LoginForm.svelte';
  import Home from './lib/Home.svelte';
    import Verify from './lib/components/Verify.svelte';
    import Books from './lib/Books.svelte';
    import Users from './lib/CreateBooks.svelte';
    import Header from './lib/components/Header.svelte';
</script>

<main>
    <Router>
        <Route path="/login" component={LoginForm} />

        <Route path="/">
            <Verify />
            <Header currentTabIndex={0} /> 
            <Home />
        </Route>
        
        <Route path="/books">
            <Verify />
            <Header currentTabIndex={1} /> 
            <!-- <div>{JSON.stringify(window.location.search)}</div> -->
            <Books />
        </Route>

        <Route path="/create-books">
            <Verify />
            <Header currentTabIndex={2} /> 
            <Users />
        </Route>
    </Router>
</main>

<style>

</style>
