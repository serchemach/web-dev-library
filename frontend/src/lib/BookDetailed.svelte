<script>
    import apiClient from "./api";
    import BookCard from "./components/BookCard.svelte";
    import { apiToken } from "./stores";

    export let book_id = 0;
    let book_obj = apiClient.get_book_by_id_with_favorite_and_reviews({
        params: {
            id: book_id
        },
        headers: {
            Authorization: `Bearer ${$apiToken}`
        }
    });
</script>

<h2>Book with id={book_id}</h2>

{#await book_obj}
    Loading the book...
{:then book} 
    <BookCard {book} />
{:catch err}
    <div>No such book:</div>
    <div>{err}</div>
{/await}
