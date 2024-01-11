<script lang="ts">
    import "../bare.css"
    import to from 'await-to-js';
    import { navigate } from "svelte-routing";
    import apiClient from "./api";
    import Textfield from '@smui/textfield';
    import HelperText from '@smui/textfield/helper-text';
    import Button, { Label } from "@smui/button";
    import { apiToken } from "./stores";

    let username = "";
    let password = "";
    let isValidLogin = true;

    const onLogin = async () => {
        const [err, tokenObj] = await to(apiClient.generate_token({
            username, password
        }));

        if (err || !tokenObj) {
            isValidLogin = false;
            return ;
        }

        console.log(tokenObj);
        $apiToken = tokenObj.access_token;
        navigate("/");
    }
</script>
  
<style>
    .invalid-login {
        color: red;
        margin: 10px;
    }

    
    #container {
        max-width: 1280px;
        margin: 0 auto;
        padding: 2rem;
        text-align: center;
    }
</style>

<div id="container">
    <Textfield invalid={!isValidLogin} bind:value={username} label="Username">
        <HelperText slot="helper">Helper Text</HelperText>
    </Textfield>

    <Textfield type="password" invalid={!isValidLogin} bind:value={password} label="Password">
        <HelperText slot="helper">Helper Text</HelperText>
    </Textfield>

    <Button on:click={onLogin} variant="raised">
        <Label>Login</Label>
    </Button>

    {#if !isValidLogin}
        <div class="invalid-login">
            Either the password or the username are invalid
        </div>
    {/if}
</div>
