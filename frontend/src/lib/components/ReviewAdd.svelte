<script lang="ts">
    import type { BookView, Review } from "../../openapi_clients";
    import Textfield from "@smui/textfield";
    import apiClient from "../api";
    import Button, { Label } from "@smui/button";
    import { apiToken } from "../stores";
    export let book: BookView;

    let reviewContent = "";
    let submitResult: Promise<Review>;

    const submitReview = () => {
        submitResult = apiClient.create_review({
            content: reviewContent,
            book_id: book.id
            },{
            headers: {
                Authorization: `Bearer ${$apiToken}`
            }
        });
    }
</script>

<style>
    .review-add {
        display: flex;
        align-items: center;
        flex-direction: column;

        border-radius: 10px;
        background-color: lightgray;
        padding: 10px;
    }

    .rejected {
        color: red;
    }

    .accepted {
        color: green;
    }
</style>

<div class="review-add">
    <Textfield 
        style="width: 100%; margin: 10px"
        helperLine$style="width: 100%;" 
        textarea bind:value={reviewContent} 
        label="Add a review" 
    />
    <Button
        on:click={submitReview}
        style="align-self: flex-end"
        variant="raised"
    >
        <Label>Submit</Label>
    </Button>
</div>
{#if submitResult}
    {#await submitResult then rev} 
        <div class="accepted">
            Successfully added the review
        </div>
    {:catch err}
        <div class="rejected">
            Couldn't add review: {err}
        </div>
    {/await}
{/if}

