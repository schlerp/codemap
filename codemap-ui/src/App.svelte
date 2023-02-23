<script>
    import Footer from "./components/Footer.svelte";
    import Header from "./components/Header.svelte";
    import Sidebar from "./components/Sidebar.svelte";
    import { currentPage } from "./lib/stores.js";
</script>

<div class="page">
    <Header />
    <div class="wrapper">
        <Sidebar />
        <main>{$currentPage}</main>
    </div>
    <Footer />
</div>

<style>
    :global(html, body) {
        width: 100%;
        height: 100%;
        font-family: "Work Sans", sans-serif;
        color: var(--pal-heading-fg, black);
        background-color: var(--pal-heading-bg, white);
        padding: 0;
        border: 0;
        margin: 0;
    }
    div.page {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    div.wrapper {
        display: flex;
        flex-direction: row;
    }
    main {
        min-width: 200px;
        height: 100%;
        background-color: var(--pal-heading-bg, white);
    }
</style>
