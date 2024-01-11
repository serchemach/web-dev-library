<script>
    import { navigate } from "svelte-routing";
    import { apiToken } from "../stores";
    import to from 'await-to-js';
    import apiClient from "../api";
    import { onMount } from "svelte";

    onMount(async () => {
        console.log($apiToken, $apiToken == "");
        if (!$apiToken || $apiToken == "") {
            navigate("/login");
        }
        else{
            const [err, userObj] = await to(apiClient.get_current_user({
                headers: {
                    Authorization: `Bearer ${$apiToken}`
                }
            }));
            
            console.log(userObj);
            if (err || !userObj) {
                navigate("/login")
            }
        }
    });
</script>

