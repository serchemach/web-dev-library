<script>
    import apiClient from "./api";
    import BookList from "./components/BookList.svelte";
    import { apiToken } from "./stores";

    const urlParams = new URLSearchParams(window.location.search);
    const pageNum = parseInt(urlParams.get('page') ?? "0") || 0;

    const pageEntryLimit = 10;
    const bookList = apiClient.get_books({
        queries: {
            offset: 0,
            limit: pageEntryLimit
        },
        headers: {
            Authorization: `Bearer ${$apiToken}`
        }
    });
</script>


<!-- <div>BPPLS </div> -->
{#await bookList}
    Loading books...
{:then books} 
    <BookList bookList={books}/>
{:catch e}
    {e}
{/await}


