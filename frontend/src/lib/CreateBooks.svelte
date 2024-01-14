<script lang="ts">
    import Textfield from "@smui/textfield";
    import apiClient from "./api";
    import Button from "@smui/button/src/Button.svelte";
    import { Label } from "@smui/button";

    let isWrongFileType = false;
    let noFilesErr = false;
    let isSuccessfulSubmit = false;
    let bookFiles: FileList = [];
    $: if (bookFiles.length) {
        if (bookFiles[0].type != "application/pdf"){
            isWrongFileType = true;
            bookFiles = [];
        }
        else {
            isWrongFileType = false;
            noFilesErr = false;
        }
    }

    let bookTitle = "";
    let bookDescription = "";

    const submitBook = () => {
        isSuccessfulSubmit = false;
        if (!bookFiles.length) {
            noFilesErr = true;
        }
        else {
            apiClient.upload_book({
                file: bookFiles[0]
            }, {
                queries: {
                    description: bookDescription,
                    name: bookTitle
                }
            }).then((book) => {
                isSuccessfulSubmit = true;
            }).catch((err) => {
                isSuccessfulSubmit = false;
            })
        }
    }
</script>

<style>
    .hide-file-ui :global(input[type='file']::file-selector-button) {
        display: none;
    }
    
    .hide-file-ui
        :global(:not(.mdc-text-field--label-floating) input[type='file']) {
        color: transparent;
        margin-bottom: 20px;
    }
</style>

<div>create-books</div>
<div>
    <Textfield invalid={noFilesErr} bind:value={bookTitle} label="Title" />
</div>
<div>
    <Textfield invalid={noFilesErr} bind:value={bookDescription} label="Description" />
</div>

<div class="hide-file-ui">
    <Textfield invalid={isWrongFileType || noFilesErr} bind:files={bookFiles} label="File" type="file" />
</div>
{#if isWrongFileType}
    <div style="color: red;">Only pdf files are accepted</div>
{/if}

{#if noFilesErr}
    <div style="color: red;">Book has to have a file</div>
{/if}
<div style="margin-top: 20px;">
    <Button on:click={submitBook} variant="raised">
        <Label>Submit</Label>
    </Button>
</div>

{#if isSuccessfulSubmit}
    <div style="color: green;">
        Successfully created the book
    </div>
{/if}