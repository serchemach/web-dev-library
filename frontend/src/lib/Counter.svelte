<script lang="ts">
  import LoginForm from "./LoginForm.svelte";
import apiClient from "./api";

  let result = "";
  apiClient.get("/api").then((res) => {
    result = res;
  });

  let res2 = "";
  apiClient.read_file({queries: {file_path: "uploads/1.txt"}}).then((res) => {
    res2 = JSON.stringify(res);
  });

  let count: number = 0
  const increment = () => {
    count += 1
  }
</script>

<button on:click={increment}>
  count is {count}
  response is {result}
</button>

<div>
  response 2 is {res2}
</div>

<LoginForm />
