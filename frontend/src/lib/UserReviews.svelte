<script lang="ts">
    import apiClient from "./api";
    import { Link } from 'svelte-routing';
    import { apiToken } from "./stores";

    let reviews = apiClient.get_user_reviews({
        headers: {
            Authorization: `Bearer ${$apiToken}`
        }
    });
</script>

<style>
    .review-container {
        margin: 10px;
        text-align: left;
    }

    .review-content {
        border-radius: 5px;
        background-color: lightgray;
    }
</style>

{#await reviews}
    Loading reviews...
{:then revs} 
    {#each revs as review}
        <div class="review-container">
            <Link to={`/books/${review.book.id}`}> 
                <strong>{review.book.name}</strong>
            </Link>
            <div class="review-content">{review.content}</div>
        </div>
    {/each}

    {#if !revs || revs.length === 0}
        <div>No reviews</div>
    {/if}
{:catch}
    <diV>Couldn't load the reviews</diV>
{/await}

