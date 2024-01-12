<script>
    import apiClient from "./api";
    import BookList from "./components/BookList.svelte";
    import { apiToken } from "./stores";

    const urlParams = new URLSearchParams(window.location.search);
    const pageNum = parseInt(urlParams.get('page') ?? "0") || 0;
    
    const pageEntryLimit = 10;
    const bookList = apiClient.get_favorite_books({
        headers: {
            Authorization: `Bearer ${$apiToken}`
        }
    });
</script>


{#await bookList}
    <div>
        Loading books...
    </div>
{:then books} 
    <BookList bookList={books}/>
{:catch e}
    {e}
{/await}
