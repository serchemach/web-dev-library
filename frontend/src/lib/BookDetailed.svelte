<script>
    import apiClient from "./api";
    import BookCard from "./components/BookCard.svelte";
    import ReviewAdd from "./components/ReviewAdd.svelte";
    import ReviewList from "./components/ReviewList.svelte";
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
    <center>
        <BookCard {book} />
        <ReviewAdd {book}/>
        <ReviewList reviews={book.reviews}/>
    </center>
{:catch err}
    <div>No such book:</div>
    <div>{err}</div>
{/await}
