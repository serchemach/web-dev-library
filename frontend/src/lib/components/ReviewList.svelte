<script lang="ts">
    import type { ReviewView } from "../../openapi_clients";

    export let reviews: ReviewView[];
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

{#each reviews as review}
    <div class="review-container">
        <strong>{review.owner.username}</strong>
        <div class="review-content">{review.content}</div>
    </div>
{/each}

{#if !reviews || reviews.length === 0}
    <div>No reviews</div>
{/if}

