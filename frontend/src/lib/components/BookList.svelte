<script lang="ts">
    import BookCard from "./BookCard.svelte";
    import type { BookView } from "../../openapi_clients";
    export let bookList: BookView[];
</script>

<style>
    .list-container {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;

        flex-wrap: wrap;
    }
</style>

<div class="list-container">
    {#each bookList as book}
        <BookCard {book} />
    {/each}
</div>
