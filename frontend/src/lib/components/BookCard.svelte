<script>
    import Button, { Label } from "@smui/button";

    export let book = {id: 0, name: "", description: "", isFavorite: false};

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
            <Button style="background-color: crimson;">
                <Label>Remove from favorites</Label>
            </Button>
        {:else}
            <Button style="background-color: green;">
                <Label>Add to favorites</Label>
            </Button>
        {/if}

        <Button>
            <Label>Download the book</Label>
        </Button>
    </div>
</div>

