<script lang="ts">
    import safeid from "../lib/utils";
    export let name: string = safeid();
    export let label: string = name;
    export let disabled: boolean = false;
    export let value: string | number | boolean;
    const groupId: string = `group_${name}`;
    const labelId: string = `label_${name}`;
    const controlId: string = `control_${name}`;
</script>

<div id={groupId}>
    <label id={labelId} for={controlId}>{label}</label>
    <input id={controlId} {name} type="text" bind:value {disabled} />
</div>

<style>
    div {
        border: 0.1rem solid var(--pal-border, black);
        border-radius: var(--spacing-small, 0.25rem);
        position: relative;
        margin-top: var(--spacing, 1rem);

    }
    input {
        width: calc(100% - calc(2 * var(--spacing, 1rem)));
        margin: var(--spacing-small, 0.5rem);
        border: none;
        outline: none;
        color: var(--pal-input-fg, black);
        background-color: var(--pal-heading-bg, white);
    }
    label {
        color: var(--pal-heading-fg, black);
        position: absolute;
        transform: translate(
            calc(2 * var(--spacing, 0.5rem)),
            calc(-1.5 * var(--spacing, 0.5rem))
        );
        padding-left: calc(var(--spacing, 0.5rem) / 2);
        padding-right: calc(var(--spacing, 0.5rem) / 2);
        background-color: white;
    }
    input:invalid {
        color: var(--pal-error, red);
        border-bottom: 1px solid var(--pal-error, red);
    }
</style>
