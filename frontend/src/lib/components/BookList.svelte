<script>
    import BookCard from "./BookCard.svelte";
    export let bookList = [{id: 0, name: "", description: "", isFavorite: false, file_path: ""}];
</script>


{#each bookList as book}
    <BookCard {book} />
{/each}
