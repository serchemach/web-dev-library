<script lang="ts">
    import { Link, navigate } from "svelte-routing";
    import apiClient from "./api";
    import BookList from "./components/BookList.svelte";
    import { apiToken } from "./stores";
    import Button from "@smui/button";
    import { Label } from "@smui/button";

    let urlParams = new URLSearchParams(window.location.search);
    let pageNum = parseInt(urlParams.get('page') ?? "0") || 0;

    const pageEntryLimit = 15;

    let bookList = apiClient.get_books({
        queries: {
            offset: pageNum * pageEntryLimit,
            limit: pageEntryLimit + 1
        },
        headers: {
            Authorization: `Bearer ${$apiToken}`
        }
    });

    const refetch = () => {
        bookList = apiClient.get_books({
            queries: {
                offset: pageNum * pageEntryLimit,
                limit: pageEntryLimit + 1
            },
            headers: {
                Authorization: `Bearer ${$apiToken}`
            }
        });
    }
    const moveForward = () => {
        pageNum += 1;
        navigate(`/books?page=${pageNum}`);
        refetch();
    }
    const moveBack = () => {
        pageNum -= 1;
        if (pageNum < 0) {
            pageNum = 0;
        }
        navigate(`/books?page=${pageNum}`);
        refetch();
    }
</script>


{#await bookList}
<div>
    Loading books...
</div>
{:then books} 
    <div>
        {#if pageNum > 0}
            <Button on:click={moveBack} variant="outlined">
                <Label>{"<"}</Label>
            </Button>
        {/if}
        <Label>{pageNum}</Label>
        {#if books.length === pageEntryLimit + 1}
            <Button on:click={moveForward} variant="outlined">
                <Label>{">"}</Label>
            </Button>
        {/if}
    </div>

    <BookList bookList={books.slice(0, pageEntryLimit)}/>

    <div>
        {#if pageNum > 0}
            <Button on:click={moveBack} variant="outlined">
                <Label>{"<"}</Label>
            </Button>
        {/if}
        <Label>{pageNum}</Label>
        {#if books.length === pageEntryLimit + 1}
            <Button on:click={moveForward} variant="outlined">
                <Label>{">"}</Label>
            </Button>
        {/if}
    </div>
{:catch e}
    {e}
{/await}


