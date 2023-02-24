<script>
    import Footer from "./components/Footer.svelte";
    import Header from "./components/Header.svelte";
    import Main from "./components/Main.svelte";
    import Sidebar from "./components/Sidebar.svelte";
</script>

<div class="page">
    <Header />
    <div class="wrapper">
        <Sidebar />
        <Main />
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
    :global(h1, h2, h3, h4, h5, h6) {
        font-family: 'Proza Libre', sans-serif;
    }
    :global(input) {
        font-family: 'Ubuntu Mono', monospace;
    }
    div.page {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    div.wrapper {
        flex-grow: 1;
        display: flex;
        flex-direction: row;
    }
</style>
