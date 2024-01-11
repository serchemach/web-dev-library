<script>
    const urlParams = new URLSearchParams(window.location.search);
    const pageNum = parseInt(urlParams.get('page') ?? "0") || 0;

</script>

<div>{`pagenum = ${pageNum}`}</div>
<div>HOME SWEET HOME</div>

