<script lang="ts">
    import { codeSets } from "../lib/stores";


</script>

<ul>
    {#each $codeSets as codeSet }
    <li>
        {codeSet.name}
        <span> ({codeSet.system})</span>
    </li>
    {/each}
</ul>

<style>
    span {
        color: grey;
    }
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
        background-color: #00d9c0;
    }
    li.selected {
        background-color: var(--pal-heading-bg, black);
        color: var(--pal-heading-fg, white);
    }
</style>
