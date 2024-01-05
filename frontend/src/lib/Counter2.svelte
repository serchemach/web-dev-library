<script lang="ts">
    import Button from '@smui/button';
    let count: number = 0
    const increment = () => {
      count += 1
    }
  </script>

<button on:click={increment}>
    2emcount2 is {count}
</button>
<Button />
