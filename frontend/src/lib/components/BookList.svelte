<script>
    import BookCard from "./BookCard.svelte";
    export let bookList = [{id: 0, name: "", description: "", isFavorite: false, file_path: ""}];
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
