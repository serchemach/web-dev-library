<script lang="ts">
    import Button, { Label } from "@smui/button";
    import IconButton, { Icon } from '@smui/icon-button';
    import apiClient from "../api";
    import { apiToken } from "../stores";
    import { Link } from "svelte-routing";
    import type { BookView } from "../../openapi_clients";

    export let book: BookView;
    
    console.log(book);
    const backgroundPath = book.preview_path ? `/api/files/${book.preview_path}` : "";

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
        flex-direction: column;
        justify-content: center;
        align-items: center;
        
        height: fit-content;
        width: fit-content;

        min-width: 150px;
        max-width: 300px;

        padding: 10px;

        background-color:burlywood;
        margin: 10px;
        border-radius: 5px;
    }

    #book-icon {
        background-color: blanchedalmond;
        background-size: cover;
        display: flex;
        align-items: center;
        justify-content: center;

        width: 100%;
        height: 100px;
        border-radius: 5px;
    }

    .book-btn {
        display: flex;
        justify-content: center;
        flex-direction: row;
        align-items: center;
    }
</style>

<div class="card-container">
    <div style="width: 95%;">
        <span id="book-icon" style={`background-image: url(${backgroundPath})`}>
            {#if !backgroundPath}
                <Icon class="material-icons">book</Icon>
            {/if}
        </span>
        <span style="text-align: center; min-width: fit-content;">
            <h3>{book.name}</h3>
            <div>{book.description}</div>
        </span>
    </div>
    
    <div class="book-btn">
        <a href={`/api/files/${book.file_path}`}>
            <Icon class="material-icons">download</Icon>
        </a>
        <div style="padding-bottom: 5px">
            <IconButton on:click={book.isFavorite ? removeFavorite : addFavorite} toggle bind:pressed={book.isFavorite}>
                <Icon class="material-icons" on>star</Icon>
                <Icon class="material-icons">star_border</Icon>
            </IconButton>
        </div>

        <Link to={`/books/${book.id}`}>
            <Icon class="material-icons">comment</Icon>
        </Link>
    </div>
</div>

