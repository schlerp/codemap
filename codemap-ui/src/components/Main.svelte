<script lang="ts">
    import { currentPage } from "../lib/stores";
    import EditCodeSet from "./EditCodeSet.svelte";
</script>

<main>
    <h2>{$currentPage}</h2>
    <EditCodeSet />
</main>

<style>
    main {
        min-width: 200px;
        background-color: var(--pal-heading-bg, white);
        padding: var(--spacing, 1rem);
        margin: var(--spacing, 1rem);
        border: 0.1rem solid black;
        border-radius: var(--padding-vsmall, 0.25rem);
    }
</style>
