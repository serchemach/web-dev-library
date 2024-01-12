<script lang="ts">
    import Button, { Label } from "@smui/button";
    import apiClient from "../api";
    import { apiToken } from "../stores";

    export let book = {id: 0, name: "", description: "", isFavorite: false, file_path: ""};

    const addFavorite = () => {
        apiClient.add_favorite_book({
            queries: {
                book_id: book.id
            },
            headers: {
                Authorization: `Bearer ${$apiToken}`
            }
        }).then(()=>{
            book.isFavorite = true;
        })
    }

    const removeFavorite = () => {
        apiClient.remove_favorite_book({
            queries: {
                book_id: book.id
            },
            headers: {
                Authorization: `Bearer ${$apiToken}`
            }
        }).then(()=>{
            book.isFavorite = false;
        })
    } 
</script>

<style>
    .card-container {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        height: 150px;
        background-color:burlywood;
        margin: 10px;
        border-radius: 10px;
    }

    .book-icon {
        background-color: blanchedalmond;
        width: 50px;
        height: 100px;
        border-radius: 5px;
        margin-left: 50px;
        margin-right: 50px;
    }

    .book-favorite-btn {
        margin-left: auto;
        margin-right: 40px;
        text-align: right;
    }
</style>

<div class="card-container">
    <span class="book-icon">COOL BOOK ICON</span>
    <span style="text-align: left;">
        <div>Book Title: {book.name}</div>
        <div>Book Description: {book.description}</div>
    </span>
    <div class="book-favorite-btn">
        {#if book.isFavorite}
            <Button style="background-color: crimson;" on:click={removeFavorite}>
                <Label>Remove from favorites</Label>
            </Button>
        {:else}
            <Button style="background-color: green;" on:click={addFavorite}>
                <Label>Add to favorites</Label>
            </Button>
        {/if}

        <a href={`/api/files/${book.file_path}`}>
            <Button>
                <Label>Download the book</Label>
            </Button>
        </a>
    </div>
</div>

