<script lang="ts">
    import { currentCodeSet, codeSets } from "../lib/stores";
    import type { CodeSet } from "../lib/types";
    import Input from "./Input.svelte";

    let thisCodeSet: CodeSet;
    $: {
        if (currentCodeSet !== undefined) {
            thisCodeSet = $codeSets.find((item) => item.id === $currentCodeSet);
        }
    }
</script>

<section>
    {#if thisCodeSet !== undefined}
        <h3>[{thisCodeSet.id}] {thisCodeSet.name} ({thisCodeSet.system})</h3>
        <form>
            {#each thisCodeSet.codes as code, index}
                <Input label="Code" bind:value={code.code} />
                <Input label="Value" bind:value={code.value} />
                <br />
            {/each}
        </form>
    {/if}
</section>

<style>
    input {
        color: var(--pal-input-fg, black);
        background-color: var(--pal-heading-bg, white);
    }
</style>
