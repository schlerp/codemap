<script lang="ts">
    import { pages } from "../lib/constants";
    import { currentPage } from "../lib/stores";

    function setPage(page: string) {
        currentPage.set(page);
    }
</script>

<nav>
    <ul>
        {#each Object.values(pages) as page}
            <li
                on:click={() => setPage(page)}
                class={$currentPage === page ? "selected" : ""}
            >
                {page}
            </li>
        {/each}
    </ul>
</nav>

<style>
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        min-width: 7rem;
        padding-inline: var(--padding, 1rem);
        margin-inline: var(--padding-small, 0.5rem);
        padding-block: var(--padding-vsmall, 0.25rem);
        margin-block: var(--padding-small, 0.5rem);
        border-radius: var(--padding-vsmall, 0.25rem);
        text-align: center;
    }
    li:hover {
        cursor: pointer;
        background-color: #fca311;
    }
    li.selected {
        background-color: var(--pal-heading-bg, black);
        color: var(--pal-heading-fg, white);
    }
</style>
