<script>
    import { Link, navigate } from 'svelte-routing';
    import Button, { Label } from '@smui/button';

    export let currentTabIndex = 0;

    const tabs = ['Favorite books', 'All books', 'Create books', 'My reviews'];
    const tabLinks = ["/", "/books", "/create-books", "/my-reviews"]

</script>

<style>
    
</style>

{#each tabs as tab, i (i)}
    <Link style="text-decoration:none" to={tabLinks[i]}>

        <Button variant={i == currentTabIndex ? "unelevated" : "outlined"} >
            <Label>{tab}</Label>
        </Button>
    </Link>
{/each}


