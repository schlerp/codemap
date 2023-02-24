<script lang="ts">
    import { codeSets, currentCodeSet } from "../lib/stores";

    function setCodeSet(id: number) {
        currentCodeSet.set(id);
    }
</script>

<div>
    <h3>Codesets</h3>
    <ul>
        {#each $codeSets as codeSet}
            <li
                class={$currentCodeSet === codeSet.id ? "selected" : ""}
                on:click={() => setCodeSet(codeSet.id)}
            >
                {codeSet.name}
                <span> ({codeSet.system})</span>
            </li>
        {/each}
    </ul>
</div>

<style>
    div {
        border: 0.1rem solid black;
        border-radius: var(--padding-vsmall, 0.25rem);
        margin-inline: 0.5rem;
    }
    span {
        color: grey;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        padding-inline: var(--padding, 1rem);
        margin-inline: var(--padding-small, 0.5rem);
        padding-block: var(--padding-vsmall, 0.25rem);
        margin-block: var(--padding-small, 0.5rem);
        border-radius: var(--padding-vsmall, 0.25rem);
        text-align: center;
    }
    li:hover {
        cursor: pointer;
        color: #00d9c0;
    }
    li.selected {
        background-color: var(--pal-heading-bg, black);
        color: var(--pal-heading-fg, white);
    }
    h3 {
        padding-inline: var(--padding, 1rem);
    }
</style>
