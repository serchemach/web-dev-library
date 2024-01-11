<script>
    import apiClient from "../api";
    import BookCard from "./BookCard.svelte";

    export let bookList = [{id: 0, name: "", description: "", isFavorite: false}];

</script>


{#each bookList as book}
    <BookCard {book} />
{/each}
