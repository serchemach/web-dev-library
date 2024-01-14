<script lang="ts">
    import { ReviewView } from "../openapi_clients";
    import apiClient from "./api";
    import { apiToken } from "./stores";

    let reviews: ReviewView[] = apiClient.get_user_reviews({
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
            <strong>{review.book.name}</strong>
            <div class="review-content">{review.content}</div>
        </div>
    {/each}
    
    {#if !reviews || reviews.length === 0}
        <div>No reviews</div>
    {/if}
{:catch}
    <diV>Couldn't load the reviews</diV>
{/await}

