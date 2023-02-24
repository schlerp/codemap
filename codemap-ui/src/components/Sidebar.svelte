<script>
    import CodeSetList from "./CodeSetList.svelte";
import Nav from "./Nav.svelte";
</script>

<aside>
    <Nav />
    <h3>Codesets</h3>
    <CodeSetList />
</aside>

<style>
    aside {
        background-color: var(--pal-heading-bg, white);
        border-right: 0.1rem solid black;
    }
    h3 {
        padding-inline: var(--padding, 1rem);
    }
</style>
