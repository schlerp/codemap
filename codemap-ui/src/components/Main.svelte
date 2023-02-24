<script>
    import { currentPage } from "../lib/stores.js";
</script>

<main>{$currentPage}</main>

<style>
    main {
        min-width: 200px;
        height: 100%;
        background-color: var(--pal-heading-bg, white);
    }
</style>
