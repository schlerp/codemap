<script>
    import CodeSetList from "./CodeSetList.svelte";
    import Nav from "./Nav.svelte";
</script>

<aside>
    <Nav />
    <CodeSetList />
</aside>

<style>
    aside {
        background-color: var(--pal-heading-bg, white);
        border-right: 0.1rem solid black;
    }
</style>
