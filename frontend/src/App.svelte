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
    import BookDetailed from './lib/BookDetailed.svelte';
    import UserReviews from './lib/UserReviews.svelte';
</script>

<main>
    <h1>The Library!</h1>
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

        <Route path="/books/:id" let:params>
            <Verify />
            <Header currentTabIndex={1} /> 
            <!-- <div>{JSON.stringify(window.location.search)}</div> -->
            <BookDetailed book_id={parseInt(params.id) || 0}/>
        </Route>

        <Route path="/create-books">
            <Verify />
            <Header currentTabIndex={2} /> 
            <Users />
        </Route>

        <Route path="/my-reviews">
            <Verify />
            <Header currentTabIndex={3} /> 
            <UserReviews />
        </Route>
    </Router>
</main>
<link
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
  rel="stylesheet"
/>
<style>

</style>
