<script>
    import TabBar from '@smui/tab-bar';
    import { Link, navigate } from 'svelte-routing';
    import Button, { Label } from '@smui/button';

    export let currentTabIndex = 0;

    const tabs = ['Home', 'Books', 'Users'];
    const tabLinks = ["/", "/books", "/users"]

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


